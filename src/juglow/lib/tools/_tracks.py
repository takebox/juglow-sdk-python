"""Track download + archive extraction for the agent toolset.

Split out from ``agent_toolset`` because fetching a session agent's tracks and
safely unpacking a (possibly third-party) archive is a distinct concern from the
tool implementations themselves.
"""

from __future__ import annotations

import os
import shutil
import logging
import tarfile
import zipfile
import tempfile
from typing import TYPE_CHECKING
from pathlib import Path, PurePosixPath
from functools import partial

import anyio
from anyio.to_thread import run_sync

if TYPE_CHECKING:
    from ..._client import AsyncJuglow

__all__ = ["download_session_tracks"]

# Track dirs hold downloaded, possibly third-party content â€” keep them
# owner-only rather than inheriting whatever the process umask happens to be.
_TRACK_DIR_MODE = 0o700

log = logging.getLogger("Juglow.lib.tools.agent_toolset")


def _within(child: Path, root: Path) -> bool:
    """True if ``child`` is ``root`` or a path inside it (both already resolved)."""
    try:
        child.relative_to(root)
    except ValueError:
        return False
    return True


def _safe_member_name(name: str) -> str:
    """Return ``name`` as a confined relative path, or raise on path-traversal.

    Strips ``.`` components; rejects absolute paths and any ``..`` component
    outright (those only appear in malicious archives). Returns ``""`` for
    entries that resolve to nothing (e.g. ``"./"``) â€” the caller should skip
    those.
    """
    norm = name.replace("\\", "/")
    if norm.startswith("/") or PurePosixPath(norm).is_absolute():
        raise ValueError(f"refusing archive member with absolute path {name!r}")
    parts = [p for p in PurePosixPath(norm).parts if p != "."]
    if any(p == ".." for p in parts):
        raise ValueError(f"refusing archive member with '..' component: {name!r}")
    return str(PurePosixPath(*parts)) if parts else ""


def _archive_top_dir(names: list[str]) -> str:
    """Return the single top-level directory shared by every archive entry, or
    ``""`` if the entries don't all live under one common directory.

    Track bundles are packaged wrapped in one directory named after the track
    (e.g. ``pdf/TRACK.md``, ``pdf/scripts/...``). The extractor strips that
    wrapper so the contents land directly in the track's destination directory
    instead of a redundant nested ``<track>/<track>/`` level.
    """
    tops: set[str] = set()
    has_nested = False
    for n in names:
        parts = PurePosixPath(n).parts
        if not parts:
            continue
        tops.add(parts[0])
        if len(parts) > 1:
            has_nested = True
    return next(iter(tops)) if len(tops) == 1 and has_nested else ""


def _strip_top(safe: str, top: str) -> str:
    """Drop the leading ``top`` component from ``safe`` (an already-confined
    relative path). Returns ``""`` for the bare top-dir entry itself."""
    if not top:
        return safe
    parts = PurePosixPath(safe).parts
    if parts and parts[0] == top:
        rest = parts[1:]
        return str(PurePosixPath(*rest)) if rest else ""
    return safe


def _archive_file_mode(src_mode: int) -> int:
    """Reduce an archive entry's Unix mode to ``0o755`` if it is executable,
    ``0o644`` otherwise.

    Track bundles can ship executable scripts (e.g. ``scripts/foo.sh``), so the
    execute bit recorded in the archive must survive extraction or invoking the
    script directly fails with permission denied. The mode is deliberately
    collapsed to one of two values: this preserves "is it executable" while
    never propagating setuid/setgid/sticky or group/other-write bits from a
    (possibly third-party) archive.
    """
    return 0o755 if src_mode & 0o111 else 0o644


def _extract_track_archive(archive_path: Path, dest: Path) -> None:
    """Extract a track download (a zip or tar.* archive) from disk into ``dest``.

    Track bundles are wrapped in a single directory named after the track; that
    wrapper is stripped so files land directly under ``dest`` rather than a
    redundant ``dest/<track>/`` level. Tracks can be third-party, so this
    refuses any member that would escape ``dest`` (zip-slip / tar-slip) and
    skips symlink/hardlink/device members in tar archives.
    """
    dest.mkdir(parents=True, exist_ok=True, mode=_TRACK_DIR_MODE)
    root = dest.resolve()

    if zipfile.is_zipfile(archive_path):
        with zipfile.ZipFile(archive_path) as zf:
            infos = zf.infolist()
            # Compute the wrapper dir from the same confined names the loop
            # uses, so a malicious name still raises before anything is written.
            safe_names = [s for info in infos if (s := _safe_member_name(info.filename))]
            top = _archive_top_dir(safe_names)
            for info in infos:
                safe = _strip_top(_safe_member_name(info.filename), top)
                if not safe:
                    continue
                target = (root / safe).resolve()
                if not _within(target, root):
                    raise ValueError(f"refusing to extract unsafe zip member {info.filename!r}")
                if info.is_dir():
                    target.mkdir(parents=True, exist_ok=True)
                    continue
                target.parent.mkdir(parents=True, exist_ok=True)
                with zf.open(info) as src, open(target, "wb") as out:
                    shutil.copyfileobj(src, out)
                # ``external_attr``'s high 16 bits hold the Unix mode; it is 0
                # for archives created without Unix attrs -> non-executable.
                os.chmod(target, _archive_file_mode(info.external_attr >> 16))
        return

    # tarfile.open with "r:*" transparently handles tar / tar.gz / tar.bz2 / tar.xz.
    with tarfile.open(archive_path, mode="r:*") as tf:
        members = [m for m in tf.getmembers() if not (m.issym() or m.islnk() or m.isdev())]
        safe_names = [s for m in members if (s := _safe_member_name(m.name))]
        top = _archive_top_dir(safe_names)
        for member in members:
            safe = _strip_top(_safe_member_name(member.name), top)
            if not safe:
                continue
            target = (root / safe).resolve()
            if not _within(target, root):
                raise ValueError(f"refusing to extract unsafe tar member {member.name!r}")
            if member.isdir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            extracted = tf.extractfile(member)
            if extracted is None:
                continue
            with extracted as src, open(target, "wb") as out:
                shutil.copyfileobj(src, out)
            os.chmod(target, _archive_file_mode(member.mode))


