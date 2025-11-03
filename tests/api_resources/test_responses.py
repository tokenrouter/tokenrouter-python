# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tokenrouter import Tokenrouter, AsyncTokenrouter
from tokenrouter.types import ResponseObject

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResponses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Tokenrouter) -> None:
        response = client.responses.create(
            input="What is the capital of France?",
        )
        assert_matches_type(ResponseObject, response, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Tokenrouter) -> None:
        response = client.responses.create(
            input="What is the capital of France?",
            background=True,
            conversation="string",
            instructions="You are a helpful assistant that provides concise answers.",
            max_output_tokens=1000,
            max_tool_calls=1,
            metadata={
                "user_id": "user_123",
                "session_id": "session_456",
            },
            model="auto:balance",
            parallel_tool_calls=True,
            previous_response_id="resp_ea9-0-b1--5f",
            prompt_cache_key="prompt_cache_key",
            reasoning={"effort": "low"},
            router_mode="balance",
            router_model="router_model",
            router_provider="openai",
            safety_identifier="safety_identifier",
            service_tier="auto",
            store=True,
            stream=True,
            stream_options={"include_usage": True},
            temperature=0.7,
            text={
                "json_schema": {
                    "name": "name",
                    "schema": {},
                    "strict": True,
                },
                "type": "text",
            },
            tool_choice="auto",
            tools=[
                {
                    "function": {
                        "description": "description",
                        "name": "name",
                        "parameters": {},
                    },
                    "type": "function",
                }
            ],
            top_logprobs=0,
            top_p=0.9,
            truncation="auto",
        )
        assert_matches_type(ResponseObject, response, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Tokenrouter) -> None:
        http_response = client.responses.with_raw_response.create(
            input="What is the capital of France?",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert_matches_type(ResponseObject, response, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Tokenrouter) -> None:
        with client.responses.with_streaming_response.create(
            input="What is the capital of France?",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = http_response.parse()
            assert_matches_type(ResponseObject, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_replay(self, client: Tokenrouter) -> None:
        response = client.responses.replay(
            request_id="req_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(ResponseObject, response, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_replay_with_all_params(self, client: Tokenrouter) -> None:
        response = client.responses.replay(
            request_id="req_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            stream=False,
        )
        assert_matches_type(ResponseObject, response, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_replay(self, client: Tokenrouter) -> None:
        http_response = client.responses.with_raw_response.replay(
            request_id="req_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert_matches_type(ResponseObject, response, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_replay(self, client: Tokenrouter) -> None:
        with client.responses.with_streaming_response.replay(
            request_id="req_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = http_response.parse()
            assert_matches_type(ResponseObject, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_replay(self, client: Tokenrouter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.responses.with_raw_response.replay(
                request_id="",
            )


class TestAsyncResponses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTokenrouter) -> None:
        response = await async_client.responses.create(
            input="What is the capital of France?",
        )
        assert_matches_type(ResponseObject, response, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTokenrouter) -> None:
        response = await async_client.responses.create(
            input="What is the capital of France?",
            background=True,
            conversation="string",
            instructions="You are a helpful assistant that provides concise answers.",
            max_output_tokens=1000,
            max_tool_calls=1,
            metadata={
                "user_id": "user_123",
                "session_id": "session_456",
            },
            model="auto:balance",
            parallel_tool_calls=True,
            previous_response_id="resp_ea9-0-b1--5f",
            prompt_cache_key="prompt_cache_key",
            reasoning={"effort": "low"},
            router_mode="balance",
            router_model="router_model",
            router_provider="openai",
            safety_identifier="safety_identifier",
            service_tier="auto",
            store=True,
            stream=True,
            stream_options={"include_usage": True},
            temperature=0.7,
            text={
                "json_schema": {
                    "name": "name",
                    "schema": {},
                    "strict": True,
                },
                "type": "text",
            },
            tool_choice="auto",
            tools=[
                {
                    "function": {
                        "description": "description",
                        "name": "name",
                        "parameters": {},
                    },
                    "type": "function",
                }
            ],
            top_logprobs=0,
            top_p=0.9,
            truncation="auto",
        )
        assert_matches_type(ResponseObject, response, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTokenrouter) -> None:
        http_response = await async_client.responses.with_raw_response.create(
            input="What is the capital of France?",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = await http_response.parse()
        assert_matches_type(ResponseObject, response, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTokenrouter) -> None:
        async with async_client.responses.with_streaming_response.create(
            input="What is the capital of France?",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = await http_response.parse()
            assert_matches_type(ResponseObject, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_replay(self, async_client: AsyncTokenrouter) -> None:
        response = await async_client.responses.replay(
            request_id="req_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(ResponseObject, response, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_replay_with_all_params(self, async_client: AsyncTokenrouter) -> None:
        response = await async_client.responses.replay(
            request_id="req_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            stream=False,
        )
        assert_matches_type(ResponseObject, response, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_replay(self, async_client: AsyncTokenrouter) -> None:
        http_response = await async_client.responses.with_raw_response.replay(
            request_id="req_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = await http_response.parse()
        assert_matches_type(ResponseObject, response, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_replay(self, async_client: AsyncTokenrouter) -> None:
        async with async_client.responses.with_streaming_response.replay(
            request_id="req_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = await http_response.parse()
            assert_matches_type(ResponseObject, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_replay(self, async_client: AsyncTokenrouter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.responses.with_raw_response.replay(
                request_id="",
            )
