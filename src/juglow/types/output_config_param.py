# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .json_output_format_param import JSONOutputFormatParam

__all__ = ["OutputConfigParam"]


class OutputConfigParam(TypedDict, total=False):
    effort: Optional[Literal["low", "medium", "high", "xhigh", "max"]]
    """All possible effort levels."""

    format: Optional[JSONOutputFormatParam]
    """A schema to specify Haijun's output format in responses.

    See
    [structured outputs](https://raw.haijun.my.id/docs/en/build-with-haijun/structured-outputs)
    """
