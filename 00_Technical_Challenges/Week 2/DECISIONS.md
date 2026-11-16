# Decisions

One row, one decision. Week 1 was retrieval; this week is the agent and its boundary. By
Week 5 this file explains the decisions you made across the whole bootcamp.

## Agentic search, week 2

**What I changed**

> One sentence. Your Step 4 augmentation (loop cap, scope router, structured output,
> streaming, memory, reranking, …).

**Why**

> Which of your 10 failures it targeted, and the before/after — not a mood, a measurement.

**What would change my mind**

> The condition under which you would undo it.

---

## Structured I/O: dataclass vs. Pydantic (answer this one too)

**The call:** the API contract in `schemas.py` is Pydantic, not a `@dataclass` like Week 1's `Hit`.

> In one or two lines: what does Pydantic give a FastAPI app that a dataclass does not, and
> where (if anywhere) would a plain dataclass still have been the right tool here?
