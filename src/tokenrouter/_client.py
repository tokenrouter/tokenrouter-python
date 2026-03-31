# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, TokenrouterError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import responses, routing_rules, firewall_rules
    from .resources.responses import ResponsesResource, AsyncResponsesResource
    from .resources.routing_rules import RoutingRulesResource, AsyncRoutingRulesResource
    from .resources.firewall_rules import FirewallRulesResource, AsyncFirewallRulesResource

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Tokenrouter",
    "AsyncTokenrouter",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.tokenrouter.io",
    "local": "https://api.tokenrouter.test",
}


class Tokenrouter(SyncAPIClient):
    # client options
    api_key: str

    _environment: Literal["production", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "local"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Tokenrouter client instance.

        This automatically infers the `api_key` argument from the `TOKENROUTER_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("TOKENROUTER_API_KEY")
        if api_key is None:
            raise TokenrouterError(
                "The api_key client option must be set either by passing api_key to the client or by setting the TOKENROUTER_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("TOKENROUTER_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `TOKENROUTER_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def responses(self) -> ResponsesResource:
        """Core endpoint for creating AI model responses with intelligent routing.

        The Responses API automatically routes your requests to the optimal AI provider
        based on your preferences, available models, and configured routing rules.
        """
        from .resources.responses import ResponsesResource

        return ResponsesResource(self)

    @cached_property
    def routing_rules(self) -> RoutingRulesResource:
        """
        Manage custom routing rules to control how TokenRouter selects AI providers and models.

        Routing rules enable fine-grained control over request routing based on content, metadata,
        or other conditions. Rules are evaluated in priority order and can force specific providers,
        models, or routing modes.
        """
        from .resources.routing_rules import RoutingRulesResource

        return RoutingRulesResource(self)

    @cached_property
    def firewall_rules(self) -> FirewallRulesResource:
        """Manage firewall rules for content filtering, security, and compliance.

        Firewall rules provide content security controls through pattern matching. Rules can detect
        and handle sensitive information, enforce policies, or implement custom content moderation.
        """
        from .resources.firewall_rules import FirewallRulesResource

        return FirewallRulesResource(self)

    @cached_property
    def with_raw_response(self) -> TokenrouterWithRawResponse:
        return TokenrouterWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TokenrouterWithStreamedResponse:
        return TokenrouterWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncTokenrouter(AsyncAPIClient):
    # client options
    api_key: str

    _environment: Literal["production", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "local"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncTokenrouter client instance.

        This automatically infers the `api_key` argument from the `TOKENROUTER_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("TOKENROUTER_API_KEY")
        if api_key is None:
            raise TokenrouterError(
                "The api_key client option must be set either by passing api_key to the client or by setting the TOKENROUTER_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("TOKENROUTER_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `TOKENROUTER_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def responses(self) -> AsyncResponsesResource:
        """Core endpoint for creating AI model responses with intelligent routing.

        The Responses API automatically routes your requests to the optimal AI provider
        based on your preferences, available models, and configured routing rules.
        """
        from .resources.responses import AsyncResponsesResource

        return AsyncResponsesResource(self)

    @cached_property
    def routing_rules(self) -> AsyncRoutingRulesResource:
        """
        Manage custom routing rules to control how TokenRouter selects AI providers and models.

        Routing rules enable fine-grained control over request routing based on content, metadata,
        or other conditions. Rules are evaluated in priority order and can force specific providers,
        models, or routing modes.
        """
        from .resources.routing_rules import AsyncRoutingRulesResource

        return AsyncRoutingRulesResource(self)

    @cached_property
    def firewall_rules(self) -> AsyncFirewallRulesResource:
        """Manage firewall rules for content filtering, security, and compliance.

        Firewall rules provide content security controls through pattern matching. Rules can detect
        and handle sensitive information, enforce policies, or implement custom content moderation.
        """
        from .resources.firewall_rules import AsyncFirewallRulesResource

        return AsyncFirewallRulesResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncTokenrouterWithRawResponse:
        return AsyncTokenrouterWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTokenrouterWithStreamedResponse:
        return AsyncTokenrouterWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class TokenrouterWithRawResponse:
    _client: Tokenrouter

    def __init__(self, client: Tokenrouter) -> None:
        self._client = client

    @cached_property
    def responses(self) -> responses.ResponsesResourceWithRawResponse:
        """Core endpoint for creating AI model responses with intelligent routing.

        The Responses API automatically routes your requests to the optimal AI provider
        based on your preferences, available models, and configured routing rules.
        """
        from .resources.responses import ResponsesResourceWithRawResponse

        return ResponsesResourceWithRawResponse(self._client.responses)

    @cached_property
    def routing_rules(self) -> routing_rules.RoutingRulesResourceWithRawResponse:
        """
        Manage custom routing rules to control how TokenRouter selects AI providers and models.

        Routing rules enable fine-grained control over request routing based on content, metadata,
        or other conditions. Rules are evaluated in priority order and can force specific providers,
        models, or routing modes.
        """
        from .resources.routing_rules import RoutingRulesResourceWithRawResponse

        return RoutingRulesResourceWithRawResponse(self._client.routing_rules)

    @cached_property
    def firewall_rules(self) -> firewall_rules.FirewallRulesResourceWithRawResponse:
        """Manage firewall rules for content filtering, security, and compliance.

        Firewall rules provide content security controls through pattern matching. Rules can detect
        and handle sensitive information, enforce policies, or implement custom content moderation.
        """
        from .resources.firewall_rules import FirewallRulesResourceWithRawResponse

        return FirewallRulesResourceWithRawResponse(self._client.firewall_rules)


class AsyncTokenrouterWithRawResponse:
    _client: AsyncTokenrouter

    def __init__(self, client: AsyncTokenrouter) -> None:
        self._client = client

    @cached_property
    def responses(self) -> responses.AsyncResponsesResourceWithRawResponse:
        """Core endpoint for creating AI model responses with intelligent routing.

        The Responses API automatically routes your requests to the optimal AI provider
        based on your preferences, available models, and configured routing rules.
        """
        from .resources.responses import AsyncResponsesResourceWithRawResponse

        return AsyncResponsesResourceWithRawResponse(self._client.responses)

    @cached_property
    def routing_rules(self) -> routing_rules.AsyncRoutingRulesResourceWithRawResponse:
        """
        Manage custom routing rules to control how TokenRouter selects AI providers and models.

        Routing rules enable fine-grained control over request routing based on content, metadata,
        or other conditions. Rules are evaluated in priority order and can force specific providers,
        models, or routing modes.
        """
        from .resources.routing_rules import AsyncRoutingRulesResourceWithRawResponse

        return AsyncRoutingRulesResourceWithRawResponse(self._client.routing_rules)

    @cached_property
    def firewall_rules(self) -> firewall_rules.AsyncFirewallRulesResourceWithRawResponse:
        """Manage firewall rules for content filtering, security, and compliance.

        Firewall rules provide content security controls through pattern matching. Rules can detect
        and handle sensitive information, enforce policies, or implement custom content moderation.
        """
        from .resources.firewall_rules import AsyncFirewallRulesResourceWithRawResponse

        return AsyncFirewallRulesResourceWithRawResponse(self._client.firewall_rules)


class TokenrouterWithStreamedResponse:
    _client: Tokenrouter

    def __init__(self, client: Tokenrouter) -> None:
        self._client = client

    @cached_property
    def responses(self) -> responses.ResponsesResourceWithStreamingResponse:
        """Core endpoint for creating AI model responses with intelligent routing.

        The Responses API automatically routes your requests to the optimal AI provider
        based on your preferences, available models, and configured routing rules.
        """
        from .resources.responses import ResponsesResourceWithStreamingResponse

        return ResponsesResourceWithStreamingResponse(self._client.responses)

    @cached_property
    def routing_rules(self) -> routing_rules.RoutingRulesResourceWithStreamingResponse:
        """
        Manage custom routing rules to control how TokenRouter selects AI providers and models.

        Routing rules enable fine-grained control over request routing based on content, metadata,
        or other conditions. Rules are evaluated in priority order and can force specific providers,
        models, or routing modes.
        """
        from .resources.routing_rules import RoutingRulesResourceWithStreamingResponse

        return RoutingRulesResourceWithStreamingResponse(self._client.routing_rules)

    @cached_property
    def firewall_rules(self) -> firewall_rules.FirewallRulesResourceWithStreamingResponse:
        """Manage firewall rules for content filtering, security, and compliance.

        Firewall rules provide content security controls through pattern matching. Rules can detect
        and handle sensitive information, enforce policies, or implement custom content moderation.
        """
        from .resources.firewall_rules import FirewallRulesResourceWithStreamingResponse

        return FirewallRulesResourceWithStreamingResponse(self._client.firewall_rules)


class AsyncTokenrouterWithStreamedResponse:
    _client: AsyncTokenrouter

    def __init__(self, client: AsyncTokenrouter) -> None:
        self._client = client

    @cached_property
    def responses(self) -> responses.AsyncResponsesResourceWithStreamingResponse:
        """Core endpoint for creating AI model responses with intelligent routing.

        The Responses API automatically routes your requests to the optimal AI provider
        based on your preferences, available models, and configured routing rules.
        """
        from .resources.responses import AsyncResponsesResourceWithStreamingResponse

        return AsyncResponsesResourceWithStreamingResponse(self._client.responses)

    @cached_property
    def routing_rules(self) -> routing_rules.AsyncRoutingRulesResourceWithStreamingResponse:
        """
        Manage custom routing rules to control how TokenRouter selects AI providers and models.

        Routing rules enable fine-grained control over request routing based on content, metadata,
        or other conditions. Rules are evaluated in priority order and can force specific providers,
        models, or routing modes.
        """
        from .resources.routing_rules import AsyncRoutingRulesResourceWithStreamingResponse

        return AsyncRoutingRulesResourceWithStreamingResponse(self._client.routing_rules)

    @cached_property
    def firewall_rules(self) -> firewall_rules.AsyncFirewallRulesResourceWithStreamingResponse:
        """Manage firewall rules for content filtering, security, and compliance.

        Firewall rules provide content security controls through pattern matching. Rules can detect
        and handle sensitive information, enforce policies, or implement custom content moderation.
        """
        from .resources.firewall_rules import AsyncFirewallRulesResourceWithStreamingResponse

        return AsyncFirewallRulesResourceWithStreamingResponse(self._client.firewall_rules)


Client = Tokenrouter

AsyncClient = AsyncTokenrouter
