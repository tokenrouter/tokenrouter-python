# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["FirewallRuleUpdateParams"]


class FirewallRuleUpdateParams(TypedDict, total=False):
    action: Literal["block", "mask", "warn"]

    is_enabled: bool

    name: str

    pattern: str

    priority: int

    replacement: Optional[str]

    scope: Literal["prompt", "response"]

    type: Literal["substring", "regex"]
