"""Response types for the model listing/retrieve endpoints (/v1/models, /models)."""

from collections.abc import Mapping
from typing import Literal, TypeAlias

from pydantic import JsonValue
from typing_extensions import NotRequired, TypedDict


ModelInfoMetadata: TypeAlias = Mapping[str, JsonValue]


class ModelInfoResponse(TypedDict):
    """OpenAI-compatible model object. `mode`, `max_input_tokens`, and
    `max_output_tokens` are attached when the cost map or deployment config
    knows them; `metadata` is present only with include_metadata=true.
    """

    id: str
    object: Literal["model"]
    created: int
    owned_by: str
    mode: NotRequired[str]
    max_input_tokens: NotRequired[int]
    max_output_tokens: NotRequired[int]
    metadata: NotRequired[ModelInfoMetadata]
