# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .routing_rule import RoutingRule

__all__ = ["RoutingRuleUpdateResponse"]


class RoutingRuleUpdateResponse(BaseModel):
    data: RoutingRule
