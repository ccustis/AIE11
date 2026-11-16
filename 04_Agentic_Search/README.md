<p align = "center" draggable=”false” ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719" 
     width="200px"
     height="auto"/>
</p>

## <h1 align="center" id="heading">Session 4: Agentic RAG From Scratch</h1>

### [Quicklinks](https://github.com/AI-Maker-Space/AIE11/tree/main/00_AIE_Quicklinks)

| 📰 Session Sheet | ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📝 Homework      | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
| ||  | You are here! |  |  |



### Outline:

In Session 3, `create_agent` gave you an agent in one line — and hid the loop. This session we open that black box and rebuild the exact same loop by hand with **LangGraph**, then turn it into Agentic RAG. Same wellness use case, same cloud models (`gpt-5.6-sol` + `text-embedding-3-small`).

🤜 BREAKOUT ROOM #1:
- Task 1: LangGraph 101 — State, Nodes, Edges
- Task 2: Build the ReAct Loop From Scratch
- Task 3: Run & Inspect the Loop

🤜 BREAKOUT ROOM #2:
- Task 4: Index the Knowledge Base (LangChain + Qdrant)
- Task 5: Assemble Agentic RAG From Scratch

### Steps to Run:

1. Install `uv` — see the [Initial Setup guide](../00_Docs/Prerequisites/Initial_Setup/README.md).
2. Run `uv sync`.
3. Copy `.env.example` to `.env` and add your OpenAI key (see [API Keys & `.env`](#api-keys--env)).
4. Open the notebook and select `.venv` as your kernel.

## API Keys & `.env`

This folder reads your OpenAI key from a **`.env` in this folder** — each project keeps its own, so keys stay scoped per project.

```bash
cp .env.example .env
# then edit .env and set OPENAI_API_KEY=sk-...
```

The notebook calls `load_dotenv()` and reads it automatically (prompting once if no `.env` exists). `.env` is gitignored, so your key is never committed — only the `.env.example` template is tracked.

### Starting Claude Code or Codex in this folder

`cd` into the folder and launch the agent:

```bash
cd 04_Agentic_Search
claude      # or: codex
```

**You don't need this folder's `.env` for the agent itself.** Claude Code signs in to your Anthropic account (or `ANTHROPIC_API_KEY`); Codex signs in to your OpenAI account (or `OPENAI_API_KEY`). The `OPENAI_API_KEY` in `.env` is for the **application code** — the notebook's OpenAI calls — not the agent.

If you run a plain command that expects the key in the environment and doesn't load `.env` itself:

```bash
uv run --env-file .env python some_script.py   # inject into one command
set -a && source .env && set +a                # or load into the shell
```

# Build 🏗️

Run the notebook! Work through `Agentic_RAG.ipynb` top to bottom and answer Questions #1–#4 inside it. You'll build a ReAct agent as a LangGraph `StateGraph` — an `agent` node, a `ToolNode`, and the `should_continue` router that is the real decision `create_agent` hid from you — then turn it into Agentic RAG over the wellness knowledge base.

# Ship 🚢 & Share 🚀 — Technical Challenge 2

The graded work for Sessions 3–4 lives in the Technical Challenges folder:

➡️ **[`00_Technical_Challenges/Week 2`](../00_Technical_Challenges/Week%202/README.md)**

There you take the from-scratch LangGraph loop out of the notebook and stand it up as an **agentic-RAG search service**: a FastAPI backend (the graph behind an HTTP endpoint with a Pydantic contract) and a frontend you build. You fill in the stubs, add one augmentation — a custom routing function, conversation memory via checkpointing, citations, streaming, or a loop cap — then compare it to the baseline, record a Loom, and share a post tagging @AIMakerspace. Full deliverables are in that README.
