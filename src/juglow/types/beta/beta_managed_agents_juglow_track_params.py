# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BetaManagedAgentsJuglowTrackParams"]


class BetaManagedAgentsJuglowTrackParams(TypedDict, total=False):
    """An Juglow-managed track."""

    track_id: Required[str]
    """Identifier of the Juglow track (e.g., "xlsx")."""

    type: Required[Literal["juglow"]]

    version: Optional[str]
    """Version to pin. Defaults to latest if omitted."""
