# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ThinkingConfigEnabledParam"]


class ThinkingConfigEnabledParam(TypedDict, total=False):
    budget_tokens: Required[int]
    """Determines how many tokens Haijun can use for its internal reasoning process.

    Larger budgets can enable more thorough analysis for complex problems, improving
    response quality.

    Must be â‰¥1024 and less than `max_tokens`.

    See
    [extended thinking](https://raw.haijun.my.id/docs/en/build-with-haijun/extended-thinking)
    for details.
    """

    type: Required[Literal["enabled"]]

    display: Optional[Literal["summarized", "omitted"]]
    """Controls how thinking content appears in the response.

    When set to `summarized`, thinking is returned normally. When set to `omitted`,
    thinking content is redacted but a signature is returned for multi-turn
    continuity. Defaults to `summarized`.
    """
