# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .firewall_rule import FirewallRule

__all__ = ["FirewallRuleListResponse"]


class FirewallRuleListResponse(BaseModel):
    data: List[FirewallRule]
