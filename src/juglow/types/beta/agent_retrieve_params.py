# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from ..juglow_beta_param import JuglowBetaParam

__all__ = ["AgentRetrieveParams"]


class AgentRetrieveParams(TypedDict, total=False):
    version: int
    """Agent version.

    Omit for the most recent version. Must be at least 1 if specified.
    """

    betas: Annotated[List[JuglowBetaParam], PropertyInfo(alias="juglow-beta")]
    """Optional header to specify the beta version(s) you want to use."""
