# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tokenrouter import Tokenrouter, AsyncTokenrouter
from tokenrouter.types import (
    FirewallRuleListResponse,
    FirewallRuleCreateResponse,
    FirewallRuleDeleteResponse,
    FirewallRuleUpdateResponse,
    FirewallRuleRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFirewallRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Tokenrouter) -> None:
        firewall_rule = client.firewall_rules.create(
            action="block",
            is_enabled=True,
            name="name",
            pattern="pattern",
            priority=-1000,
            scope="prompt",
            type="substring",
        )
        assert_matches_type(FirewallRuleCreateResponse, firewall_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Tokenrouter) -> None:
        firewall_rule = client.firewall_rules.create(
            action="block",
            is_enabled=True,
            name="name",
            pattern="pattern",
            priority=-1000,
            scope="prompt",
            type="substring",
            replacement="replacement",
        )
        assert_matches_type(FirewallRuleCreateResponse, firewall_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Tokenrouter) -> None:
        response = client.firewall_rules.with_raw_response.create(
            action="block",
            is_enabled=True,
            name="name",
            pattern="pattern",
            priority=-1000,
            scope="prompt",
            type="substring",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall_rule = response.parse()
        assert_matches_type(FirewallRuleCreateResponse, firewall_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Tokenrouter) -> None:
        with client.firewall_rules.with_streaming_response.create(
            action="block",
            is_enabled=True,
            name="name",
            pattern="pattern",
            priority=-1000,
            scope="prompt",
            type="substring",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall_rule = response.parse()
            assert_matches_type(FirewallRuleCreateResponse, firewall_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Tokenrouter) -> None:
        firewall_rule = client.firewall_rules.retrieve(
            1,
        )
        assert_matches_type(FirewallRuleRetrieveResponse, firewall_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Tokenrouter) -> None:
        response = client.firewall_rules.with_raw_response.retrieve(
            1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall_rule = response.parse()
        assert_matches_type(FirewallRuleRetrieveResponse, firewall_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Tokenrouter) -> None:
        with client.firewall_rules.with_streaming_response.retrieve(
            1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall_rule = response.parse()
            assert_matches_type(FirewallRuleRetrieveResponse, firewall_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Tokenrouter) -> None:
        firewall_rule = client.firewall_rules.update(
            id=1,
        )
        assert_matches_type(FirewallRuleUpdateResponse, firewall_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Tokenrouter) -> None:
        firewall_rule = client.firewall_rules.update(
            id=1,
            action="block",
            is_enabled=True,
            name="name",
            pattern="pattern",
            priority=-1000,
            replacement="replacement",
            scope="prompt",
            type="substring",
        )
        assert_matches_type(FirewallRuleUpdateResponse, firewall_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Tokenrouter) -> None:
        response = client.firewall_rules.with_raw_response.update(
            id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall_rule = response.parse()
        assert_matches_type(FirewallRuleUpdateResponse, firewall_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Tokenrouter) -> None:
        with client.firewall_rules.with_streaming_response.update(
            id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall_rule = response.parse()
            assert_matches_type(FirewallRuleUpdateResponse, firewall_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Tokenrouter) -> None:
        firewall_rule = client.firewall_rules.list()
        assert_matches_type(FirewallRuleListResponse, firewall_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Tokenrouter) -> None:
        response = client.firewall_rules.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall_rule = response.parse()
        assert_matches_type(FirewallRuleListResponse, firewall_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Tokenrouter) -> None:
        with client.firewall_rules.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall_rule = response.parse()
            assert_matches_type(FirewallRuleListResponse, firewall_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Tokenrouter) -> None:
        firewall_rule = client.firewall_rules.delete(
            1,
        )
        assert_matches_type(FirewallRuleDeleteResponse, firewall_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Tokenrouter) -> None:
        response = client.firewall_rules.with_raw_response.delete(
            1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall_rule = response.parse()
        assert_matches_type(FirewallRuleDeleteResponse, firewall_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Tokenrouter) -> None:
        with client.firewall_rules.with_streaming_response.delete(
            1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall_rule = response.parse()
            assert_matches_type(FirewallRuleDeleteResponse, firewall_rule, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFirewallRules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTokenrouter) -> None:
        firewall_rule = await async_client.firewall_rules.create(
            action="block",
            is_enabled=True,
            name="name",
            pattern="pattern",
            priority=-1000,
            scope="prompt",
            type="substring",
        )
        assert_matches_type(FirewallRuleCreateResponse, firewall_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTokenrouter) -> None:
        firewall_rule = await async_client.firewall_rules.create(
            action="block",
            is_enabled=True,
            name="name",
            pattern="pattern",
            priority=-1000,
            scope="prompt",
            type="substring",
            replacement="replacement",
        )
        assert_matches_type(FirewallRuleCreateResponse, firewall_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTokenrouter) -> None:
        response = await async_client.firewall_rules.with_raw_response.create(
            action="block",
            is_enabled=True,
            name="name",
            pattern="pattern",
            priority=-1000,
            scope="prompt",
            type="substring",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall_rule = await response.parse()
        assert_matches_type(FirewallRuleCreateResponse, firewall_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTokenrouter) -> None:
        async with async_client.firewall_rules.with_streaming_response.create(
            action="block",
            is_enabled=True,
            name="name",
            pattern="pattern",
            priority=-1000,
            scope="prompt",
            type="substring",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall_rule = await response.parse()
            assert_matches_type(FirewallRuleCreateResponse, firewall_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTokenrouter) -> None:
        firewall_rule = await async_client.firewall_rules.retrieve(
            1,
        )
        assert_matches_type(FirewallRuleRetrieveResponse, firewall_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTokenrouter) -> None:
        response = await async_client.firewall_rules.with_raw_response.retrieve(
            1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall_rule = await response.parse()
        assert_matches_type(FirewallRuleRetrieveResponse, firewall_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTokenrouter) -> None:
        async with async_client.firewall_rules.with_streaming_response.retrieve(
            1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall_rule = await response.parse()
            assert_matches_type(FirewallRuleRetrieveResponse, firewall_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTokenrouter) -> None:
        firewall_rule = await async_client.firewall_rules.update(
            id=1,
        )
        assert_matches_type(FirewallRuleUpdateResponse, firewall_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTokenrouter) -> None:
        firewall_rule = await async_client.firewall_rules.update(
            id=1,
            action="block",
            is_enabled=True,
            name="name",
            pattern="pattern",
            priority=-1000,
            replacement="replacement",
            scope="prompt",
            type="substring",
        )
        assert_matches_type(FirewallRuleUpdateResponse, firewall_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTokenrouter) -> None:
        response = await async_client.firewall_rules.with_raw_response.update(
            id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall_rule = await response.parse()
        assert_matches_type(FirewallRuleUpdateResponse, firewall_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTokenrouter) -> None:
        async with async_client.firewall_rules.with_streaming_response.update(
            id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall_rule = await response.parse()
            assert_matches_type(FirewallRuleUpdateResponse, firewall_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTokenrouter) -> None:
        firewall_rule = await async_client.firewall_rules.list()
        assert_matches_type(FirewallRuleListResponse, firewall_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTokenrouter) -> None:
        response = await async_client.firewall_rules.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall_rule = await response.parse()
        assert_matches_type(FirewallRuleListResponse, firewall_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTokenrouter) -> None:
        async with async_client.firewall_rules.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall_rule = await response.parse()
            assert_matches_type(FirewallRuleListResponse, firewall_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTokenrouter) -> None:
        firewall_rule = await async_client.firewall_rules.delete(
            1,
        )
        assert_matches_type(FirewallRuleDeleteResponse, firewall_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTokenrouter) -> None:
        response = await async_client.firewall_rules.with_raw_response.delete(
            1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall_rule = await response.parse()
        assert_matches_type(FirewallRuleDeleteResponse, firewall_rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTokenrouter) -> None:
        async with async_client.firewall_rules.with_streaming_response.delete(
            1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall_rule = await response.parse()
            assert_matches_type(FirewallRuleDeleteResponse, firewall_rule, path=["response"])

        assert cast(Any, response.is_closed) is True
