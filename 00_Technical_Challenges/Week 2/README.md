<div align="center">
  <img
    src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719"
    width="200"
    alt="AI Makerspace logo"
  />
  <h1>Technical Challenge 2</h1>
  <p><strong>Your agent, out of the notebook and behind an API: an agentic-RAG search service with a FastAPI backend and a frontend you build.</strong></p>
</div>

---

## Overview

> **Read first:** [`03_The_Agent_Harness/README.md`](../../03_The_Agent_Harness/README.md) and [`04_Agentic_Search/README.md`](../../04_Agentic_Search/README.md) for setup, and work through `Agentic_RAG_From_Scratch.ipynb` before you start here.

In Week 1, retrieval always ran before every answer, from your terminal. In Sessions 3–4 you made retrieval a **tool** the agent *chooses* to call, and then you built that agent loop by hand with LangGraph. **This week it becomes a service** — the same hand-built loop, now behind an HTTP boundary, returning one clean, validated JSON object instead of a sprawl of messages.

The skeleton is provided (the FastAPI app, the startup wiring, the `python -m agent_app` command, and the **Pydantic contract** in `schemas.py`). What's missing are the four stages of the pipeline: five functions with contracts and `NotImplementedError` in the body. You fill those in. The question isn't *"did it answer?"* but:

> **"Which of your questions makes the agent do the wrong thing — retrieve when it shouldn't, skip retrieval when it should, loop, or lose its citations — and which stage owns it?"**

> ⚠️ **This is not production-ready, and you're not being asked to make it one.** Qdrant runs embedded (on-disk, single-process) rather than as a clustered server; there is no auth, rate limiting, eval, or deployment, on purpose. This week buys the thing that makes the real versions make sense: an agent whose decisions you can see across a wire, and the habit of naming which stage to blame.

<table>
  <tr>
    <td width="120"><strong>Outcome</strong></td>
    <td>A FastAPI service you wrote that answers questions about a body of text — deciding for itself when to search — returns typed JSON with its sources and trace, and a frontend you built on top of it.</td>
  </tr>
  <tr>
    <td><strong>Tools</strong></td>
    <td>LangGraph, LangChain, Qdrant, the OpenAI API, FastAPI, Pydantic, <code>uv</code>. The Session 3/4 notebooks are the reference you reimplement.</td>
  </tr>
  <tr>
    <td><strong>Due</strong></td>
    <td>End of the week. Post your repo link and Loom in the Maven Community.</td>
  </tr>
  <tr>
    <td><strong>Before you start</strong></td>
    <td>Your AIE11 repo synced, <code>uv</code> installed, an OpenAI key with a little credit, and the Session 4 notebook run at least once.</td>
  </tr>
</table>

---

<!-- deliverables:start -->
## 🏗️ Build | 🚢 Ship | 📤 Share

**Build** is you can run it. **Ship** is someone else can run it and you see your errors. **Share** is someone who isn't you has an opinion about it.

### 🏗️ Build

`uv run python -m agent_app` starts a server; `POST /ask` answers a question with the agentic-RAG graph and returns a typed `AskResponse` — the answer, whether it retrieved, its sources, and its trace. Four questions are asked inside the Session 3/4 notebooks as you work — *not graded*, just comprehension checks:

| # | Question | Asked in |
| :---: | --- | --- |
| 1 | What `create_agent` does in place of your `should_continue` function | S3 / S4 |
| 2 | Where middleware's job lives once you build the loop as a graph | S3 / S4 |
| 3 | What you gain and give up building from scratch vs. `create_agent` | S4 |
| 4 | What could make the loop run forever, and where you'd bound it | S4 |

### 🚢 Ship — the graded stuff, all from the steps below

