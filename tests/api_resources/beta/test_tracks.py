# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from juglow import JuGloW, AsyncJuGloW
from tests.utils import assert_matches_type
from juglow.pagination import SyncPageCursor, AsyncPageCursor
from juglow.types.beta import (
    TrackListResponse,
    TrackCreateResponse,
    TrackDeleteResponse,
    TrackRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTracks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: JuGloW) -> None:
        track = client.beta.tracks.create(
            files=[b"Example data"],
        )
        assert_matches_type(TrackCreateResponse, track, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: JuGloW) -> None:
        track = client.beta.tracks.create(
            files=[b"Example data"],
            display_title="display_title",
            betas=["string"],
        )
        assert_matches_type(TrackCreateResponse, track, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: JuGloW) -> None:
        response = client.beta.tracks.with_raw_response.create(
            files=[b"Example data"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        track = response.parse()
        assert_matches_type(TrackCreateResponse, track, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: JuGloW) -> None:
        with client.beta.tracks.with_streaming_response.create(
            files=[b"Example data"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            track = response.parse()
            assert_matches_type(TrackCreateResponse, track, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: JuGloW) -> None:
        track = client.beta.tracks.retrieve(
            track_id="track_id",
        )
        assert_matches_type(TrackRetrieveResponse, track, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: JuGloW) -> None:
        track = client.beta.tracks.retrieve(
            track_id="track_id",
            betas=["string"],
        )
        assert_matches_type(TrackRetrieveResponse, track, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: JuGloW) -> None:
        response = client.beta.tracks.with_raw_response.retrieve(
            track_id="track_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        track = response.parse()
        assert_matches_type(TrackRetrieveResponse, track, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: JuGloW) -> None:
        with client.beta.tracks.with_streaming_response.retrieve(
            track_id="track_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            track = response.parse()
            assert_matches_type(TrackRetrieveResponse, track, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: JuGloW) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `track_id` but received ''"):
            client.beta.tracks.with_raw_response.retrieve(
                track_id="",
            )

    @parametrize
    def test_method_list(self, client: JuGloW) -> None:
        track = client.beta.tracks.list()
        assert_matches_type(SyncPageCursor[TrackListResponse], track, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: JuGloW) -> None:
        track = client.beta.tracks.list(
            limit=0,
            page="page",
            source="source",
            betas=["string"],
        )
        assert_matches_type(SyncPageCursor[TrackListResponse], track, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: JuGloW) -> None:
        response = client.beta.tracks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        track = response.parse()
        assert_matches_type(SyncPageCursor[TrackListResponse], track, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: JuGloW) -> None:
        with client.beta.tracks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            track = response.parse()
            assert_matches_type(SyncPageCursor[TrackListResponse], track, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: JuGloW) -> None:
        track = client.beta.tracks.delete(
            track_id="track_id",
        )
        assert_matches_type(TrackDeleteResponse, track, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: JuGloW) -> None:
        track = client.beta.tracks.delete(
            track_id="track_id",
            betas=["string"],
        )
        assert_matches_type(TrackDeleteResponse, track, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: JuGloW) -> None:
        response = client.beta.tracks.with_raw_response.delete(
            track_id="track_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        track = response.parse()
        assert_matches_type(TrackDeleteResponse, track, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: JuGloW) -> None:
        with client.beta.tracks.with_streaming_response.delete(
            track_id="track_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            track = response.parse()
            assert_matches_type(TrackDeleteResponse, track, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: JuGloW) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `track_id` but received ''"):
            client.beta.tracks.with_raw_response.delete(
                track_id="",
            )


class TestAsyncTracks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncJuGloW) -> None:
        track = await async_client.beta.tracks.create(
            files=[b"Example data"],
        )
        assert_matches_type(TrackCreateResponse, track, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncJuGloW) -> None:
        track = await async_client.beta.tracks.create(
            files=[b"Example data"],
            display_title="display_title",
            betas=["string"],
        )
        assert_matches_type(TrackCreateResponse, track, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJuGloW) -> None:
        response = await async_client.beta.tracks.with_raw_response.create(
            files=[b"Example data"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        track = response.parse()
        assert_matches_type(TrackCreateResponse, track, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJuGloW) -> None:
        async with async_client.beta.tracks.with_streaming_response.create(
            files=[b"Example data"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            track = await response.parse()
            assert_matches_type(TrackCreateResponse, track, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncJuGloW) -> None:
        track = await async_client.beta.tracks.retrieve(
            track_id="track_id",
        )
        assert_matches_type(TrackRetrieveResponse, track, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncJuGloW) -> None:
        track = await async_client.beta.tracks.retrieve(
            track_id="track_id",
            betas=["string"],
        )
        assert_matches_type(TrackRetrieveResponse, track, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncJuGloW) -> None:
        response = await async_client.beta.tracks.with_raw_response.retrieve(
            track_id="track_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        track = response.parse()
        assert_matches_type(TrackRetrieveResponse, track, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncJuGloW) -> None:
        async with async_client.beta.tracks.with_streaming_response.retrieve(
            track_id="track_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            track = await response.parse()
            assert_matches_type(TrackRetrieveResponse, track, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncJuGloW) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `track_id` but received ''"):
            await async_client.beta.tracks.with_raw_response.retrieve(
                track_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncJuGloW) -> None:
        track = await async_client.beta.tracks.list()
        assert_matches_type(AsyncPageCursor[TrackListResponse], track, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncJuGloW) -> None:
        track = await async_client.beta.tracks.list(
            limit=0,
            page="page",
            source="source",
            betas=["string"],
        )
        assert_matches_type(AsyncPageCursor[TrackListResponse], track, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJuGloW) -> None:
        response = await async_client.beta.tracks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        track = response.parse()
        assert_matches_type(AsyncPageCursor[TrackListResponse], track, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJuGloW) -> None:
        async with async_client.beta.tracks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            track = await response.parse()
            assert_matches_type(AsyncPageCursor[TrackListResponse], track, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncJuGloW) -> None:
        track = await async_client.beta.tracks.delete(
            track_id="track_id",
        )
        assert_matches_type(TrackDeleteResponse, track, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncJuGloW) -> None:
        track = await async_client.beta.tracks.delete(
            track_id="track_id",
            betas=["string"],
        )
        assert_matches_type(TrackDeleteResponse, track, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncJuGloW) -> None:
        response = await async_client.beta.tracks.with_raw_response.delete(
            track_id="track_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        track = response.parse()
        assert_matches_type(TrackDeleteResponse, track, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncJuGloW) -> None:
        async with async_client.beta.tracks.with_streaming_response.delete(
            track_id="track_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            track = await response.parse()
            assert_matches_type(TrackDeleteResponse, track, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncJuGloW) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `track_id` but received ''"):
            await async_client.beta.tracks.with_raw_response.delete(
                track_id="",
            )
