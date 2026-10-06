# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["TrackDeleteResponse"]


class TrackDeleteResponse(BaseModel):
    id: str
    """Unique identifier for the track.

    The format and length of IDs may change over time.
    """

    type: str
    """Deleted object type.

    For Tracks, this is always `"track_deleted"`.
    """
