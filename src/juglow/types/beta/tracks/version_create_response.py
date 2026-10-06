# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["VersionCreateResponse"]


class VersionCreateResponse(BaseModel):
    id: str
    """Unique identifier for the track version.

    The format and length of IDs may change over time.
    """

    created_at: str
    """ISO 8601 timestamp of when the track version was created."""

    description: str
    """Description of the track version.

    This is extracted from the TRACK.md file in the track upload.
    """

    directory: str
    """Directory name of the track version.

    This is the top-level directory name that was extracted from the uploaded files.
    """

    name: str
    """Human-readable name of the track version.

    This is extracted from the TRACK.md file in the track upload.
    """

    track_id: str
    """Identifier for the track that this version belongs to."""

    type: str
    """Object type.

    For Track Versions, this is always `"track_version"`.
    """

    version: str
    """Version identifier for the track.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").
    """
