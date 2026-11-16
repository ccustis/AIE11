"""An agentic-RAG search service. One LangGraph agent, behind a FastAPI endpoint.

Four stages, four files you write, plus the plumbing that is already done.

index.py    →  load, split, embed, and expose a retriever over the corpus   (✏️ you)
tools.py    →  wrap the retriever as a tool the agent may choose to call     (✏️ you)
graph.py    →  the from-scratch agent loop: agent node, router, graph        (✏️ you)
service.py  →  shape the agent's messages into the AskResponse contract      (✏️ you)

schemas.py  →  the Pydantic request/response contract                        (✅ given)
api.py      →  the FastAPI app, routes, and startup wiring                    (✅ given)
__main__.py →  `python -m agent_app` launches the server                      (✅ given)

The whole point: in Session 3 `create_agent` hid the loop; in Session 4 you built it
by hand. This week that hand-built loop goes behind an HTTP boundary, and the messy
list of messages it produces becomes one clean, validated JSON object.
"""
