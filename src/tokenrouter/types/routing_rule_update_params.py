# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict

__all__ = ["RoutingRuleUpdateParams"]


class RoutingRuleUpdateParams(TypedDict, total=False):
    action_json: Union[str, object]

    is_enabled: bool

    match_json: Union[str, object]

    name: str

    priority: int
