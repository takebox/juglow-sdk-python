# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo
from ...juglow_beta_param import JuglowBetaParam

__all__ = ["WorkListParams"]


class WorkListParams(TypedDict, total=False):
    limit: int
    """Maximum number of work items to return"""

    page: Optional[str]
    """Opaque cursor from previous response for pagination"""

    betas: Annotated[List[JuglowBetaParam], PropertyInfo(alias="juglow-beta")]
    """Optional header to specify the beta version(s) you want to use."""
