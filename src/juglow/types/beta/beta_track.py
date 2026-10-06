# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BetaTrack"]


class BetaTrack(BaseModel):
    """A track that was loaded in a container (response model)."""

    track_id: str
    """Track ID"""

    type: Literal["juglow", "custom"]
    """Type of track - either 'juglow' (built-in) or 'custom' (user-defined)"""

    version: str
    """Track version or 'latest' for most recent version"""
