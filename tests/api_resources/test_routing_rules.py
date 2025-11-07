# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tokenrouter import Tokenrouter, AsyncTokenrouter
from tokenrouter.types import (
    RoutingRuleListResponse,
    RoutingRuleCreateResponse,
    RoutingRuleDeleteResponse,
    RoutingRuleUpdateResponse,
    RoutingRuleRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoutingRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Tokenrouter) -> None:
        routing_rule = client.routing_rules.create(
            action_json="string",
            is_enabled=True,
            match_json="string",
            name="name",
            priority=-1000,
        )
        assert_matches_type(RoutingRuleCreateResponse, routing_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Tokenrouter) -> None:
        response = client.routing_rules.with_raw_response.create(
            action_json="string",
            is_enabled=True,
            match_json="string",
            name="name",
            priority=-1000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_rule = response.parse()
        assert_matches_type(RoutingRuleCreateResponse, routing_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Tokenrouter) -> None:
        with client.routing_rules.with_streaming_response.create(
            action_json="string",
            is_enabled=True,
            match_json="string",
            name="name",
            priority=-1000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_rule = response.parse()
            assert_matches_type(RoutingRuleCreateResponse, routing_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Tokenrouter) -> None:
        routing_rule = client.routing_rules.retrieve(
            1,
        )
        assert_matches_type(RoutingRuleRetrieveResponse, routing_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Tokenrouter) -> None:
        response = client.routing_rules.with_raw_response.retrieve(
            1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_rule = response.parse()
        assert_matches_type(RoutingRuleRetrieveResponse, routing_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Tokenrouter) -> None:
        with client.routing_rules.with_streaming_response.retrieve(
            1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_rule = response.parse()
            assert_matches_type(RoutingRuleRetrieveResponse, routing_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Tokenrouter) -> None:
        routing_rule = client.routing_rules.update(
            id=1,
        )
        assert_matches_type(RoutingRuleUpdateResponse, routing_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Tokenrouter) -> None:
        routing_rule = client.routing_rules.update(
            id=1,
            action_json="string",
            is_enabled=True,
            match_json="string",
            name="name",
            priority=-1000,
        )
        assert_matches_type(RoutingRuleUpdateResponse, routing_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Tokenrouter) -> None:
        response = client.routing_rules.with_raw_response.update(
            id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_rule = response.parse()
        assert_matches_type(RoutingRuleUpdateResponse, routing_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Tokenrouter) -> None:
        with client.routing_rules.with_streaming_response.update(
            id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_rule = response.parse()
            assert_matches_type(RoutingRuleUpdateResponse, routing_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Tokenrouter) -> None:
        routing_rule = client.routing_rules.list()
        assert_matches_type(RoutingRuleListResponse, routing_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Tokenrouter) -> None:
        response = client.routing_rules.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_rule = response.parse()
        assert_matches_type(RoutingRuleListResponse, routing_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Tokenrouter) -> None:
        with client.routing_rules.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_rule = response.parse()
            assert_matches_type(RoutingRuleListResponse, routing_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Tokenrouter) -> None:
        routing_rule = client.routing_rules.delete(
            1,
        )
        assert_matches_type(RoutingRuleDeleteResponse, routing_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Tokenrouter) -> None:
        response = client.routing_rules.with_raw_response.delete(
            1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_rule = response.parse()
        assert_matches_type(RoutingRuleDeleteResponse, routing_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Tokenrouter) -> None:
        with client.routing_rules.with_streaming_response.delete(
            1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_rule = response.parse()
            assert_matches_type(RoutingRuleDeleteResponse, routing_rule, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRoutingRules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTokenrouter) -> None:
        routing_rule = await async_client.routing_rules.create(
            action_json="string",
            is_enabled=True,
            match_json="string",
            name="name",
            priority=-1000,
        )
        assert_matches_type(RoutingRuleCreateResponse, routing_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTokenrouter) -> None:
        response = await async_client.routing_rules.with_raw_response.create(
            action_json="string",
            is_enabled=True,
            match_json="string",
            name="name",
            priority=-1000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_rule = await response.parse()
        assert_matches_type(RoutingRuleCreateResponse, routing_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTokenrouter) -> None:
        async with async_client.routing_rules.with_streaming_response.create(
            action_json="string",
            is_enabled=True,
            match_json="string",
            name="name",
            priority=-1000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_rule = await response.parse()
            assert_matches_type(RoutingRuleCreateResponse, routing_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTokenrouter) -> None:
        routing_rule = await async_client.routing_rules.retrieve(
            1,
        )
        assert_matches_type(RoutingRuleRetrieveResponse, routing_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTokenrouter) -> None:
        response = await async_client.routing_rules.with_raw_response.retrieve(
            1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_rule = await response.parse()
        assert_matches_type(RoutingRuleRetrieveResponse, routing_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTokenrouter) -> None:
        async with async_client.routing_rules.with_streaming_response.retrieve(
            1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_rule = await response.parse()
            assert_matches_type(RoutingRuleRetrieveResponse, routing_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTokenrouter) -> None:
        routing_rule = await async_client.routing_rules.update(
            id=1,
        )
        assert_matches_type(RoutingRuleUpdateResponse, routing_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTokenrouter) -> None:
        routing_rule = await async_client.routing_rules.update(
            id=1,
            action_json="string",
            is_enabled=True,
            match_json="string",
            name="name",
            priority=-1000,
        )
        assert_matches_type(RoutingRuleUpdateResponse, routing_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTokenrouter) -> None:
        response = await async_client.routing_rules.with_raw_response.update(
            id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_rule = await response.parse()
        assert_matches_type(RoutingRuleUpdateResponse, routing_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTokenrouter) -> None:
        async with async_client.routing_rules.with_streaming_response.update(
            id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_rule = await response.parse()
            assert_matches_type(RoutingRuleUpdateResponse, routing_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTokenrouter) -> None:
        routing_rule = await async_client.routing_rules.list()
        assert_matches_type(RoutingRuleListResponse, routing_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTokenrouter) -> None:
        response = await async_client.routing_rules.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_rule = await response.parse()
        assert_matches_type(RoutingRuleListResponse, routing_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTokenrouter) -> None:
        async with async_client.routing_rules.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_rule = await response.parse()
            assert_matches_type(RoutingRuleListResponse, routing_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTokenrouter) -> None:
        routing_rule = await async_client.routing_rules.delete(
            1,
        )
        assert_matches_type(RoutingRuleDeleteResponse, routing_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTokenrouter) -> None:
        response = await async_client.routing_rules.with_raw_response.delete(
            1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_rule = await response.parse()
        assert_matches_type(RoutingRuleDeleteResponse, routing_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTokenrouter) -> None:
        async with async_client.routing_rules.with_streaming_response.delete(
            1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_rule = await response.parse()
            assert_matches_type(RoutingRuleDeleteResponse, routing_rule, path=["response"])

        assert cast(Any, response.is_closed) is True
