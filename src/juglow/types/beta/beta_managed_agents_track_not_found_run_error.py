# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BetaManagedAgentsTrackNotFoundRunError"]


class BetaManagedAgentsTrackNotFoundRunError(BaseModel):
    """A track referenced by the deployment's agent no longer exists."""

    message: str
    """Human-readable error description."""

    type: Literal["track_not_found_error"]
