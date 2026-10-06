# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ...juglow_beta_param import JuglowBetaParam
from .beta_managed_agents_event_params import BetaManagedAgentsEventParams

__all__ = ["EventSendParams"]


class EventSendParams(TypedDict, total=False):
    events: Required[Iterable[BetaManagedAgentsEventParams]]
    """Events to send to the `session`."""

    betas: Annotated[List[JuglowBetaParam], PropertyInfo(alias="juglow-beta")]
    """Optional header to specify the beta version(s) you want to use."""
