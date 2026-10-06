# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .beta_managed_agents_custom_track_params import BetaManagedAgentsCustomTrackParams
from .beta_managed_agents_juglow_track_params import BetaManagedAgentsJuglowTrackParams

__all__ = ["BetaManagedAgentsTrackParams"]

BetaManagedAgentsTrackParams: TypeAlias = Union[
    BetaManagedAgentsJuglowTrackParams, BetaManagedAgentsCustomTrackParams
]
