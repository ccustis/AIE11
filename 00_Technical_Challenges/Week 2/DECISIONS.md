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



# Technical Challenge 2 — Engineering Decisions

## 1. What I changed

I augmented the agent's wellness retrieval tool to support

multiple focused subqueries. The tool retrieves evidence

separately for distinct information needs, combines the

results, and deduplicates source chunks within each call.

## 2. Why I made this change

Baseline Test 7 revealed a retrieval-coverage failure.

When asked about hydration and sleep together, the agent

retrieved the hydration recommendation but missed the

guide's 7–9-hour sleep recommendation.

The isolated sleep question succeeded, suggesting that

the combined retrieval query was insufficient.

After augmentation, Test 7 succeeded. The agent selected

focused hydration and sleep queries and retrieved evidence

supporting both recommendations.

Across the 10-test evaluation:

- Baseline: 8 passed, 1 failed, 1 ambiguous.

- Augmented: 9 passed, 0 failed, 1 ambiguous.

## 3. Tradeoffs and limitations

Multi-query retrieval improved coverage for compound

questions but increased retrieval activity.

Some single-topic questions triggered multiple searches

without improving the answer. Test 4 also demonstrated

redundant tool calls with overlapping results.

Citation precision remains imperfect: the API can return

retrieved passages that do not directly support every

claim in the final answer.

The experiment establishes a targeted improvement, not

a general guarantee of better retrieval performance.

## 4. What would change my mind

I would reconsider this approach if additional searches

significantly increased latency or cost without consistent

improvements in answer quality.

A future version could selectively invoke multi-query

retrieval only when a question contains distinct

information needs, and apply relevance filtering to

reduce unsupported or unnecessary citations.

## 5. Why Pydantic instead of dataclasses?

Pydantic provides runtime validation, JSON serialization,

and machine-readable schemas for FastAPI's HTTP interface.

Dataclasses provide useful Python structures but do not

offer these API-oriented capabilities natively.

Pydantic therefore makes the request and response

contracts more explicit and enforceable.
