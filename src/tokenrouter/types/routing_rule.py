# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RoutingRule", "ActionJson", "ActionJsonAddWarning", "MatchJson"]


class ActionJsonAddWarning(BaseModel):
    message: Optional[str] = None


class ActionJson(BaseModel):
    add_warning: Optional[ActionJsonAddWarning] = None
    """Add a custom warning to the response"""

    set_mode: Optional[Literal["balance", "cost", "quality", "latency"]] = None
    """Override routing mode"""

    set_model: Optional[str] = None
    """Force a specific model"""

    set_provider: Optional[Literal["openai", "anthropic", "gemini", "mistral", "deepseek"]] = None
    """Force a specific provider"""


class MatchJson(BaseModel):
    contains: Union[str, List[str], None] = None
    """String or array of strings to search for in user input"""

    metadata_equals: Optional[Dict[str, str]] = None
    """Match specific metadata key-value pairs"""

    mode: Optional[Literal["fast", "balanced", "quality"]] = None
    """Match specific routing mode"""

    task: Optional[str] = None
    """Convenience shorthand for metadata_equals.task"""


class RoutingRule(BaseModel):
    id: int
    """Unique identifier for the routing rule"""

    action_json: ActionJson
    """Actions to take when this rule matches"""

    created_at: datetime

    is_enabled: bool
    """Whether the rule is active"""

    match_json: MatchJson
    """Conditions that determine when this rule matches a request"""

    name: str
    """Human-readable name for the rule"""

    priority: int
    """Rule evaluation priority (higher values = higher priority)"""

    updated_at: datetime

    user_id: int
    """ID of the user who owns this rule"""