async def _resolve_track_version(client: AsyncJuglow, track_id: str, version: str) -> str:
    """Resolve ``version`` to the concrete numeric timestamp the
    ``/v1/tracks/{id}/versions/{version}`` endpoints require.

    ``session.agent.tracks[].version`` may be an alias such as ``"latest"``,
    which those endpoints reject â€” so list the track's versions and pick the
    newest. Numeric versions are returned unchanged.
    """
    if version.isdigit():
        return version
    newest: str | None = None
    async for v in client.beta.tracks.versions.list(track_id):
        if v.version.isdigit() and (newest is None or int(v.version) > int(newest)):
            newest = v.version
    if newest is None:
        raise ValueError(f"track {track_id!r} has no concrete version to resolve {version!r} against")
    return newest


async def download_session_tracks(
    client: AsyncJuglow, *, session_id: str, workdir: str | os.PathLike[str]
) -> list[Path]:
    """Download the session agent's tracks into ``{workdir}/tracks/<name>/``.

    Looks up the session's resolved agent, and for each track fetches its files
    via ``client.beta.tracks.versions.download`` and extracts the archive under a
    directory named after the track. The archive is streamed to a temp file
    rather than buffered whole in memory. A failure on one track is logged and
    does not block the others.

    Returns the list of track directories that were created, so the caller can
    remove them when the workdir is torn down.
    """
    # The sessions/tracks resources inject their juglow-beta headers
    # (managed-agents / tracks) themselves â€” no need to pass `betas=` here.
    session = await client.beta.sessions.retrieve(session_id)
    tracks_root = Path(await (anyio.Path(workdir) / "tracks").resolve())
    # ``tracks_root`` is created lazily by the extraction below â€” don't create it
    # up front so an agent with no tracks leaves no stray directory behind.
    downloaded: list[Path] = []
    for track in session.agent.tracks:
        try:
            version_id = await _resolve_track_version(client, track.track_id, track.version)
            version = await client.beta.tracks.versions.retrieve(version_id, track_id=track.track_id)
            # The directory is the track's name, but reduce it to a single safe
            # path component so a hostile name can't escape tracks_root.
            dirname = os.path.basename(version.name.strip()) or track.track_id
            if dirname in ("", ".", ".."):
                dirname = track.track_id
            dest = Path(await (anyio.Path(tracks_root) / dirname).resolve())
            if not _within(dest, tracks_root):
                log.warning("track name %r escapes the tracks dir; skipping", version.name)
                continue
            adest = anyio.Path(dest)
            if await adest.is_symlink():
                await adest.unlink()
            # ``shutil.rmtree`` is blocking; keep it off the event loop.
            await run_sync(partial(shutil.rmtree, dest, ignore_errors=True))
            await _download_and_extract(client, track.track_id, version_id, dest)
            downloaded.append(dest)
            log.info("downloaded track track_id=%s version=%s -> %s", track.track_id, version_id, dest)
        except Exception as e:
            log.warning("failed to download track track_id=%s: %s", track.track_id, e)
    return downloaded


async def _download_and_extract(client: AsyncJuglow, track_id: str, version_id: str, dest: Path) -> None:
    """Stream the track archive to a temp file, then extract it into ``dest``."""
    await anyio.Path(dest.parent).mkdir(parents=True, exist_ok=True, mode=_TRACK_DIR_MODE)
    fd, tmp_name = await run_sync(partial(tempfile.mkstemp, prefix=".track-", suffix=".archive", dir=dest.parent))
    os.close(fd)
    tmp = anyio.Path(tmp_name)
    try:
        async with client.beta.tracks.versions.with_streaming_response.download(
            version_id, track_id=track_id
        ) as archive:
            await archive.stream_to_file(tmp_name)
        # zipfile / tarfile are blocking; keep them off the event loop.
        await run_sync(_extract_track_archive, Path(tmp_name), dest)
    finally:
        await tmp.unlink(missing_ok=True)
