# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ResponseCreateParams",
    "InputUnionMember1",
    "InputUnionMember1ImageURL",
    "Reasoning",
    "StreamOptions",
    "Text",
    "TextJsonSchema",
    "ToolChoice",
    "ToolChoiceUnionMember1",
    "ToolChoiceUnionMember1Function",
    "Tool",
    "ToolFunction",
]


class ResponseCreateParams(TypedDict, total=False):
    input: Required[Union[str, Iterable[InputUnionMember1]]]
    """Text, image, or file inputs to the model.

    Can be a simple string or an array of content items.
    """

    background: bool
    """Run response generation in background"""

    conversation: Union[str, object, None]
    """Conversation ID or object for context"""

    instructions: Optional[str]
    """System-level instructions for the model"""

    max_output_tokens: Optional[int]
    """Maximum number of tokens in the response"""

    max_tool_calls: Optional[int]
    """Maximum number of tool calls"""

    metadata: Optional[Dict[str, str]]
    """Custom metadata (up to 16 key-value pairs)"""

    model: str
    """Model ID or routing mode. Supports:

    - `auto:balance` - Balanced routing (default)
    - `auto:cost` - Cost-optimized routing
    - `auto:quality` - Quality-optimized routing
    - `auto:latency` - Latency-optimized routing
    - Specific model with mode: `gpt-4o:balance`, `claude-3-7-sonnet-latest:quality`
    - Specific model: `gpt-4o`, `claude-3-7-sonnet-latest`, etc.
    """

    parallel_tool_calls: bool
    """Allow parallel tool execution"""

    previous_response_id: Optional[str]
    """ID of previous response for context"""

    prompt_cache_key: Optional[str]
    """Key for prompt caching (OpenAI)"""

    reasoning: Optional[Reasoning]
    """Configuration for reasoning models (o-series, gpt-5)"""

    router_mode: Optional[Literal["balance", "cost", "quality", "latency"]]
    """Override routing mode (advanced)"""

    router_model: Optional[str]
    """Override model for routing (advanced)"""

    router_provider: Optional[Literal["openai", "anthropic", "gemini", "mistral", "deepseek"]]
    """Force specific provider (advanced)"""

    safety_identifier: Optional[str]
    """Stable identifier for policy violation detection"""

    service_tier: Literal["auto", "default", "flex", "priority"]
    """Processing priority tier"""

    store: bool
    """Whether to store the response for later retrieval"""

    stream: bool
    """Whether to stream the response as Server-Sent Events"""

    stream_options: Optional[StreamOptions]
    """Options for streaming responses"""

    temperature: Optional[float]
    """Sampling temperature (0-2). Higher values make output more random."""

    text: Optional[Text]
    """Configuration for structured text output"""

    tool_choice: ToolChoice
    """How the model should select tools"""

    tools: Optional[Iterable[Tool]]
    """Tools/functions the model may call"""

    top_logprobs: Optional[int]
    """Number of top log probabilities to return (0-20)"""

    top_p: Optional[float]
    """Nucleus sampling probability mass cutoff"""

    truncation: Literal["auto", "disabled"]
    """Truncation strategy"""


class InputUnionMember1ImageURL(TypedDict, total=False):
    url: str


class InputUnionMember1(TypedDict, total=False):
    image_url: InputUnionMember1ImageURL

    text: str

    type: Literal["text", "image_url", "image_file"]


class Reasoning(TypedDict, total=False):
    effort: Literal["low", "medium", "high"]


class StreamOptions(TypedDict, total=False):
    include_usage: bool
    """Include usage statistics in stream"""


class TextJsonSchema(TypedDict, total=False):
    name: str

    schema: object

    strict: bool


class Text(TypedDict, total=False):
    json_schema: TextJsonSchema
    """JSON Schema for structured output"""

    type: Literal["text", "json_object", "json_schema"]


class ToolChoiceUnionMember1Function(TypedDict, total=False):
    name: str


class ToolChoiceUnionMember1(TypedDict, total=False):
    function: ToolChoiceUnionMember1Function

    type: Literal["function"]


ToolChoice: TypeAlias = Union[Literal["auto", "none", "required"], ToolChoiceUnionMember1]


class ToolFunction(TypedDict, total=False):
    description: Required[str]
    """Function description"""

    name: Required[str]
    """Function name"""

    parameters: object
    """JSON Schema for function parameters"""


class Tool(TypedDict, total=False):
    function: Required[ToolFunction]

    type: Required[Literal["function"]]
