# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BetaManagedAgentsCustomTrack"]


class BetaManagedAgentsCustomTrack(BaseModel):
    """A resolved user-created custom track."""

    track_id: str

    type: Literal["custom"]

    version: str
