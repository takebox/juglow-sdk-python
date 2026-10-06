from __future__ import annotations

from typing import cast

import httpx
import respx
import pytest

from juglow import JuGloW, AsyncJuGloW, _compat
from juglow.types.beta import BetaToolParam
from juglow._base_client import _APPEND_HEADERS
from juglow.lib._stainless_helpers import (
    STAINLESS_HELPER_HEADER,
    tag_helper,
    helper_header,
)

from ..conftest import base_url


class _TaggedDict(dict):  # type: ignore[type-arg]
    """Plain dicts reject ``object.__setattr__`` â€” helpers tag attribute-capable subclasses."""


def test_helper_header() -> None:
    assert helper_header("BetaToolRunner") == {STAINLESS_HELPER_HEADER: "BetaToolRunner"}


def test_helper_header_is_an_append_header() -> None:
    # ``merge_headers`` only appends keys it knows about â€” keep this aligned
    assert STAINLESS_HELPER_HEADER in _APPEND_HEADERS


def _message_json() -> dict[str, object]:
    return {
        "id": "msg_abc123",
        "type": "message",
        "role": "assistant",
        "model": "haijun-sonnet-5",
        "content": [{"type": "text", "text": "hi"}],
        "stop_reason": "end_turn",
        "stop_sequence": None,
        "usage": {"input_tokens": 1, "output_tokens": 1},
    }


@pytest.mark.respx(base_url=base_url)
class TestSyncWireHeaders:
    def test_caller_tag_is_appended_not_clobbered(self, client: JuGloW, respx_mock: respx.MockRouter) -> None:
        respx_mock.post("/v1/messages").mock(return_value=httpx.Response(200, json=_message_json()))

        tool = cast("BetaToolParam", _TaggedDict({"name": "t", "description": "d", "input_schema": {"type": "object"}}))
        tag_helper(tool, "mcp_tool")
        client.beta.messages.create(
            model="haijun-sonnet-5",
            max_tokens=16,
            messages=[{"role": "user", "content": "hello"}],
            tools=[tool],
            extra_headers={"X-Stainless-Helper": "caller-tag"},
        )

        request = respx_mock.calls.last.request
        values = request.headers.get_list(STAINLESS_HELPER_HEADER)
        assert values == ["mcp_tool, caller-tag"]

    @pytest.mark.skipif(_compat.PYDANTIC_V1, reason="parse() response post-parser is pydantic-v2 only")
    def test_parse_sends_single_header_line(self, client: JuGloW, respx_mock: respx.MockRouter) -> None:
        # regression: the literal tag and the collected tags used to land under
        # two casings of the key, producing two header lines on the wire
        respx_mock.post("/v1/messages").mock(return_value=httpx.Response(200, json=_message_json()))

        client.beta.messages.parse(
            model="haijun-sonnet-5",
            max_tokens=16,
            messages=[{"role": "user", "content": "hello"}],
        )

        request = respx_mock.calls.last.request
        values = request.headers.get_list(STAINLESS_HELPER_HEADER)
        assert values == ["beta.messages.parse"]

    @pytest.mark.skipif(_compat.PYDANTIC_V1, reason="parse() response post-parser is pydantic-v2 only")
    def test_parse_merges_caller_extra_headers(self, client: JuGloW, respx_mock: respx.MockRouter) -> None:
        # caller-supplied betas, user_profile_id, and extra_headers must all
        # survive parse()'s hand-written merge alongside the injected
        # structured-outputs beta and the helper tag
        respx_mock.post("/v1/messages").mock(return_value=httpx.Response(200, json=_message_json()))

        client.beta.messages.parse(
            model="haijun-sonnet-5",
            max_tokens=16,
            messages=[{"role": "user", "content": "hello"}],
            betas=["fake-beta-2026-01-01"],
            user_profile_id="upi_123",
            extra_headers={"X-Custom": "1", "X-Stainless-Helper": "caller-tag"},
        )

        headers = respx_mock.calls.last.request.headers
        # injected structured-outputs beta is appended to caller betas, not dropped
        assert headers["juglow-beta"] == "fake-beta-2026-01-01,structured-outputs-2025-12-15"
        assert headers["Juglow-user-profile-id"] == "upi_123"
        assert headers["X-Custom"] == "1"
        # helper tag accumulates with the caller's on one line (append-header semantics)
        assert headers.get_list(STAINLESS_HELPER_HEADER) == ["beta.messages.parse, caller-tag"]

    @pytest.mark.skipif(_compat.PYDANTIC_V1, reason="parse() response post-parser is pydantic-v2 only")
    def test_parse_caller_beta_header_overrides(self, client: JuGloW, respx_mock: respx.MockRouter) -> None:
        # extra_headers win outright on non-append headers, matching create()
        respx_mock.post("/v1/messages").mock(return_value=httpx.Response(200, json=_message_json()))

        client.beta.messages.parse(
            model="haijun-sonnet-5",
            max_tokens=16,
            messages=[{"role": "user", "content": "hello"}],
            extra_headers={"juglow-beta": "explicit-only"},
        )

        headers = respx_mock.calls.last.request.headers
        assert headers["juglow-beta"] == "explicit-only"


