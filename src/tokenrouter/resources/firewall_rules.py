# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import firewall_rule_create_params, firewall_rule_update_params
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
from ..types.firewall_rule_list_response import FirewallRuleListResponse
from ..types.firewall_rule_create_response import FirewallRuleCreateResponse
from ..types.firewall_rule_delete_response import FirewallRuleDeleteResponse
from ..types.firewall_rule_update_response import FirewallRuleUpdateResponse
from ..types.firewall_rule_retrieve_response import FirewallRuleRetrieveResponse

__all__ = ["FirewallRulesResource", "AsyncFirewallRulesResource"]


class FirewallRulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FirewallRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tokenrouter/tokenrouter-python#accessing-raw-response-data-eg-headers
        """
        return FirewallRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FirewallRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tokenrouter/tokenrouter-python#with_streaming_response
        """
        return FirewallRulesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        action: Literal["block", "mask", "warn"],
        is_enabled: bool,
        name: str,
        pattern: str,
        priority: int,
        scope: Literal["prompt", "response"],
        type: Literal["substring", "regex"],
        replacement: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FirewallRuleCreateResponse:
        """
        Creates a new firewall rule for the authenticated user.

        **Note**: This endpoint requires a paid plan.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/firewall-rules",
            body=maybe_transform(
                {
                    "action": action,
                    "is_enabled": is_enabled,
                    "name": name,
                    "pattern": pattern,
                    "priority": priority,
                    "scope": scope,
                    "type": type,
                    "replacement": replacement,
                },
                firewall_rule_create_params.FirewallRuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FirewallRuleCreateResponse,
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
    ) -> FirewallRuleRetrieveResponse:
        """
        Returns a single firewall rule by ID for the authenticated user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v1/firewall-rules/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FirewallRuleRetrieveResponse,
        )

    def update(
        self,
        id: int,
        *,
        action: Literal["block", "mask", "warn"] | Omit = omit,
        is_enabled: bool | Omit = omit,
        name: str | Omit = omit,
        pattern: str | Omit = omit,
        priority: int | Omit = omit,
        replacement: Optional[str] | Omit = omit,
        scope: Literal["prompt", "response"] | Omit = omit,
        type: Literal["substring", "regex"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FirewallRuleUpdateResponse:
        """Updates an existing firewall rule.

        All fields are optional.

        **Note**: This endpoint requires a paid plan.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/v1/firewall-rules/{id}",
            body=maybe_transform(
                {
                    "action": action,
                    "is_enabled": is_enabled,
                    "name": name,
                    "pattern": pattern,
                    "priority": priority,
                    "replacement": replacement,
                    "scope": scope,
                    "type": type,
                },
                firewall_rule_update_params.FirewallRuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FirewallRuleUpdateResponse,
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
    ) -> FirewallRuleListResponse:
        """
        Returns all firewall rules for the authenticated user, ordered by priority
        (highest first).
        """
        return self._get(
            "/v1/firewall-rules",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FirewallRuleListResponse,
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
    ) -> FirewallRuleDeleteResponse:
        """
        Permanently deletes a firewall rule.

        **Note**: This endpoint requires a paid plan.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/v1/firewall-rules/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FirewallRuleDeleteResponse,
        )


class AsyncFirewallRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFirewallRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tokenrouter/tokenrouter-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFirewallRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFirewallRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tokenrouter/tokenrouter-python#with_streaming_response
        """
        return AsyncFirewallRulesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        action: Literal["block", "mask", "warn"],
        is_enabled: bool,
        name: str,
        pattern: str,
        priority: int,
        scope: Literal["prompt", "response"],
        type: Literal["substring", "regex"],
        replacement: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FirewallRuleCreateResponse:
        """
        Creates a new firewall rule for the authenticated user.

        **Note**: This endpoint requires a paid plan.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/firewall-rules",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "is_enabled": is_enabled,
                    "name": name,
                    "pattern": pattern,
                    "priority": priority,
                    "scope": scope,
                    "type": type,
                    "replacement": replacement,
                },
                firewall_rule_create_params.FirewallRuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FirewallRuleCreateResponse,
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
    ) -> FirewallRuleRetrieveResponse:
        """
        Returns a single firewall rule by ID for the authenticated user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v1/firewall-rules/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FirewallRuleRetrieveResponse,
        )

    async def update(
        self,
        id: int,
        *,
        action: Literal["block", "mask", "warn"] | Omit = omit,
        is_enabled: bool | Omit = omit,
        name: str | Omit = omit,
        pattern: str | Omit = omit,
        priority: int | Omit = omit,
        replacement: Optional[str] | Omit = omit,
        scope: Literal["prompt", "response"] | Omit = omit,
        type: Literal["substring", "regex"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FirewallRuleUpdateResponse:
        """Updates an existing firewall rule.

        All fields are optional.

        **Note**: This endpoint requires a paid plan.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/v1/firewall-rules/{id}",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "is_enabled": is_enabled,
                    "name": name,
                    "pattern": pattern,
                    "priority": priority,
                    "replacement": replacement,
                    "scope": scope,
                    "type": type,
                },
                firewall_rule_update_params.FirewallRuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FirewallRuleUpdateResponse,
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
    ) -> FirewallRuleListResponse:
        """
        Returns all firewall rules for the authenticated user, ordered by priority
        (highest first).
        """
        return await self._get(
            "/v1/firewall-rules",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FirewallRuleListResponse,
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
    ) -> FirewallRuleDeleteResponse:
        """
        Permanently deletes a firewall rule.

        **Note**: This endpoint requires a paid plan.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/v1/firewall-rules/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FirewallRuleDeleteResponse,
        )


class FirewallRulesResourceWithRawResponse:
    def __init__(self, firewall_rules: FirewallRulesResource) -> None:
        self._firewall_rules = firewall_rules

        self.create = to_raw_response_wrapper(
            firewall_rules.create,
        )
        self.retrieve = to_raw_response_wrapper(
            firewall_rules.retrieve,
        )
        self.update = to_raw_response_wrapper(
            firewall_rules.update,
        )
        self.list = to_raw_response_wrapper(
            firewall_rules.list,
        )
        self.delete = to_raw_response_wrapper(
            firewall_rules.delete,
        )


class AsyncFirewallRulesResourceWithRawResponse:
    def __init__(self, firewall_rules: AsyncFirewallRulesResource) -> None:
        self._firewall_rules = firewall_rules

        self.create = async_to_raw_response_wrapper(
            firewall_rules.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            firewall_rules.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            firewall_rules.update,
        )
        self.list = async_to_raw_response_wrapper(
            firewall_rules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            firewall_rules.delete,
        )


class FirewallRulesResourceWithStreamingResponse:
    def __init__(self, firewall_rules: FirewallRulesResource) -> None:
        self._firewall_rules = firewall_rules

        self.create = to_streamed_response_wrapper(
            firewall_rules.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            firewall_rules.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            firewall_rules.update,
        )
        self.list = to_streamed_response_wrapper(
            firewall_rules.list,
        )
        self.delete = to_streamed_response_wrapper(
            firewall_rules.delete,
        )


class AsyncFirewallRulesResourceWithStreamingResponse:
    def __init__(self, firewall_rules: AsyncFirewallRulesResource) -> None:
        self._firewall_rules = firewall_rules

        self.create = async_to_streamed_response_wrapper(
            firewall_rules.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            firewall_rules.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            firewall_rules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            firewall_rules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            firewall_rules.delete,
        )
