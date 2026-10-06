# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BetaTrackParams"]


class BetaTrackParams(TypedDict, total=False):
    """Specification for a track to be loaded in a container (request model)."""

    track_id: Required[str]
    """Track ID"""

    type: Required[Literal["juglow", "custom"]]
    """Type of track - either 'juglow' (built-in) or 'custom' (user-defined)"""

    version: str
    """Track version or 'latest' for most recent version"""
