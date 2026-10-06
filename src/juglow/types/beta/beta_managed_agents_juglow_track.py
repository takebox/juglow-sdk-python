# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BetaManagedAgentsJuglowTrack"]


class BetaManagedAgentsJuglowTrack(BaseModel):
    """A resolved Juglow-managed track."""

    track_id: str

    type: Literal["juglow"]

    version: str
