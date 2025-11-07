# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .routing_rule import RoutingRule

__all__ = ["RoutingRuleListResponse"]


class RoutingRuleListResponse(BaseModel):
    data: List[RoutingRule]
