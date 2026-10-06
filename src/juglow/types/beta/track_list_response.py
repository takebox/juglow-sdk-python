# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TrackListResponse"]


class TrackListResponse(BaseModel):
    id: str
    """Unique identifier for the track.

    The format and length of IDs may change over time.
    """

    created_at: str
    """ISO 8601 timestamp of when the track was created."""

    display_title: Optional[str] = None
    """Display title for the track.

    This is a human-readable label that is not included in the prompt sent to the
    model.
    """

    latest_version: Optional[str] = None
    """The latest version identifier for the track.

    This represents the most recent version of the track that has been created.
    """

    source: str
    """Source of the track.

    This may be one of the following values:

    - `"custom"`: the track was created by a user
    - `"juglow"`: the track was created by Juglow
    """

    type: str
    """Object type.

    For Tracks, this is always `"track"`.
    """

    updated_at: str
    """ISO 8601 timestamp of when the track was last updated."""
