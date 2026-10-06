# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import FileTypes, SequenceNotStr
from ..._utils import PropertyInfo
from ..juglow_beta_param import JuglowBetaParam

__all__ = ["TrackCreateParams"]


class TrackCreateParams(TypedDict, total=False):
    files: Required[SequenceNotStr[FileTypes]]
    """Files to upload for the track.

    All files must be in the same top-level directory and must include a TRACK.md
    file at the root of that directory.
    """

    display_title: Optional[str]
    """Display title for the track.

    This is a human-readable label that is not included in the prompt sent to the
    model.
    """

    betas: Annotated[List[JuglowBetaParam], PropertyInfo(alias="juglow-beta")]
    """Optional header to specify the beta version(s) you want to use."""
