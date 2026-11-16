"""Stage 3: the agent loop, built from scratch with LangGraph.

YOUR CODE GOES HERE. `should_continue` and `build_agent_graph` raise NotImplementedError.

This is the Session 4 notebook, Task 2 and Task 5 — the ReAct loop as an explicit graph.
`AgentState`, the system prompt, and the model name are given. The two things you write are
the router (the one real decision in any agent) and the graph that wires it together.
"""

from typing import Annotated, Literal, TypedDict

from langchain_core.messages import BaseMessage
from langchain_core.runnables import Runnable
from langchain_core.tools import BaseTool
from langgraph.graph.message import add_messages

from .index import CHAT_MODEL

SYSTEM_PROMPT = (
    "You are a supportive wellness assistant with a health & wellness knowledge base.\n"
    "- For questions about health, fitness, nutrition, sleep, or stress, ALWAYS call the "
    "search_wellness_knowledge tool first and answer from what it returns.\n"
    "- If the knowledge base doesn't cover it, say so honestly rather than guessing. For current "
    "information it can't contain (recent research, today's conditions), use the web search tool "
    "if one is available.\n"
    "- For anything else, just answer directly.\n"
    "- Be encouraging, and remind users to consult a professional for medical concerns."
)


class AgentState(TypedDict):
    """The agent's whole memory: a list of messages, appended to as it loops."""

    messages: Annotated[list[BaseMessage], add_messages]


def should_continue(state: AgentState) -> Literal["tools", "end"]:
    """Route to the tools node if the model requested a tool; otherwise finish.

    Returns:
        "tools" if the last message has tool calls, "end" otherwise.

    This function is the decision `create_agent` made for you in Session 3. Look at the last
    message in `state["messages"]` and check its `.tool_calls`.
    """
    raise NotImplementedError("Write should_continue() in agent_app/graph.py")


def build_agent_graph(tools: list[BaseTool]) -> Runnable:
    """Wire the ReAct loop and compile it.

    Args:
        tools: the tools the agent may call. `service.build_agent` passes the wellness search
            tool from tools.make_search_tool(), plus the optional web search tool when a
            `TAVILY_API_KEY` is set. You don't special-case them — bind and route the whole list.

    Returns:
        A compiled LangGraph you can `.invoke({"messages": [...]})`.

    The recipe, straight from Session 4 Task 2 (steps 1-4) — note it binds a *list* of tools,
    exactly like the notebook's `rag_tools`:
      1. Build the model and bind the tools:
             llm = ChatOpenAI(model=CHAT_MODEL, temperature=0)
             llm_with_tools = llm.bind_tools(tools)
      2. Define the agent node — a function that prepends SystemMessage(SYSTEM_PROMPT) to
         state["messages"], calls llm_with_tools, and returns {"messages": [response]}.
      3. Make the tools node with `ToolNode(tools)`.
      4. Build a StateGraph(AgentState): add "agent" and "tools" nodes, edge START->agent,
         a conditional edge from "agent" using should_continue ({"tools": "tools", "end": END}),
         and an edge "tools"->"agent" (the loop). `.compile()` and return it.

    Hint: define the agent node as a closure *inside* this function so it can see
    `llm_with_tools`. That mirrors the notebook, where the node read a module-level binding.

    Guardrail worth knowing: a compiled graph takes a `recursion_limit` at invoke time, so a
    confused loop stops instead of running forever. Bounding it cleanly is a Step 4 option.
    """
    raise NotImplementedError("Write build_agent_graph() in agent_app/graph.py")
