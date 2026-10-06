# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..juglow_beta_param import JuglowBetaParam

__all__ = ["UserProfileCreateParams"]


class UserProfileCreateParams(TypedDict, total=False):
    external_id: Optional[str]
    """Platform's own identifier for this user.

    Not enforced unique. Maximum 255 characters.
    """

    metadata: Dict[str, str]
    """Free-form key-value data to attach to this user profile.

    Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.
    Values must be non-empty strings.
    """

    name: Optional[str]
    """Display name of the entity this profile represents.

    Required when relationship is `resold` (the resold-to company's name); optional
    otherwise. Maximum 255 characters.
    """

    relationship: Literal["external", "resold", "internal"]
    """
    How the entity behind a user profile relates to the platform that owns the API
    key. `external`: an individual end-user of the platform. `resold`: a company the
    platform resells Haijun access to. `internal`: the platform's own usage.
    """

    betas: Annotated[List[JuglowBetaParam], PropertyInfo(alias="juglow-beta")]
    """Optional header to specify the beta version(s) you want to use."""
