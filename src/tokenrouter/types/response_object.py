# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ResponseObject",
    "Error",
    "Metadata",
    "Output",
    "OutputContent",
    "OutputContentUnionMember0",
    "OutputContentUnionMember1",
    "OutputContentUnionMember1Function",
    "Usage",
]


class Error(BaseModel):
    code: Optional[str] = None

    message: Optional[str] = None

    type: Optional[str] = None


class Metadata(BaseModel):
    provider: Optional[str] = None
    """Provider used for this request"""

    request_id: Optional[str] = None
    """Internal request ID"""

    routing_confidence: Optional[float] = None
    """Confidence score of routing decision"""

    routing_mode: Optional[str] = None
    """Routing mode applied"""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class OutputContentUnionMember0(BaseModel):
    text: Optional[str] = None

    type: Optional[Literal["text"]] = None


class OutputContentUnionMember1Function(BaseModel):
    arguments: Optional[str] = None

    name: Optional[str] = None


class OutputContentUnionMember1(BaseModel):
    id: Optional[str] = None

    function: Optional[OutputContentUnionMember1Function] = None

    type: Optional[Literal["tool_call"]] = None


OutputContent: TypeAlias = Union[OutputContentUnionMember0, OutputContentUnionMember1]


class Output(BaseModel):
    content: Optional[List[OutputContent]] = None

    role: Optional[Literal["assistant"]] = None


class Usage(BaseModel):
    input_tokens: Optional[int] = None
    """Number of input tokens"""

    output_tokens: Optional[int] = None
    """Number of output tokens"""

    total_tokens: Optional[int] = None
    """Total tokens used"""


class ResponseObject(BaseModel):
    id: str
    """Unique response identifier"""

    created_at: int
    """Unix timestamp of response creation"""

    model: str
    """Actual model used to generate response"""

    object: Literal["response"]
    """Object type"""

    status: Literal["completed", "failed", "in_progress", "incomplete"]
    """Response status"""

    error: Optional[Error] = None
    """Error information (if status is 'failed')"""

    incomplete_details: Optional[builtins.object] = None
    """Details about incomplete response"""

    instructions: Optional[str] = None
    """System instructions used"""

    max_output_tokens: Optional[int] = None
    """Maximum output tokens setting"""

    metadata: Optional[Metadata] = None
    """Custom metadata attached to response"""

    output: Optional[List[Output]] = None
    """Model output messages"""

    temperature: Optional[float] = None
    """Temperature setting used"""

    top_p: Optional[float] = None
    """Top-p setting used"""

    usage: Optional[Usage] = None
    """Token usage statistics"""
