# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Mapping, Optional, cast
from itertools import chain

import httpx

from .... import _legacy_response
from .versions import (
    Versions,
    AsyncVersions,
    VersionsWithRawResponse,
    AsyncVersionsWithRawResponse,
    VersionsWithStreamingResponse,
    AsyncVersionsWithStreamingResponse,
)
from ...._files import deepcopy_with_paths
from ...._types import (
    Body,
    Omit,
    Query,
    Headers,
    NotGiven,
    FileTypes,
    SequenceNotStr,
    omit,
    not_given,
)
from ...._utils import is_given, extract_files, path_template, maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ....pagination import SyncPageCursor, AsyncPageCursor
from ....types.beta import track_list_params, track_create_params
from ...._base_client import AsyncPaginator, make_request_options
from ....types.juglow_beta_param import JuglowBetaParam
from ....types.beta.track_list_response import TrackListResponse
from ....types.beta.track_create_response import TrackCreateResponse
from ....types.beta.track_delete_response import TrackDeleteResponse
from ....types.beta.track_retrieve_response import TrackRetrieveResponse

__all__ = ["Tracks", "AsyncTracks"]


class Tracks(SyncAPIResource):
    @cached_property
    def versions(self) -> Versions:
        return Versions(self._client)

    @cached_property
    def with_raw_response(self) -> TracksWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Juglows/Juglow-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TracksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TracksWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Juglows/Juglow-sdk-python#with_streaming_response
        """
        return TracksWithStreamingResponse(self)

    def create(
        self,
        *,
        files: SequenceNotStr[FileTypes],
        display_title: Optional[str] | Omit = omit,
        betas: List[JuglowBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrackCreateResponse:
        """
        Create Track

        Args:
          files: Files to upload for the track.

              All files must be in the same top-level directory and must include a TRACK.md
              file at the root of that directory.

          display_title: Display title for the track.

              This is a human-readable label that is not included in the prompt sent to the
              model.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "juglow-beta": ",".join(chain((str(e) for e in betas), ["tracks-2025-10-02"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"juglow-beta": "tracks-2025-10-02", **(extra_headers or {})}
        body = deepcopy_with_paths(
            {
                "files": files,
                "display_title": display_title,
            },
            [["files", "<array>"]],
        )
        extracted_files = extract_files(cast(Mapping[str, object], body), paths=[["files", "<array>"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return self._post(
            "/v1/tracks?beta=true",
            body=maybe_transform(body, track_create_params.TrackCreateParams),
            files=extracted_files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrackCreateResponse,
        )

    def retrieve(
        self,
        track_id: str,
        *,
        betas: List[JuglowBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrackRetrieveResponse:
        """
        Get Track

        Args:
          track_id: Unique identifier for the track.

              The format and length of IDs may change over time.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not track_id:
            raise ValueError(f"Expected a non-empty value for `track_id` but received {track_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "juglow-beta": ",".join(chain((str(e) for e in betas), ["tracks-2025-10-02"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"juglow-beta": "tracks-2025-10-02", **(extra_headers or {})}
        return self._get(
            path_template("/v1/tracks/{track_id}?beta=true", track_id=track_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrackRetrieveResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        page: Optional[str] | Omit = omit,
        source: Optional[str] | Omit = omit,
        betas: List[JuglowBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPageCursor[TrackListResponse]:
        """
        List Tracks

        Args:
          limit: Number of results to return per page.

              Maximum value is 100. Defaults to 20.

          page: Pagination token for fetching a specific page of results.

              Pass the value from a previous response's `next_page` field to get the next page
              of results.

          source: Filter tracks by source.

              If provided, only tracks from the specified source will be returned:

              - `"custom"`: only return user-created tracks
              - `"juglow"`: only return Juglow-created tracks

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "juglow-beta": ",".join(chain((str(e) for e in betas), ["tracks-2025-10-02"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"juglow-beta": "tracks-2025-10-02", **(extra_headers or {})}
        return self._get_api_list(
            "/v1/tracks?beta=true",
            page=SyncPageCursor[TrackListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "source": source,
                    },
                    track_list_params.TrackListParams,
                ),
            ),
            model=TrackListResponse,
        )

    def delete(
        self,
        track_id: str,
        *,
        betas: List[JuglowBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrackDeleteResponse:
        """
        Delete Track

        Args:
          track_id: Unique identifier for the track.

              The format and length of IDs may change over time.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not track_id:
            raise ValueError(f"Expected a non-empty value for `track_id` but received {track_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "juglow-beta": ",".join(chain((str(e) for e in betas), ["tracks-2025-10-02"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"juglow-beta": "tracks-2025-10-02", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/tracks/{track_id}?beta=true", track_id=track_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrackDeleteResponse,
        )


class AsyncTracks(AsyncAPIResource):
    @cached_property
    def versions(self) -> AsyncVersions:
        return AsyncVersions(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTracksWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Juglows/Juglow-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTracksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTracksWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Juglows/Juglow-sdk-python#with_streaming_response
        """
        return AsyncTracksWithStreamingResponse(self)

    async def create(
        self,
        *,
        files: SequenceNotStr[FileTypes],
        display_title: Optional[str] | Omit = omit,
        betas: List[JuglowBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrackCreateResponse:
        """
        Create Track

        Args:
          files: Files to upload for the track.

              All files must be in the same top-level directory and must include a TRACK.md
              file at the root of that directory.

          display_title: Display title for the track.

              This is a human-readable label that is not included in the prompt sent to the
              model.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "juglow-beta": ",".join(chain((str(e) for e in betas), ["tracks-2025-10-02"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"juglow-beta": "tracks-2025-10-02", **(extra_headers or {})}
        body = deepcopy_with_paths(
            {
                "files": files,
                "display_title": display_title,
            },
            [["files", "<array>"]],
        )
        extracted_files = extract_files(cast(Mapping[str, object], body), paths=[["files", "<array>"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return await self._post(
            "/v1/tracks?beta=true",
            body=await async_maybe_transform(body, track_create_params.TrackCreateParams),
            files=extracted_files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrackCreateResponse,
        )

    async def retrieve(
        self,
        track_id: str,
        *,
        betas: List[JuglowBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrackRetrieveResponse:
        """
        Get Track

        Args:
          track_id: Unique identifier for the track.

              The format and length of IDs may change over time.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not track_id:
            raise ValueError(f"Expected a non-empty value for `track_id` but received {track_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "juglow-beta": ",".join(chain((str(e) for e in betas), ["tracks-2025-10-02"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"juglow-beta": "tracks-2025-10-02", **(extra_headers or {})}
        return await self._get(
            path_template("/v1/tracks/{track_id}?beta=true", track_id=track_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrackRetrieveResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        page: Optional[str] | Omit = omit,
        source: Optional[str] | Omit = omit,
        betas: List[JuglowBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TrackListResponse, AsyncPageCursor[TrackListResponse]]:
        """
        List Tracks

        Args:
          limit: Number of results to return per page.

              Maximum value is 100. Defaults to 20.

          page: Pagination token for fetching a specific page of results.

              Pass the value from a previous response's `next_page` field to get the next page
              of results.

          source: Filter tracks by source.

              If provided, only tracks from the specified source will be returned:

              - `"custom"`: only return user-created tracks
              - `"juglow"`: only return Juglow-created tracks

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "juglow-beta": ",".join(chain((str(e) for e in betas), ["tracks-2025-10-02"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"juglow-beta": "tracks-2025-10-02", **(extra_headers or {})}
        return self._get_api_list(
            "/v1/tracks?beta=true",
            page=AsyncPageCursor[TrackListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "source": source,
                    },
                    track_list_params.TrackListParams,
                ),
            ),
            model=TrackListResponse,
        )

    async def delete(
        self,
        track_id: str,
        *,
        betas: List[JuglowBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrackDeleteResponse:
        """
        Delete Track

        Args:
          track_id: Unique identifier for the track.

              The format and length of IDs may change over time.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not track_id:
            raise ValueError(f"Expected a non-empty value for `track_id` but received {track_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "juglow-beta": ",".join(chain((str(e) for e in betas), ["tracks-2025-10-02"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"juglow-beta": "tracks-2025-10-02", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/tracks/{track_id}?beta=true", track_id=track_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrackDeleteResponse,
        )


class TracksWithRawResponse:
    def __init__(self, tracks: Tracks) -> None:
        self._tracks = tracks

        self.create = _legacy_response.to_raw_response_wrapper(
            tracks.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            tracks.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            tracks.list,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            tracks.delete,
        )

    @cached_property
    def versions(self) -> VersionsWithRawResponse:
        return VersionsWithRawResponse(self._tracks.versions)


class AsyncTracksWithRawResponse:
    def __init__(self, tracks: AsyncTracks) -> None:
        self._tracks = tracks

        self.create = _legacy_response.async_to_raw_response_wrapper(
            tracks.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            tracks.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            tracks.list,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            tracks.delete,
        )

    @cached_property
    def versions(self) -> AsyncVersionsWithRawResponse:
        return AsyncVersionsWithRawResponse(self._tracks.versions)


class TracksWithStreamingResponse:
    def __init__(self, tracks: Tracks) -> None:
        self._tracks = tracks

        self.create = to_streamed_response_wrapper(
            tracks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tracks.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            tracks.list,
        )
        self.delete = to_streamed_response_wrapper(
            tracks.delete,
        )

    @cached_property
    def versions(self) -> VersionsWithStreamingResponse:
        return VersionsWithStreamingResponse(self._tracks.versions)


class AsyncTracksWithStreamingResponse:
    def __init__(self, tracks: AsyncTracks) -> None:
        self._tracks = tracks

        self.create = async_to_streamed_response_wrapper(
            tracks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tracks.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            tracks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tracks.delete,
        )

    @cached_property
    def versions(self) -> AsyncVersionsWithStreamingResponse:
        return AsyncVersionsWithStreamingResponse(self._tracks.versions)
