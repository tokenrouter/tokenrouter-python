# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .firewall_rule import FirewallRule

__all__ = ["FirewallRuleCreateResponse"]


class FirewallRuleCreateResponse(BaseModel):
    data: FirewallRule
