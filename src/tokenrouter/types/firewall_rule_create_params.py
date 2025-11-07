# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FirewallRuleCreateParams"]


class FirewallRuleCreateParams(TypedDict, total=False):
    action: Required[Literal["block", "mask", "warn"]]

    is_enabled: Required[bool]

    name: Required[str]

    pattern: Required[str]

    priority: Required[int]

    scope: Required[Literal["prompt", "response"]]

    type: Required[Literal["substring", "regex"]]

    replacement: Optional[str]
