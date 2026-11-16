"""Stage 2: wrap the retriever as a tool the agent may choose to call.

YOUR CODE GOES HERE. `make_search_tool` raises NotImplementedError.

This is the line that makes RAG *agentic*: the retriever becomes a tool, and the model
decides whether to use it. You wrote a version of this in Session 4 Task 4, Step 3 — but
there the tool returned a loose string. Here the output format matters, because
`service.answer_question` has to recover `Source` objects from it later.
"""

import os

from langchain_core.retrievers import BaseRetriever
from langchain_core.tools import BaseTool, tool

# The per-source line format the tool must emit, and the service must parse. Keep them in
# sync — this one constant is the contract between the tool and the API response.
SOURCE_LINE = "[source chunk_id={chunk_id} score={score:.3f}]"

# The name your search tool must carry. `answer_question` keys `used_retrieval` and `sources`
# off this exact name, so give the inner @tool function in make_search_tool() this name.
WELLNESS_SEARCH_TOOL_NAME = "search_wellness_knowledge"


def build_web_search_tool() -> BaseTool | None:
    """A second source: live web search via Tavily. WRITTEN FOR YOU — this is not a stub.

    Returns a Tavily search tool when `TAVILY_API_KEY` is set, else `None` (the app then runs
    on the local guide alone). `service.build_agent` adds it to the agent's tool list
    automatically, so the agent gains a second place to look the moment you add a key — no
    graph change needed, because `build_agent_graph` takes a *list* of tools.

    This is the two-source setup from Session 4, Task 5: the guide is a fixed snapshot, the web
    is current. Having both is what makes the Step 4 routing augmentation real — "try the guide
    first, hit the web on a miss," "cap web calls to one per question," "never let a medical
    claim come from an unvetted web result." Those are decisions you own in the graph.

    Note: a Tavily result does NOT match `SOURCE_LINE`, so `answer_question` won't turn it into a
    `Source` — web answers show up in the `trace`, while `sources` stay grounded in the guide.
    """
    if not os.environ.get("TAVILY_API_KEY"):
        return None
    from langchain_tavily import TavilySearch

    return TavilySearch(max_results=3)


def make_search_tool(retriever: BaseRetriever) -> BaseTool:
    """Build the `search_wellness_knowledge` tool, closed over a ready retriever.

    Args:
        retriever: from index.build_retriever().

    Returns:
        A LangChain tool the model can call. Its docstring is the model's only instruction
        for *when* to call it, so write it like one.

    What the tool must do when invoked with a `query`:
      1. `retriever.invoke(query)` -> a list of Documents.
      2. For each, format one block as:
             SOURCE_LINE.format(chunk_id=<from metadata>, score=<similarity>)
             <the chunk text>
         Use the `chunk_id` you stamped into metadata in index.py. (A plain retriever does
         not return scores; if you want a real score, retrieve with
         `vector_store.similarity_search_with_score` instead — a reasonable Step 4 upgrade.
         Until then, a placeholder like 0.0 is honest.)
      3. Join the blocks and return the string. Return a clear "nothing found" string if empty.

    Why the rigid format? The agent only ever returns text. The API needs structured
    `sources`. That format is the seam the service pulls them back out of — see
    `service.answer_question`.

    Hint: define an inner `@tool`-decorated function and `return` it. The decorator turns a
    function into a tool; closing over `retriever` is what lets the tool reach your index.
    """
    raise NotImplementedError("Write make_search_tool() in agent_app/tools.py")
