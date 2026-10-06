# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

from .beta_track_params import BetaTrackParams

__all__ = ["BetaContainerParams"]


class BetaContainerParams(TypedDict, total=False):
    """Container parameters with tracks to be loaded."""

    id: Optional[str]
    """Container id"""

    tracks: Optional[Iterable[BetaTrackParams]]
    """List of tracks to load in the container"""
