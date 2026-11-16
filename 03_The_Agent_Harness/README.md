<p align="center" draggable="false"><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719"
     width="200px"
     height="auto"/>
</p>

## <h1 align="center" id="heading">Session 3: The Agent Harness</h1>

### [Quicklinks](https://github.com/AI-Maker-Space/AIE11/tree/main/00_AIE_Quicklinks)

| 📰 Session Sheet | ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📝 Homework      | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
| ||  | You are here! |  |  |



### Outline:

In Session 2 you were the control flow — retrieve, then generate, every time. This session you hand the model a **toolbox** and let it decide when to use it. You'll build an agent harness with LangChain's `create_agent`, turn the wellness knowledge base into a **tool** the agent chooses to call (Agentic RAG), and wrap the loop in **middleware** to watch and bound it. Same wellness use case, cloud models (`gpt-5.6-sol` + `text-embedding-3-small`).

🤜 BREAKOUT ROOM #1:
- Task 1: From Pipeline to Agent Loop
- Task 2: The harness with no framework
- Task 3: Define Tools with `@tool`
- Task 4: Build the Baseline Agent with `create_agent`

🤜 BREAKOUT ROOM #2:
- Task 5: Inspect the Loop (stream, trace, visualize)
- Task 6: Agentic RAG — turn retrieval into a tool
- Task 7: Add Middleware (logging + a call budget)

### Steps to Run:

1. Install `uv` — see the [Initial Setup guide](../00_Docs/Prerequisites/Initial_Setup/README.md).
2. Run `uv sync`.
3. Copy `.env.example` to `.env` and add your OpenAI key (see [API Keys & `.env`](#api-keys--env)).
4. Open `The_Agent_Harness.ipynb` and select `.venv` as your kernel.

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
cd 03_The_Agent_Harness
claude      # or: codex
```

**You don't need this folder's `.env` for the agent itself.** Claude Code signs in to your Anthropic account (or `ANTHROPIC_API_KEY`); Codex signs in to your OpenAI account (or `OPENAI_API_KEY`). The `OPENAI_API_KEY` in `.env` is for the **application code** — the notebook's OpenAI calls — not the agent.

# Build 🏗️

Run the notebook! Work through `The_Agent_Harness.ipynb` top to bottom and answer Questions #1–#4 inside it. You'll build an agent with `create_agent`, give it tools (including a Qdrant-backed retrieval tool for Agentic RAG), inspect the loop with streaming and traces, and wrap it in logging + call-budget middleware.

# Ship 🚢 & Share 🚀 — Technical Challenge 2

The graded work for Sessions 3–4 lives in the Technical Challenges folder:

➡️ **[`00_Technical_Challenges/Week 2`](../00_Technical_Challenges/Week%202/README.md)**

There you take the agent out of the notebook and stand it up as an **agentic-RAG search service**: a FastAPI backend (the agent loop behind an HTTP endpoint with a Pydantic contract) and a frontend you build. You fill in the stubs, add one augmentation — a new tool, custom middleware, citations, a tool-call budget, or human-in-the-loop approval — then compare it to the baseline, record a Loom, and share a post tagging @AIMakerspace. Full deliverables are in that README.
