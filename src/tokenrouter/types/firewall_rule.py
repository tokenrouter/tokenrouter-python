# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FirewallRule"]


class FirewallRule(BaseModel):
    id: int
    """Unique identifier for the firewall rule"""

    action: Literal["block", "mask", "warn"]
    """Action to take when matched"""

    created_at: datetime

    is_enabled: bool
    """Whether the rule is active"""

    name: str
    """Human-readable name for the rule"""

    pattern: str
    """The pattern to match"""

    priority: int
    """Rule evaluation priority (higher values = higher priority)"""

    scope: Literal["prompt", "response"]
    """Where the rule applies (prompt or response)"""

    type: Literal["substring", "regex"]
    """Pattern matching type"""

    updated_at: datetime

    user_id: int
    """ID of the user who owns this rule"""

    replacement: Optional[str] = None
    """Replacement text for mask action"""
