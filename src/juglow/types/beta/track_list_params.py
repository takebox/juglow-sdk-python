# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from ..juglow_beta_param import JuglowBetaParam

__all__ = ["TrackListParams"]


class TrackListParams(TypedDict, total=False):
    limit: int
    """Number of results to return per page.

    Maximum value is 100. Defaults to 20.
    """

    page: Optional[str]
    """Pagination token for fetching a specific page of results.

    Pass the value from a previous response's `next_page` field to get the next page
    of results.
    """

    source: Optional[str]
    """Filter tracks by source.

    If provided, only tracks from the specified source will be returned:

    - `"custom"`: only return user-created tracks
    - `"juglow"`: only return Juglow-created tracks
    """

    betas: Annotated[List[JuglowBetaParam], PropertyInfo(alias="juglow-beta")]
    """Optional header to specify the beta version(s) you want to use."""