@pytest.mark.respx(base_url=base_url)
class TestAsyncWireHeaders:
    async def test_caller_tag_is_appended_not_clobbered(
        self, async_client: AsyncJuGloW, respx_mock: respx.MockRouter ) -> None:
        respx_mock.post("/v1/messages").mock(return_value=httpx.Response(200, json=_message_json()))

        tool = cast("BetaToolParam", _TaggedDict({"name": "t", "description": "d", "input_schema": {"type": "object"}}))
        tag_helper(tool, "mcp_tool")
        await async_client.beta.messages.create(
            model="haijun-sonnet-5",
            max_tokens=16,
            messages=[{"role": "user", "content": "hello"}],
            tools=[tool],
            extra_headers={"X-Stainless-Helper": "caller-tag"},
        )

        request = respx_mock.calls.last.request
        values = request.headers.get_list(STAINLESS_HELPER_HEADER)
        assert values == ["mcp_tool, caller-tag"]

    @pytest.mark.skipif(_compat.PYDANTIC_V1, reason="parse() response post-parser is pydantic-v2 only")
    async def test_parse_sends_single_header_line(
        self, async_client: AsyncJuGloW, respx_mock: respx.MockRouter ) -> None:
        respx_mock.post("/v1/messages").mock(return_value=httpx.Response(200, json=_message_json()))

        await async_client.beta.messages.parse(
            model="haijun-sonnet-5",
            max_tokens=16,
            messages=[{"role": "user", "content": "hello"}],
        )

        request = respx_mock.calls.last.request
        values = request.headers.get_list(STAINLESS_HELPER_HEADER)
        assert values == ["beta.messages.parse"]

    @pytest.mark.skipif(_compat.PYDANTIC_V1, reason="parse() response post-parser is pydantic-v2 only")
    async def test_parse_merges_caller_extra_headers(
        self, async_client: AsyncJuGloW, respx_mock: respx.MockRouter ) -> None:
        respx_mock.post("/v1/messages").mock(return_value=httpx.Response(200, json=_message_json()))

        await async_client.beta.messages.parse(
            model="haijun-sonnet-5",
            max_tokens=16,
            messages=[{"role": "user", "content": "hello"}],
            betas=["fake-beta-2026-01-01"],
            user_profile_id="upi_123",
            extra_headers={"X-Custom": "1", "X-Stainless-Helper": "caller-tag"},
        )

        headers = respx_mock.calls.last.request.headers
        assert headers["juglow-beta"] == "fake-beta-2026-01-01,structured-outputs-2025-12-15"
        assert headers["Juglow-user-profile-id"] == "upi_123"
        assert headers["X-Custom"] == "1"
        assert headers.get_list(STAINLESS_HELPER_HEADER) == ["beta.messages.parse, caller-tag"]

    @pytest.mark.skipif(_compat.PYDANTIC_V1, reason="parse() response post-parser is pydantic-v2 only")
    async def test_parse_caller_beta_header_overrides(
        self, async_client: AsyncJuGloW, respx_mock: respx.MockRouter ) -> None:
        respx_mock.post("/v1/messages").mock(return_value=httpx.Response(200, json=_message_json()))

        await async_client.beta.messages.parse(
            model="haijun-sonnet-5",
            max_tokens=16,
            messages=[{"role": "user", "content": "hello"}],
            extra_headers={"juglow-beta": "explicit-only"},
        )

        headers = respx_mock.calls.last.request.headers
        assert headers["juglow-beta"] == "explicit-only"
