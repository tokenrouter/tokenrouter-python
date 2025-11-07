# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

import httpx

from ..types import routing_rule_create_params, routing_rule_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.routing_rule_list_response import RoutingRuleListResponse
from ..types.routing_rule_create_response import RoutingRuleCreateResponse
from ..types.routing_rule_delete_response import RoutingRuleDeleteResponse
from ..types.routing_rule_update_response import RoutingRuleUpdateResponse
from ..types.routing_rule_retrieve_response import RoutingRuleRetrieveResponse

__all__ = ["RoutingRulesResource", "AsyncRoutingRulesResource"]


class RoutingRulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoutingRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tokenrouter/tokenrouter-python#accessing-raw-response-data-eg-headers
        """
        return RoutingRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutingRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tokenrouter/tokenrouter-python#with_streaming_response
        """
        return RoutingRulesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        action_json: Union[str, object],
        is_enabled: bool,
        match_json: Union[str, object],
        name: str,
        priority: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingRuleCreateResponse:
        """
        Creates a new routing rule for the authenticated user.

        **Note**: This endpoint requires a paid plan.

        Args:
          action_json: Actions to take when matched (JSON object or string)

          match_json: Conditions for matching requests (JSON object or string)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/routing-rules",
            body=maybe_transform(
                {
                    "action_json": action_json,
                    "is_enabled": is_enabled,
                    "match_json": match_json,
                    "name": name,
                    "priority": priority,
                },
                routing_rule_create_params.RoutingRuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingRuleCreateResponse,
        )

    def retrieve(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingRuleRetrieveResponse:
        """
        Returns a single routing rule by ID for the authenticated user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v1/routing-rules/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingRuleRetrieveResponse,
        )

    def update(
        self,
        id: int,
        *,
        action_json: Union[str, object] | Omit = omit,
        is_enabled: bool | Omit = omit,
        match_json: Union[str, object] | Omit = omit,
        name: str | Omit = omit,
        priority: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingRuleUpdateResponse:
        """Updates an existing routing rule.

        All fields are optional.

        **Note**: This endpoint requires a paid plan.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/v1/routing-rules/{id}",
            body=maybe_transform(
                {
                    "action_json": action_json,
                    "is_enabled": is_enabled,
                    "match_json": match_json,
                    "name": name,
                    "priority": priority,
                },
                routing_rule_update_params.RoutingRuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingRuleUpdateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingRuleListResponse:
        """
        Returns all routing rules for the authenticated user, ordered by priority
        (highest first).

        Rules are returned in the order they will be evaluated during request routing.
        """
        return self._get(
            "/v1/routing-rules",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingRuleListResponse,
        )

    def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingRuleDeleteResponse:
        """
        Permanently deletes a routing rule.

        **Note**: This endpoint requires a paid plan.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/v1/routing-rules/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingRuleDeleteResponse,
        )


class AsyncRoutingRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoutingRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tokenrouter/tokenrouter-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoutingRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutingRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tokenrouter/tokenrouter-python#with_streaming_response
        """
        return AsyncRoutingRulesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        action_json: Union[str, object],
        is_enabled: bool,
        match_json: Union[str, object],
        name: str,
        priority: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingRuleCreateResponse:
        """
        Creates a new routing rule for the authenticated user.

        **Note**: This endpoint requires a paid plan.

        Args:
          action_json: Actions to take when matched (JSON object or string)

          match_json: Conditions for matching requests (JSON object or string)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/routing-rules",
            body=await async_maybe_transform(
                {
                    "action_json": action_json,
                    "is_enabled": is_enabled,
                    "match_json": match_json,
                    "name": name,
                    "priority": priority,
                },
                routing_rule_create_params.RoutingRuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingRuleCreateResponse,
        )

    async def retrieve(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingRuleRetrieveResponse:
        """
        Returns a single routing rule by ID for the authenticated user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v1/routing-rules/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingRuleRetrieveResponse,
        )

    async def update(
        self,
        id: int,
        *,
        action_json: Union[str, object] | Omit = omit,
        is_enabled: bool | Omit = omit,
        match_json: Union[str, object] | Omit = omit,
        name: str | Omit = omit,
        priority: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingRuleUpdateResponse:
        """Updates an existing routing rule.

        All fields are optional.

        **Note**: This endpoint requires a paid plan.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/v1/routing-rules/{id}",
            body=await async_maybe_transform(
                {
                    "action_json": action_json,
                    "is_enabled": is_enabled,
                    "match_json": match_json,
                    "name": name,
                    "priority": priority,
                },
                routing_rule_update_params.RoutingRuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingRuleUpdateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingRuleListResponse:
        """
        Returns all routing rules for the authenticated user, ordered by priority
        (highest first).

        Rules are returned in the order they will be evaluated during request routing.
        """
        return await self._get(
            "/v1/routing-rules",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingRuleListResponse,
        )

    async def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingRuleDeleteResponse:
        """
        Permanently deletes a routing rule.

        **Note**: This endpoint requires a paid plan.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/v1/routing-rules/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingRuleDeleteResponse,
        )


class RoutingRulesResourceWithRawResponse:
    def __init__(self, routing_rules: RoutingRulesResource) -> None:
        self._routing_rules = routing_rules

        self.create = to_raw_response_wrapper(
            routing_rules.create,
        )
        self.retrieve = to_raw_response_wrapper(
            routing_rules.retrieve,
        )
        self.update = to_raw_response_wrapper(
            routing_rules.update,
        )
        self.list = to_raw_response_wrapper(
            routing_rules.list,
        )
        self.delete = to_raw_response_wrapper(
            routing_rules.delete,
        )


class AsyncRoutingRulesResourceWithRawResponse:
    def __init__(self, routing_rules: AsyncRoutingRulesResource) -> None:
        self._routing_rules = routing_rules

        self.create = async_to_raw_response_wrapper(
            routing_rules.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            routing_rules.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            routing_rules.update,
        )
        self.list = async_to_raw_response_wrapper(
            routing_rules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            routing_rules.delete,
        )


class RoutingRulesResourceWithStreamingResponse:
    def __init__(self, routing_rules: RoutingRulesResource) -> None:
        self._routing_rules = routing_rules

        self.create = to_streamed_response_wrapper(
            routing_rules.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            routing_rules.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            routing_rules.update,
        )
        self.list = to_streamed_response_wrapper(
            routing_rules.list,
        )
        self.delete = to_streamed_response_wrapper(
            routing_rules.delete,
        )


class AsyncRoutingRulesResourceWithStreamingResponse:
    def __init__(self, routing_rules: AsyncRoutingRulesResource) -> None:
        self._routing_rules = routing_rules

        self.create = async_to_streamed_response_wrapper(
            routing_rules.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            routing_rules.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            routing_rules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            routing_rules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            routing_rules.delete,
        )
