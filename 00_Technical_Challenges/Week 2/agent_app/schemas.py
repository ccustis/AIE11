"""The API contract, in Pydantic. This file is written for you: read it, don't rewrite it.

Why Pydantic and not a plain `@dataclass` (like Week 1's `Hit`)? Because this app has
an HTTP boundary, and FastAPI is built on Pydantic. These models buy you three things a
dataclass does not:

  1. Validation — a request with no question, or `k=999`, is rejected with a clean 422
     before your agent ever runs. A dataclass would sail through and blow up later.
  2. Serialization — FastAPI turns these into JSON (and back) with no manual code.
  3. A schema — `/docs` documents every field for free, from the types below.

`Source` is Week 1's `Hit` grown up: same job (cite a chunk), now a validated model that
crosses the wire. The lesson of the week lives in the gap between the agent's raw list of
messages and this tidy object — closing that gap is `service.answer_question`'s job.
"""

from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    """What a client POSTs to /ask."""

    question: str = Field(..., min_length=1, description="The user's question.")
    k: int = Field(3, ge=1, le=10, description="Max chunks the retriever may return.")


class Source(BaseModel):
    """One retrieved chunk the answer was grounded in — Week 1's `Hit`, across the wire."""

    chunk_id: int = Field(..., description="Which chunk, so the answer is traceable.")
    score: float = Field(..., description="Similarity score for this chunk.")
    preview: str = Field(..., description="First ~160 characters of the chunk text.")


class TraceStep(BaseModel):
    """One step the agent took — a node that fired and what happened there."""

    node: str = Field(..., description='Graph node, e.g. "agent" or "tools".')
    detail: str = Field(..., description="What happened: a tool call, a tool result, or the final answer.")


class AskResponse(BaseModel):
    """What /ask returns. One validated object built from the agent's messages."""

    answer: str = Field(..., description="The agent's final answer.")
    used_retrieval: bool = Field(..., description="Did the agent call the search tool?")
    sources: list[Source] = Field(default_factory=list, description="Chunks the answer cites.")
    trace: list[TraceStep] = Field(default_factory=list, description="The path the agent took.")
