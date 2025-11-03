# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ResponseReplayParams"]


class ResponseReplayParams(TypedDict, total=False):
    stream: bool
    """Whether to stream the replayed response"""
