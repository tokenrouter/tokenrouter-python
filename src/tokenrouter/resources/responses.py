# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import response_create_params, response_replay_params
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
from ..types.response_object import ResponseObject

__all__ = ["ResponsesResource", "AsyncResponsesResource"]


class ResponsesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tokenrouter-python#accessing-raw-response-data-eg-headers
        """
        return ResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tokenrouter-python#with_streaming_response
        """
        return ResponsesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        background: bool | Omit = omit,
        conversation: Union[str, object, None] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        model: str | Omit = omit,
        parallel_tool_calls: bool | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        prompt_cache_key: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        router_mode: Optional[Literal["balance", "cost", "quality", "latency"]] | Omit = omit,
        router_model: Optional[str] | Omit = omit,
        router_provider: Optional[Literal["openai", "anthropic", "gemini", "mistral", "deepseek"]] | Omit = omit,
        safety_identifier: Optional[str] | Omit = omit,
        service_tier: Literal["auto", "default", "flex", "priority"] | Omit = omit,
        store: bool | Omit = omit,
        stream: bool | Omit = omit,
        stream_options: Optional[response_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tool_choice: response_create_params.ToolChoice | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        truncation: Literal["auto", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseObject:
        """
        Creates a new AI model response by routing your request to the optimal provider
        and model.

        This endpoint intelligently selects the best provider based on:

        - Your routing mode (balance, cost, quality, latency)
        - Available provider keys
        - Model capabilities and availability
        - Custom routing rules you've configured
        - Firewall rules and security policies

        The response follows OpenAI's response format for compatibility while adding
        TokenRouter-specific metadata like routing decisions and provider information.

        Args:
          input: Text, image, or file inputs to the model. Can be a simple string or an array of
              content items.

          background: Run response generation in background

          conversation: Conversation ID or object for context

          instructions: System-level instructions for the model

          max_output_tokens: Maximum number of tokens in the response

          max_tool_calls: Maximum number of tool calls

          metadata: Custom metadata (up to 16 key-value pairs)

          model:
              Model ID or routing mode. Supports:

              - `auto:balance` - Balanced routing (default)
              - `auto:cost` - Cost-optimized routing
              - `auto:quality` - Quality-optimized routing
              - `auto:latency` - Latency-optimized routing
              - Specific model with mode: `gpt-4o:balance`, `claude-3-7-sonnet-latest:quality`
              - Specific model: `gpt-4o`, `claude-3-7-sonnet-latest`, etc.

          parallel_tool_calls: Allow parallel tool execution

          previous_response_id: ID of previous response for context

          prompt_cache_key: Key for prompt caching (OpenAI)

          reasoning: Configuration for reasoning models (o-series, gpt-5)

          router_mode: Override routing mode (advanced)

          router_model: Override model for routing (advanced)

          router_provider: Force specific provider (advanced)

          safety_identifier: Stable identifier for policy violation detection

          service_tier: Processing priority tier

          store: Whether to store the response for later retrieval

          stream: Whether to stream the response as Server-Sent Events

          stream_options: Options for streaming responses

          temperature: Sampling temperature (0-2). Higher values make output more random.

          text: Configuration for structured text output

          tool_choice: How the model should select tools

          tools: Tools/functions the model may call

          top_logprobs: Number of top log probabilities to return (0-20)

          top_p: Nucleus sampling probability mass cutoff

          truncation: Truncation strategy

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/responses",
            body=maybe_transform(
                {
                    "input": input,
                    "background": background,
                    "conversation": conversation,
                    "instructions": instructions,
                    "max_output_tokens": max_output_tokens,
                    "max_tool_calls": max_tool_calls,
                    "metadata": metadata,
                    "model": model,
                    "parallel_tool_calls": parallel_tool_calls,
                    "previous_response_id": previous_response_id,
                    "prompt_cache_key": prompt_cache_key,
                    "reasoning": reasoning,
                    "router_mode": router_mode,
                    "router_model": router_model,
                    "router_provider": router_provider,
                    "safety_identifier": safety_identifier,
                    "service_tier": service_tier,
                    "store": store,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "text": text,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "truncation": truncation,
                },
                response_create_params.ResponseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseObject,
        )

    def replay(
        self,
        request_id: str,
        *,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseObject:
        """Replays a previously stored response by request ID.

        This is useful for:

        - Debugging and testing
        - Retrieving cached responses
        - Re-streaming previous responses

        The response can be returned in either standard JSON format or streamed format
        based on the `stream` parameter in the request body.

        Args:
          stream: Whether to stream the replayed response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._post(
            f"/v1/responses/{request_id}",
            body=maybe_transform({"stream": stream}, response_replay_params.ResponseReplayParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseObject,
        )


class AsyncResponsesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tokenrouter-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tokenrouter-python#with_streaming_response
        """
        return AsyncResponsesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        background: bool | Omit = omit,
        conversation: Union[str, object, None] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        model: str | Omit = omit,
        parallel_tool_calls: bool | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        prompt_cache_key: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        router_mode: Optional[Literal["balance", "cost", "quality", "latency"]] | Omit = omit,
        router_model: Optional[str] | Omit = omit,
        router_provider: Optional[Literal["openai", "anthropic", "gemini", "mistral", "deepseek"]] | Omit = omit,
        safety_identifier: Optional[str] | Omit = omit,
        service_tier: Literal["auto", "default", "flex", "priority"] | Omit = omit,
        store: bool | Omit = omit,
        stream: bool | Omit = omit,
        stream_options: Optional[response_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tool_choice: response_create_params.ToolChoice | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        truncation: Literal["auto", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseObject:
        """
        Creates a new AI model response by routing your request to the optimal provider
        and model.

        This endpoint intelligently selects the best provider based on:

        - Your routing mode (balance, cost, quality, latency)
        - Available provider keys
        - Model capabilities and availability
        - Custom routing rules you've configured
        - Firewall rules and security policies

        The response follows OpenAI's response format for compatibility while adding
        TokenRouter-specific metadata like routing decisions and provider information.

        Args:
          input: Text, image, or file inputs to the model. Can be a simple string or an array of
              content items.

          background: Run response generation in background

          conversation: Conversation ID or object for context

          instructions: System-level instructions for the model

          max_output_tokens: Maximum number of tokens in the response

          max_tool_calls: Maximum number of tool calls

          metadata: Custom metadata (up to 16 key-value pairs)

          model:
              Model ID or routing mode. Supports:

              - `auto:balance` - Balanced routing (default)
              - `auto:cost` - Cost-optimized routing
              - `auto:quality` - Quality-optimized routing
              - `auto:latency` - Latency-optimized routing
              - Specific model with mode: `gpt-4o:balance`, `claude-3-7-sonnet-latest:quality`
              - Specific model: `gpt-4o`, `claude-3-7-sonnet-latest`, etc.

          parallel_tool_calls: Allow parallel tool execution

          previous_response_id: ID of previous response for context

          prompt_cache_key: Key for prompt caching (OpenAI)

          reasoning: Configuration for reasoning models (o-series, gpt-5)

          router_mode: Override routing mode (advanced)

          router_model: Override model for routing (advanced)

          router_provider: Force specific provider (advanced)

          safety_identifier: Stable identifier for policy violation detection

          service_tier: Processing priority tier

          store: Whether to store the response for later retrieval

          stream: Whether to stream the response as Server-Sent Events

          stream_options: Options for streaming responses

          temperature: Sampling temperature (0-2). Higher values make output more random.

          text: Configuration for structured text output

          tool_choice: How the model should select tools

          tools: Tools/functions the model may call

          top_logprobs: Number of top log probabilities to return (0-20)

          top_p: Nucleus sampling probability mass cutoff

          truncation: Truncation strategy

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/responses",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "background": background,
                    "conversation": conversation,
                    "instructions": instructions,
                    "max_output_tokens": max_output_tokens,
                    "max_tool_calls": max_tool_calls,
                    "metadata": metadata,
                    "model": model,
                    "parallel_tool_calls": parallel_tool_calls,
                    "previous_response_id": previous_response_id,
                    "prompt_cache_key": prompt_cache_key,
                    "reasoning": reasoning,
                    "router_mode": router_mode,
                    "router_model": router_model,
                    "router_provider": router_provider,
                    "safety_identifier": safety_identifier,
                    "service_tier": service_tier,
                    "store": store,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "text": text,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "truncation": truncation,
                },
                response_create_params.ResponseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseObject,
        )

    async def replay(
        self,
        request_id: str,
        *,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseObject:
        """Replays a previously stored response by request ID.

        This is useful for:

        - Debugging and testing
        - Retrieving cached responses
        - Re-streaming previous responses

        The response can be returned in either standard JSON format or streamed format
        based on the `stream` parameter in the request body.

        Args:
          stream: Whether to stream the replayed response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._post(
            f"/v1/responses/{request_id}",
            body=await async_maybe_transform({"stream": stream}, response_replay_params.ResponseReplayParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseObject,
        )


class ResponsesResourceWithRawResponse:
    def __init__(self, responses: ResponsesResource) -> None:
        self._responses = responses

        self.create = to_raw_response_wrapper(
            responses.create,
        )
        self.replay = to_raw_response_wrapper(
            responses.replay,
        )


class AsyncResponsesResourceWithRawResponse:
    def __init__(self, responses: AsyncResponsesResource) -> None:
        self._responses = responses

        self.create = async_to_raw_response_wrapper(
            responses.create,
        )
        self.replay = async_to_raw_response_wrapper(
            responses.replay,
        )


class ResponsesResourceWithStreamingResponse:
    def __init__(self, responses: ResponsesResource) -> None:
        self._responses = responses

        self.create = to_streamed_response_wrapper(
            responses.create,
        )
        self.replay = to_streamed_response_wrapper(
            responses.replay,
        )


class AsyncResponsesResourceWithStreamingResponse:
    def __init__(self, responses: AsyncResponsesResource) -> None:
        self._responses = responses

        self.create = async_to_streamed_response_wrapper(
            responses.create,
        )
        self.replay = async_to_streamed_response_wrapper(
            responses.replay,
        )
