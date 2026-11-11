<p align = "center" draggable=”false” ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719" 
     width="200px"
     height="auto"/>
</p>

## <h1 align="center" id="heading">Session 2: Dense Vector Retrieval</h1>

### [Quicklinks](https://github.com/AI-Maker-Space/AIE11/tree/main/00_AIE_Quicklinks)

| 📰 Session Sheet | ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📝 Homework      | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
| ||  | You are here! |  |  |



### Outline:

🤜 BREAKOUT ROOM #1:
- Task 1: Imports and Utilities
- Task 2: Documents
- Task 3: Embeddings and Vectors
- Task 4: Prompts
- Task 5: Retrieval Augmented Generation

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
cd 02_Dense_Vector_Retrieval
claude      # or: codex
```

**You don't need this folder's `.env` for the agent itself.** Claude Code signs in to your Anthropic account (or `ANTHROPIC_API_KEY`); Codex signs in to your OpenAI account (or `OPENAI_API_KEY`). The `OPENAI_API_KEY` in `.env` is for the **application code** — the notebook's OpenAI calls — not the agent.

If you run a plain command that expects the key in the environment and doesn't load `.env` itself:

```bash
uv run --env-file .env python some_script.py   # inject into one command
set -a && source .env && set +a                # or load into the shell
```

# Build 🏗️

Run the notebook! Work through `Pythonic_RAG.ipynb` top to bottom and answer the questions inside it.

# Ship 🚢 & Share 🚀 — the Week 1 Technical Challenge

The graded work for this session lives in the Technical Challenges folder:

➡️ **[`00_Technical_Challenges/Week 1`](../00_Technical_Challenges/Week%201/README.md)**

There you turn this notebook into a terminal app, add one augmentation (PDF support, a new distance metric, vector-database metadata, a different embedding model, a YouTube link ingest, or whatever suits your use-case), draw a diagram of your RAG pipeline, record a Loom, and share a post tagging @AIMakerspace. Full deliverables and submission steps are in that README.
