# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

__all__ = ["RoutingRuleCreateParams"]


class RoutingRuleCreateParams(TypedDict, total=False):
    action_json: Required[Union[str, object]]
    """Actions to take when matched (JSON object or string)"""

    is_enabled: Required[bool]

    match_json: Required[Union[str, object]]
    """Conditions for matching requests (JSON object or string)"""

    name: Required[str]

    priority: Required[int]
