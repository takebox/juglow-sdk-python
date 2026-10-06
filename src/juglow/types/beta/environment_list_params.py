# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from ..juglow_beta_param import JuglowBetaParam

__all__ = ["EnvironmentListParams"]


class EnvironmentListParams(TypedDict, total=False):
    include_archived: bool
    """Include archived environments in the response"""

    limit: int
    """Maximum number of environments to return"""

    page: Optional[str]
    """Opaque cursor from previous response for pagination.

    Pass the `next_page` value from the previous response.
    """

    betas: Annotated[List[JuglowBetaParam], PropertyInfo(alias="juglow-beta")]
    """Optional header to specify the beta version(s) you want to use."""