- [ ] **All five stubs filled in**, so `POST /ask` returns an `AskResponse` rather than a 501
- [ ] **Every answer's `sources` are real** — populated from the chunks the agent actually retrieved
- [ ] **A frontend you built** (not the shipped starter page) that calls `/ask` and shows the answer + sources
- [ ] **One augmentation**, with the same 10 questions re-run and before/after recorded
- [ ] **A diagram** of your graph and service. Hand drawn and photographed is fine, [mermaid](https://mermaid.ai) is better
- [ ] **`DECISIONS.md`**: your augmentation, plus the dataclass-vs-Pydantic call
- [ ] It runs **from a clean terminal**, not just your kernel

### 📤 Share

- [ ] **A Loom (≤ 5 min)**: your frontend answering two questions, your `/docs` page, and your before/after
- [ ] **One real person asked three questions of it**, and what they said, in their words
- [ ] Your repo link posted in [our community on Maven](https://bit.ly/fde1-maven-community)
- [ ] A social post tagging **@AIMakerspace** with three lessons learned
<!-- deliverables:end -->

---

## Official documentation

Prefer these to blog posts and your agent's memory of them.

| Tool | What you use it for here | Docs |
| --- | --- | --- |
| LangGraph | the `StateGraph`, nodes, conditional edge, and `ToolNode` that are the loop | [docs.langchain.com — langgraph](https://docs.langchain.com/oss/python/langgraph/graph-api) |
| LangChain tools | `@tool`, and binding tools to a model | [docs.langchain.com — tools](https://docs.langchain.com/oss/python/langchain/tools) |
| FastAPI | the app, routes, and how it reads your Pydantic models | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/) |
| Pydantic | the request/response contract and validation | [docs.pydantic.dev](https://docs.pydantic.dev/latest/) |
| Qdrant + `langchain-qdrant` | the vector store behind the retriever | [qdrant.tech/documentation](https://qdrant.tech/documentation/) |
| OpenAI | embeddings + the chat model | [platform.openai.com](https://platform.openai.com/docs/guides/embeddings) |
| Tavily (optional) | the wired-in web_search tool — the second source | [tavily.com](https://tavily.com) |
| uv | `uv sync`, `uv add`, `uv run` | [docs.astral.sh/uv](https://docs.astral.sh/uv/) |

---

## Setting expectations

**Budget five to seven hours** across the week. The functions are short; the time goes into understanding the agent loop well enough to shape its messy output into one clean object, and into a frontend you're willing to show.

| Step | What it is | Rough time |
| :---: | --- | --- |
| 1 | Run the Session 3/4 notebooks, then read them | 1–1.5 hrs |
| 2 | Fill in the five stubs, get `/ask` working | 1.5–2.5 hrs |
| 3 | Write 10 questions, find the failures | 45 min |
| 4 | Make one change, measure it | 1–2 hrs |
| 5 | Build your frontend, diagram, decision | 1.5–2 hrs |
| 6 | Show it to one person, and share | 30 min + their calendar |

> **Do Step 3 before Step 4.** Questions you wrote yourself turn Step 4 from "I added a feature" into "I fixed a failure I can point at." The other way round, you can't defend the augmentation.

---

## What you are building

Everything's in this folder. **✏️ is yours to write; ✅ is already done.**

```
00_Technical_Challenges/Week 2/
├── pyproject.toml          ✅ deps: langgraph, langchain, qdrant, fastapi, pydantic, …
├── .env.example            ✅ cp to .env, add your key
├── data/
│   └── HealthWellnessGuide.txt   ✅ the corpus that ships. 16,206 characters.
├── agent_app/
│   ├── __main__.py         ✅ `python -m agent_app` -> starts uvicorn
│   ├── api.py              ✅ the FastAPI app, routes, and startup wiring
│   ├── schemas.py          ✅ the Pydantic contract (AskRequest, Source, TraceStep, AskResponse)
│   ├── index.py            ✏️ build_retriever
│   ├── tools.py            ✏️ make_search_tool   (✅ build_web_search_tool is written for you)
│   ├── graph.py            ✏️ should_continue, build_agent_graph
│   └── service.py          ✏️ answer_question   (build_agent is written for you)
├── frontend/
│   └── index.html          ✅ a starter page — ✏️ you replace it with your own UI
├── qdrant_storage/         ⚙️ created on first run — on-disk vectors, gitignored
├── DECISIONS.md            ✏️ your augmentation + the dataclass-vs-Pydantic call
└── diagram.png             ✏️ your graph + service, drawn by you
```

Each stub has a docstring with arguments, return type, and a hint that points back to the exact notebook task. **Read it before you write the body.**

> **Your coding agent is a teaching assistant here, not autocomplete.** The repo's [`AGENTS.md`](../../AGENTS.md) puts Claude Code and Codex into instructor mode: they explain, debug, and review, but decline to write your app. The code is a couple hundred lines; the understanding is the assignment.

### Why Pydantic, and not a dataclass like Week 1's `Hit`?

Because this app has an HTTP boundary, and FastAPI is built on Pydantic. A `@dataclass` gives you structure but **no validation, no JSON (de)serialization, and no schema**. Pydantic gives you all three: a bad request (`k=999`, no question) is rejected with a clean `422` before your agent runs, responses serialize themselves, and `/docs` documents every field for free. `schemas.py` is Week 1's `Hit` grown up — `Source` does the same job, now across the wire. You'll defend this choice in `DECISIONS.md`.

### A second source: optional web search

The agent ships with two places to look. The local guide is one; the second is **web search (Tavily)**, wired in for you by `tools.build_web_search_tool` and `service.build_agent`. It's off by default — set `TAVILY_API_KEY` in your `.env` and the agent gains a `web_search` tool it can call; leave it unset and everything runs on the guide alone. You write no code to turn it on, because `build_agent_graph` binds a *list* of tools.

This is the two-source setup from Session 4. It's not busywork: the guide is a fixed snapshot, the web is current, and *two* sources are what make the routing decisions in Step 4 real — "try the guide first, hit the web on a miss," "cap web calls to one per question," "never let a medical claim come from an unvetted web result." Those are decisions you own in the graph, not the model's to improvise. (Web results show up in the `trace`; `sources` stay grounded in the guide, since a web result doesn't carry a `chunk_id`.)

---

## Your corpus

`data/HealthWellnessGuide.txt` ships here and everything below works on it — but you don't have to use it. Drop any `.txt` into `data/` and the app finds it (exactly one `.txt`, or it asks which). The four requirements from Week 1 still hold:

| Requirement | Why |
| --- | --- |
| **Plain `.txt`, utf-8** | `build_retriever` loads text. PDF is a Step 4 augmentation, not a prerequisite |
| **10,000–50,000 characters** | enough chunks that `k` matters, few enough you can eyeball what came back |
| **Facts it keeps in two places** | your "needs 2 chunks" question has to be writable |
| **A clear edge** | you need to know what it does *not* cover, to write the decline question |

> ⚠️ **Don't pick something famous.** A corpus the model already memorised answers correctly even with retrieval broken — so you lose the ability to attribute a failure to a stage. Obscure beats interesting. And remember the new failure mode this week: the agent can decide *not to retrieve at all* and answer from the model. That's exactly the behaviour you're learning to catch.

---

## Step 1: Run the notebooks, then read them

```bash
cd 04_Agentic_Search
uv sync
cp .env.example .env     # then set OPENAI_API_KEY=sk-...
```

Open `Agentic_RAG_From_Scratch.ipynb`, **select `.venv` as your kernel**, run it top to bottom, and answer the openers. You are about to reimplement its four stages behind an API. Three things to find before you leave the notebook:

| # | Look at | Find |
| :---: | --- | --- |
| a | `should_continue` | it reads **one** thing — the last message's `tool_calls` — and returns `"tools"` or `"end"`. This three-line function is the entire agent decision. Which of your questions makes it decide wrong? |
| b | the RAG tool | it returns a **string**. The model can only ever emit text — so where do the structured `sources` your API promises come from? (Answer: you reconstruct them in `service.answer_question`.) |
| c | `tools -> agent` edge | the loop has no built-in stop. A fresh `create_agent` had a recursion limit; your hand-built graph needs one too. What question could make it loop? |

---

## Step 2: Fill in the five stubs

```bash
cd "00_Technical_Challenges/Week 2"
uv sync
cp .env.example .env     # then set OPENAI_API_KEY=sk-...
uv run python -m agent_app
```

The server starts **even with every stub empty** — open <http://127.0.0.1:8000/docs> and try `POST /ask`; it returns `501` naming the first file to open. Fill the stubs in dependency order; each one moves the error along:

| File | Functions | Your check |
| --- | --- | --- |
| `index.py` | `build_retriever` | server logs `agent ready — indexed …`; `/health` shows `agent_ready: true` |
| `tools.py` | `make_search_tool` | call the tool once in a scratch cell; it returns source blocks in the `[source chunk_id=… score=…]` format |
| `graph.py` | `should_continue`, `build_agent_graph` | a wellness question routes through `tools`; "What is 125 * 8?" does not |
| `service.py` | `answer_question` | `/ask` returns a full `AskResponse` — answer, `used_retrieval`, `sources`, `trace` |

The Session 4 notebook has a working version of the first three. **Reading it and writing your own is the assignment; pasting it in is not** — you'll explain this on a Loom. Three things the skeleton decided for you:

1. **The index is built once, and on disk** — `api.py`'s lifespan calls `build_agent` once, not per request, and Qdrant persists to `qdrant_storage/`. So the first boot embeds; later boots load from disk for free. Re-embedding the whole corpus on every question (Week 1's CLI) — or even every startup — is the bug you're avoiding. Make `build_retriever` idempotent: don't re-create or re-fill a collection that's already there.
2. **The tool's output format is a contract.** `tools.SOURCE_LINE` is the one seam connecting what the model reads to the `sources` your API returns. Keep the tool and `answer_question` in sync.
3. **`answer_question` does pure data-shaping** — no model or retriever calls. It walks the messages the graph already produced and fills the Pydantic object. That gap, messy messages → typed object, is the whole lesson of the week.

> **`sources` is only as honest as your parsing.** If `used_retrieval` is `true` but `sources` is empty, your `answer_question` isn't reading the `ToolMessage`s — not the agent's fault.

---

## Step 3: 10 questions, what fails?

The agent adds failure modes Week 1 never had. Write questions that probe each:

| Kind | What it has to do | Example |
| --- | --- | --- |
| **Should retrieve** | a wellness fact in the corpus — the agent must call the tool | "How many minutes of aerobic activity per week?" |
| **Should NOT retrieve** | math, a greeting, off-topic — the agent must *not* search | "What is 125 × 8?" |
| **Decline** | wellness-adjacent but not in your corpus. Correct answer is a refusal | "What dose of ibuprofen for a migraine?" |
| **Needs 2 chunks** | two facts kept apart — does `k=3` reach both? | "What should my morning *and* evening routine look like?" |
| **Citation integrity** | a grounded answer whose `sources` must actually contain the claim | any "should retrieve" question — then read `sources` |

Run all 10. ✅/❌ with **one line naming a stage, not a mood**:

```markdown
| # | Question | ✅/❌ | What went wrong, where |
|---|----------|------|------------------------|
| 1 | Aerobic activity per week? | ✅ | retrieved ch.1, answered from it, cited it |
| 2 | What is 125 × 8? | ❌ | agent called search anyway — prompt/routing, not retrieval |
| 3 | Ibuprofen dose? | ❌ | retrieved 3 headache chunks, answered from them — should have declined |
| 4 | Morning and evening routine? | ❌ | retrieval — k=3 reached morning, missed evening |
| 5 | Sleep tips? | ❌ | answered well but `sources` empty — service didn't parse ToolMessages |
```

"Retrieved the wrong chunk", "retrieved when it shouldn't have", "right answer, lost citation", "looped" are four different bugs with four different fixes — in four different files. **The skill is telling them apart**, which means reading the `trace` and `sources`, not just the answer.

> Expect 3–5 failures out of 10. 10/10 means your questions were too kind.

> **Optional — see it visually with LangSmith.** Your `AskResponse.trace` already shows what the agent did; that's what's graded, and it's enough. But if you'd rather *see* each run as a visual trace while you hunt failures, [LangSmith](https://smith.langchain.com) records every model and tool step and draws the loop for you — the same tracing the Session 3 notebook leaves commented out. It's free to start: grab a key, then set `LANGSMITH_TRACING=true`, `LANGSMITH_API_KEY=...`, and `LANGSMITH_PROJECT=aie-week2` in your `.env` before launching the server. It's a lens, not a requirement — nothing in the grade depends on it, and it sends your run data to LangSmith's cloud, so skip it if you'd rather not.

---

## Step 4: One change, measure it

Pick **one** — and pick the one that **fixes a failure from Step 3.** Name the failure, show the numbers either side.

| Augmentation | What failure it targets | Size |
| --- | --- | --- |
| **Recursion / step cap** (invoke with `recursion_limit`, or count loops in state) | the agent that loops forever | a few lines |
| **Deterministic scope route** (a node before the model that declines off-topic) | agent retrieving or answering out of its lane | a node + a router |
| **Guide-first web routing** (needs `TAVILY_API_KEY`; search the guide, only hit the web on a miss, and cap web calls) | the guide missed and the answer needs current info the snapshot can't hold | a router edge + a counter in state |
| **Structured output** (`llm.with_structured_output(Model)`) | flaky answers / sources that don't match the contract | a Pydantic model + one call |
| **Real similarity scores** (`similarity_search_with_score`) | every `Source.score` is 0.0 | 1 method swap |
| **Reranking or metadata filter** | wrong chunk retrieved for the right question | a few lines in the tool |
| **Tool-call budget** (max 1 retrieval per run) | agent over-retrieving, cost/latency | middleware or a counter |
| **Streaming** (`graph.stream` → SSE endpoint) | slow *perceived* latency; your frontend UX | a route + `sse-starlette` |
| **Conversation memory** (checkpointer + `thread_id`) | follow-up questions losing context | compile arg + config |

> **"My score didn't move"** is a finding. Write what you expected, what happened, and your best explanation for the gap. A documented null result beats a vague improvement.

**✅ Deliverables:** the augmentation working in your app; before/after on your 10 questions including regressions; a one-paragraph vibe check.

---

## Step 5: Frontend, diagram, decision

**Frontend** — replace `frontend/index.html` with your own. The shipped page is a 60-line starter that only proves the backend works; the deliverable is a UI *you* built against `POST /ask`. It doesn't need to be fancy — a chat box, the answer, and a sources panel is enough — but it has to be yours, and it has to run. Streaming, chat history, or a trace viewer that renders `AskResponse.trace` are good reaches (and pair with the streaming augmentation; if you turned on LangSmith in Step 3, a link out to the run there is a cheap win on your Loom).

**Diagram** — paper, drawing app, or a Mermaid block, not a box labeled "agent". Draw the graph (`START → agent → should_continue → tools → agent → END`) *and* the service boundary around it (HTTP request → `AskRequest` → graph → messages → `answer_question` → `AskResponse` → JSON). Mark the two arrows that call OpenAI (embed query, chat) and where your Step 4 change sits. If you can't draw it without opening your code, you just found the part you don't understand yet.

**Decision** in `DECISIONS.md` — short answers, not an essay:

| Field | What it means |
| --- | --- |
| **What I changed** | Your augmentation. 1 sentence |
| **Why** | Which of your 10 failures it targeted. Before/after |
| **What would change my mind** | The condition under which you'd undo it |
| **dataclass vs Pydantic** | One or two lines: what Pydantic bought this app that a dataclass wouldn't |

That third field is what everyone skips and gets asked about. *"I added a `recursion_limit=8` after a comparison question looped twice; it costs nothing on normal runs and turns a hang into a clean error. I'd raise it if a legitimate multi-tool question hit the ceiling."* is an engineering position. *"Added a limit, seems safer"* is a preference.

**✅ Deliverables:** your frontend; the diagram (data types on arrows, paid calls marked); `DECISIONS.md` with all four fields.

---

## If it's blocked

- **`No OPENAI_API_KEY found`** — Did you `cp .env.example .env` **in this folder** and add your key (no quotes, no spaces around `=`)? Does the key have credit? Zero balance fails at *request*, not auth.
- **`/ask` returns 501** — A stub is still unwritten; `detail` names the file. That's the design: the server runs so you can test incrementally. Fill `index → tools → graph → service`.
- **`agent_ready: false` at `/health`** — `build_retriever` raised (unwritten, or the embedding/Qdrant call failed), or there isn't exactly one `.txt` in `data/`. Read the server's startup log line.
- **`Storage folder qdrant_storage is already accessed by another instance`** — on-disk Qdrant allows one client at a time, and another server (or a notebook) still holds it. Stop the other process. If you changed the corpus, chunking, or embedding model, delete `qdrant_storage/` so it re-embeds — otherwise you're querying a stale index.
- **`ModuleNotFoundError: agent_app` / `fastapi`** — Run from `00_Technical_Challenges/Week 2/` with `uv run python -m agent_app`, and `uv sync` if you haven't. Plain `python` lacks the deps.
- **`used_retrieval: true` but `sources: []`** — `answer_question` isn't parsing the `ToolMessage`s, or your tool isn't emitting the `SOURCE_LINE` format. The two must match exactly.
- **Every `Source.score` is 0.0** — a plain retriever doesn't return scores; you're returning the placeholder. Switch to `similarity_search_with_score` (that's the Step 4 option).
- **The agent loops / `GraphRecursionError`** — expected without a cap. Invoke with `config={"recursion_limit": 8}`, or add a step counter to the state. This is a Step 4 augmentation hiding as a bug.
- **The agent answers a math question by searching** — routing/prompt, not retrieval. Your `should_continue` is fine; the *model* chose to call the tool. Tighten the system prompt, or add a deterministic scope route.

---

## Your final submission

Sync your fork first, then commit and push:

```bash
git checkout main && git pull upstream main && git push origin main
```

Post **your repo link and Loom** in [Maven](https://maven.com/aimakerspace/ai-eng-bootcamp/11/home). Your repo should contain your runnable service, your frontend, `DECISIONS.md`, and your diagram, all in `00_Technical_Challenges/Week 2/`. **After the deadline, comment on at least 2 other students' submissions** — read their `DECISIONS.md` and leave something specific.

> **Never commit secrets.** `.env` is gitignored for a reason. Run `git diff --staged` before you push. A key in a public repo is scraped in minutes, and deleting the commit doesn't help — rotate it.

---

Everything after this week assumes you have an agent that decides when to retrieve, lives behind an API that returns typed data, can say where its answer came from, and that you know which stage to look at when it's wrong. **That's the whole deliverable.**
