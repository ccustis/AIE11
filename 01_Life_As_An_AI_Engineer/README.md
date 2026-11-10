<p align = "center" draggable="false" ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719" 
     width="200px"
     height="auto" alt="AI Makerspace"/>
</p>

## <h1 align="center" id="heading">Session 1: Life As An AI Engineer</h1>

### [Quicklinks](https://github.com/AI-Maker-Space/AIE11/tree/main/00_AIE_Quicklinks)

| 📰 Session | ⏺️ Recording | 🖼️ Slides | 📝 Technical Challenge | 📁 Feedback |
|:-----------------|:------------|:----------|:--------|:------------|
| You are here! | [Recording!](https://us02web.zoom.us/rec/share/jAarPK0giKhBtd7Sk2SUaJQRTBGQSewEVIgMquMDU0kgeL6e5p3PdGVstrCZx3A.QaC8mvzYsqtvEnoZ) <br> passcode: `9kvErL?d` | [Slides](https://canva.link/5n1omu8z39yrhat) |   [Week 1](../00_Technical_Challenges/Week%201/README.md)      |  [11/9](https://forms.gle/znovu6Fieh3zaSx49) |

---

## Contents

- [🎯 Learning Outcomes](#learning-outcomes)
- [🧰 New Tools](#new-tools)
- [🖥️ Environment setup](#environment-setup)
- [API Keys & `.env`](#api-keys--env)
- [The concepts](#the-concepts)
  - [🔀 Why version control](#why-version-control)
  - [🔀 How version control](#how-version-control)
  - [⌨️ Why an LLM API call](#why-an-llm-api-call)
  - [⌨️ How — the three roles, then prompting](#how-the-three-roles)
  - [🖱️ Why an interactive development environment](#why-interactive-dev-environment)
  - [🎨 Why a frontend and a backend](#why-frontend-and-backend)
  - [🎨 How — no demo, by design](#how-no-demo)
- [Build 🏗️](#build) · [Ship 🚢](#ship) · [Share 🚀](#share)
- [🧯 If it's blocked](#if-its-blocked)

---

<a id="learning-outcomes"></a>

## 🎯 Learning Outcomes

By the end of this session you will have:

- Understood the course structure, the technical challenges, and what certification requires
- Met the cohort staff, your peer supporters, and your journey group
- **Set up and validated** your AI engineering development environment
- Applied AI-assisted coding practice using Claude Code

The third one is the deliverable. The rest you get by showing up; a working machine you
have to actually build, and this session exists so that you do it **now** rather than in
week 4 with an assignment due.

<a id="new-tools"></a>

## 🧰 New Tools

|                     | Tool                                                  | Why this one                                           |
|---------------------|-------------------------------------------------------|--------------------------------------------------------|
| **LLM**             | [OpenAI GPT](https://platform.openai.com/docs/models) | the models every project in this course calls          |
| **Editor**          | [VS Code](https://code.visualstudio.com/)             | officially supported, and the terminal lives inside it |
| **Coding Agent**    | [Claude Code](https://claude.com/download)            | runs in that same terminal, reads the repo's rules     |
| **Runtime**         | Python + [uv](https://docs.astral.sh/uv/)             | one tool for Python versions, venvs and dependencies   |
| **Version Control** | Git + [GitHub](https://github.com/)                   | how you get course material and submit work            |

> Prefer Cursor, Codex, or PyCharm? They work on the same base setup, but you are on your
> own for debugging. See [Initial Setup](../00_Docs/Prerequisites/Initial_Setup/README.md).

---

### Outline

🤜 Session #1 — [`Life_As_An_AI_Engineer.ipynb`](./Life_As_An_AI_Engineer.ipynb)

- Part 0: Does your environment actually work? (0.1 Python → 0.6 the installer's own check)
- Part 1: Version control, with this repo as the example
- Part 2: The LLM API call and the three message roles
- Part 3: Prompt engineering, five patterns
     - 🚧 ACTIVITY #1: Stack three patterns in one call
- Part 4: Frontend and backend, and why they are separate

---

<a id="environment-setup"></a>

## 🖥️ Environment setup

Your machine is set up by **one script**, from the course's
[Interactive-Dev-Environment-for-AI-Engineers](https://github.com/AI-Maker-Space/Interactive-Dev-Environment-for-AI-Engineers) repo. It installs everything this
course needs and nothing it doesn't, and it is **safe to re-run at any time** — whatever
is already done gets reported `[ OK ]` and skipped.

### 1. Install VS Code first

The script does not install VS Code — get it from
[code.visualstudio.com/download](https://code.visualstudio.com/download). On a Mac, move it
into **Applications** before opening it, or the `code` command won't work properly.

Then open its built-in terminal: **Terminal → New Terminal**. Everything below is typed
there, which is why the process is nearly identical on every OS.

| Your prompt looks like  | You are on | Use                        |
|-------------------------|------------|----------------------------|
| `PS C:\Users\you>`      | Windows    | the **Windows** commands   |
| `you@laptop ~ %` or `$` | Mac/Linux  | the **Mac/Linux** commands |

> **Windows:** if the panel says `bash`, click the arrow next to **+** and pick **PowerShell**.

### 2. Run the installer

**Mac/Linux**
```bash
mkdir -p ~/ai-eng && curl -fsSL https://raw.githubusercontent.com/AI-Maker-Space/Interactive-Dev-Environment-for-AI-Engineers/main/setup.sh -o ~/ai-eng/setup.sh && bash ~/ai-eng/setup.sh
```

**Windows**
```powershell
mkdir -Force $HOME\ai-eng | Out-Null; irm https://raw.githubusercontent.com/AI-Maker-Space/Interactive-Dev-Environment-for-AI-Engineers/main/setup.ps1 -OutFile $HOME\ai-eng\setup.ps1; powershell -ExecutionPolicy Bypass -File $HOME\ai-eng\setup.ps1
```

Budget ~15 minutes, plus 5-15 more on a Mac that still needs Apple's developer tools.
It will ask you a few things: your name and email for git, whether to add an SSH key to
GitHub (say yes, it copies the key and opens the right page), optionally Homebrew on a Mac
(Enter to skip), and your password on Linux.

#### What it installs, and where

Everything lives in **one directory** so nothing is scattered across your machine:

```
~/ai-eng/
├── env.sh  /  env.ps1     ← you source this in each terminal
├── setup.sh / setup.ps1   the installer itself
├── bin/                   uv
├── python/                Python (UV_PYTHON_INSTALL_DIR)
├── nvm/                   nvm v0.40.8, for Node   (Mac/Linux)
├── node/                  portable Node 24        (Windows)
├── setup.log              full log of the last run
├── setup-report.txt       written only on a FAIL or WARN
└── path-backup.txt        your PATH before it was edited (Windows)

~/.local/bin/              Claude Code (its installer insists on this path)
```

| Tool           | Version  | Notes                                                                                |
|----------------|----------|--------------------------------------------------------------------------------------|
| Git            | latest   | Mac: via Apple's developer tools. Windows: via `winget`. Linux: your package manager |
| uv             | latest   | installed into `~/ai-eng/bin`                                                        |
| Python         | **3.13** | any existing 3.12-3.14 is accepted and reused; 3.13 installed only if you have none  |
| Node.js        | **24**   | Mac/Linux via nvm; Windows downloads a portable copy, SHA256-verified                |
| Claude Code    | latest   | into `~/.local/bin`                                                                  |
| VS Code `code` | —        | the command only. You install the app yourself                                       |

It also sets `init.defaultBranch main` if you have no preference set, and creates an
ed25519 SSH key at `~/.ssh/id_ed25519` if you don't already have a working one.

### 3. Load the tools into your terminal

This is the step people miss, and it produces every "but I installed it!" message in the
help channel. The installer does **not** modify every shell on your machine. You load it,
per terminal:

```bash
source ~/ai-eng/env.sh          # Mac/Linux
```
```powershell
. $HOME\ai-eng\env.ps1          # Windows
```

**In every new terminal you use for coursework.** Close the terminal, and it unloads, which
is the point: your other projects are untouched. The one exception is VS Code's `code`
command, configured once and available everywhere.

> If `uv`, `node` or `claude` says *not found*, you skipped this step. If you launched
> Jupyter from an unloaded terminal, the kernel inherited that — load it, then **restart
> the kernel**.

### 4. Verify it

```bash
bash ~/ai-eng/setup.sh --check                                          # Mac/Linux
```
```powershell
powershell -ExecutionPolicy Bypass -File $HOME\ai-eng\setup.ps1 -Check   # Windows
```

Check mode changes nothing. You want **All good**; it exits non-zero if anything failed.

| Marker   | Means                          | What to do                  |
|----------|--------------------------------|-----------------------------|
| `[ OK ]` | already installed and working  | nothing                     |
| `[DONE]` | installed or fixed on this run | nothing                     |
| `[ -- ]` | optional, skipped              | nothing — this is fine      |
| `[WARN]` | works, but worth a look        | read the `->` hint under it |
| `[FAIL]` | needs fixing                   | read the `->` hint under it |

On a `FAIL` or `WARN` the script writes `~/ai-eng/setup-report.txt` **and copies it to
your clipboard**. Paste that into the help channel; the full detail is in `~/ai-eng/setup.log`.

#### Flags worth knowing

| Mac/Linux             | Windows               | What it does                                                |
|-----------------------|-----------------------|-------------------------------------------------------------|
| `--check`             | `-Check`              | report only, change nothing                                 |
| `--tools-only`        | `-ToolsOnly`          | install tools, skip the git name/email and GitHub SSH steps |
| `--yes` / `-y`        | `-Yes`                | ask nothing, take every default                             |
| `--no-copy`           | `-NoCopy`             | don't copy the report to your clipboard                     |
| `--help` / `-h`       | —                     | print usage and exit                                        |
| `PYTHON_VERSION=3.13` | `-PythonVersion 3.13` | override the Python version                                 |
| `NODE_VERSION=24`     | `-NodeVersion 24`     | override the Node major version                             |
| `AI_ENG_HOME=<dir>`   | —                     | install somewhere other than `~/ai-eng`                     |

### 5. Install the VS Code notebook extensions

Two, both from Microsoft:

```bash
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter
```

**Supported OSes:** Windows, Linux (Debian/Ubuntu/Fedora/SUSE/Arch), macOS Intel, macOS
Apple Silicon. WSL2 is detected and handled.

Prefer to install each tool by hand? There is a
[step-by-step DIY guide](https://github.com/AI-Maker-Space/Interactive-Dev-Environment-for-AI-Engineers/blob/main/details/README.md).

---

### Steps to Run

Assuming you have run the installer above:

1. Load the tools into this terminal — `source ~/ai-eng/env.sh` (Mac/Linux) or
   `. $HOME\ai-eng\env.ps1` (Windows)
2. Run `uv sync` **in this folder** (each project folder has its own `pyproject.toml` and `.venv`)
3. Copy `.env.example` to `.env` and add your OpenAI key (see [API Keys & `.env`](#api-keys--env) below)
4. Open `Life_As_An_AI_Engineer.ipynb` and select **this folder's** `.venv` as your kernel
5. Run Part 0 first. It needs no API key, and it tells you whether steps 1-4 actually worked

```bash
source ~/ai-eng/env.sh   # Mac/Linux; Windows: . $HOME\ai-eng\env.ps1
cd 01_Life_As_An_AI_Engineer
uv sync
cp .env.example .env     # then edit .env and set OPENAI_API_KEY=sk-...
```

## API Keys & `.env`

This folder reads your OpenAI key from a **`.env` file in this folder**. Every project
folder keeps its own `.env`, so keys stay scoped per project.

1. Copy the template and add your key:
   ```bash
   cp .env.example .env
   # then edit .env and set OPENAI_API_KEY=sk-...
   ```
2. That's it. The notebook calls `load_dotenv()`, which reads this folder's `.env`
   automatically (and falls back to the repo root's `.env` if you keep one there).

`.env` is gitignored, so your real key is never committed; only `.env.example` (the
template, no secret) is tracked. **Part 0.4 of the notebook proves this** by asking git
directly, rather than trusting it.

You can also override the model or point at any OpenAI-compatible endpoint:

```
LLM_MODEL=gpt-5.4-mini                   # any OpenAI-compatible model string
LLM_API_BASE=http://localhost:4000/v1    # a LiteLLM proxy, a local server, ...
```

### Starting Claude Code or Codex in this folder

Just `cd` into the folder and launch the agent:

```bash
cd 01_Life_As_An_AI_Engineer
claude      # or: codex
```

**You do not need this folder's `.env` for the agent itself.** Claude Code and Codex
authenticate with their *own* credentials, not the project key:

- **Claude Code** signs in to your Anthropic account (or reads `ANTHROPIC_API_KEY` from your shell).
- **Codex** signs in to your OpenAI account (or reads `OPENAI_API_KEY` from your shell).

The `OPENAI_API_KEY` in `.env` is for the **application code** — the notebook's OpenAI
calls via `python-dotenv` — which is a separate concern from how the agent talks to its
own model.

> **The agent is a teaching assistant here, not an autocomplete.** The repo's
> [`AGENTS.md`](../AGENTS.md) puts Claude Code and Codex into instructor mode: they
> explain, debug and review, and decline to write your assignments. That is the
> system-role priority from Part 2 of the notebook, applied to you.

---

# The concepts

The notebook runs these as code. This section is the argument behind each one, so you can
read it before class and have the *why* already settled.

<a id="why-version-control"></a>

## 🔀 Why version control

Not "so you don't lose your work" — backups do that. Version control exists because
**more than one version of the truth has to be true at once.**

With one environment, the moment you start editing you are editing the only copy users
have. So you split the timeline into **dev** (your machine, allowed to be broken) and
**production** (what users see, only what works). That alone stops you breaking
production by typing.

But it leaves a gap: the jump from "works on my laptop" to "live for everyone" is one
move, tested nowhere real. So teams add **staging** — a real deployment with fake users,
where you find out your change was wrong before customers do.

**Staging is the entire argument for version control.** Three states have to coexist and
changes have to move between them deliberately. Git is the tool that holds three states
at once.

| Branch      | Industry meaning                             | In this course                  |
|-------------|----------------------------------------------|---------------------------------|
| `main`      | production. "The current official story"     | where your submitted work lives |
| `develop`   | staging. "The draft of the next chapter"     | not used; we keep it simple     |
| `feature/*` | dev. "Paragraphs before they go in the book" | use freely for experiments      |

<a id="how-version-control"></a>

## 🔀 How version control

Three places, one direction of flow: `upstream` → `origin` → `local` → `origin`.

| Name         | Where                     | What you do                           |
|--------------|---------------------------|---------------------------------------|
| **upstream** | AI Makerspace's repo      | `pull` from it. Never push            |
| **origin**   | *your* fork on GitHub     | `push` to it. This is what you submit |
| **local**    | the folder on your laptop | edit files here                       |

Your weekly loop, for all ten weeks:

```bash
git checkout main
git pull upstream main      # get new course material
git push origin main        # keep your fork level with it
# ... do the assignment ...
git add .
git diff --staged           # READ IT. this is the step that saves you
git commit -m "week N"
git push origin main
```

> ⚠️ **`git diff --staged` before every commit.** It is how you catch a `.env` with a
> live key before the commit is permanent. A key in a public repo is scraped in minutes,
> and deleting the commit does not help — you have to rotate the key.

Deeper: [Git & GitHub](../00_Docs/Prerequisites/Initial_Setup/1_Git_and_GitHub/README.md) ·
[Set Up Initial Repos](../00_Docs/Prerequisites/Initial_Setup/2_Set_Up_Initial_Repos/README.md) ·
[Version Control](../00_Docs/Prerequisites/Initial_Setup/3_Version_Control/README.md) ·
[Weekly Git Workflow](../00_Docs/Prerequisites/Initial_Setup/4_Your_Weekly_Git_Workflow/README.md)

<a id="why-an-llm-api-call"></a>

## ⌨️ Why an LLM API call

You have used ChatGPT. The model is the same. What changes is what you can do with the call:

| In the chat window                 | Through the API                                  |
|------------------------------------|--------------------------------------------------|
| You type, you read                 | *Your code* types, and your code reads           |
| One conversation                   | Ten thousand, in parallel                        |
| You decide what to send, each time | You decide the rules **before** any user arrives |
| Output is text on a screen         | Output is a typed object your program acts on    |

The third row is the real one. As a user you write a message. As an engineer you write the
**system instructions** — the rules that hold for every user — and the user's message
arrives inside the frame you built. That asymmetry is the job.

<a id="how-the-three-roles"></a>

## ⌨️ How — the three roles, then prompting

As a user: text in, text out. As a developer: **a list of role-tagged messages in, one
message out.**

| Role        | Who writes it                     | What it does                                 |
|-------------|-----------------------------------|----------------------------------------------|
| `system`    | **you, the engineer**             | the rules. Prioritised above everything else |
| `user`      | your app's user                   | the request                                  |
| `assistant` | the model — **or you, faking it** | a reply. Faking these is how few-shot works  |

**Demo, in [the notebook](./Life_As_An_AI_Engineer.ipynb) Part 3** — five patterns, each
shown weak first and then strong, because the weak version is what you will write by
default:

| Pattern               | What it buys you                                                             |
|-----------------------|------------------------------------------------------------------------------|
| **Persona**           | `instructions` steer voice without changing facts                            |
| **Few-shot**          | teach a convention the model cannot guess, with two examples and no training |
| **Chain of thought**  | reasoning before answering, with a measurable token and latency cost         |
| **Structured output** | a Pydantic schema enforced at the API layer, not a polite request for JSON   |
| **Grounded context**  | paste a document in and answer only from it. "RAG by hand"                   |

That last one is where Session 2 begins: pasting works until the document doesn't fit, and
then you need chunking, embeddings and search.

More depth: [`instructor_materials/Prompt_Engineering_Patterns.ipynb`](instructor_materials/Prompt_Engineering_Patterns.ipynb) ·
[LLM APIs — the System role](../00_Docs/Prerequisites/Initial_Setup/6_LLM_APIs/README.md)

<a id="why-interactive-dev-environment"></a>

## 🖱️ Why an interactive development environment

A notebook is a lab: you see every intermediate value, you re-run one cell without
re-running the other twenty, and when something breaks you are standing right next to it.
That is exactly right for learning what a call returns.

It is also not a product. No users, no URL, and your API key sits in the same process as
your output. Both halves of this course need both: notebooks to understand, projects to
ship.

### Which one do we recommend?

**VS Code, with Claude Code in its terminal.** That pairing is officially supported, which
in practice means: when it breaks, we can help you.

| Tool                    | Status                                              |
|-------------------------|-----------------------------------------------------|
| VS Code                 | ✅ officially supported                             |
| Claude Code             | ✅ officially supported                             |
| Cursor, Codex, Windsurf | works on the same setup, debugging is on you        |
| PyCharm / JetBrains     | works; only the "open a terminal" step differs      |
| Colab                   | fine for a quick notebook, not for the project work |

Install path: [Environment setup](#environment-setup) above (one script, ~15 minutes) ·
[Coding Agents](../00_Docs/Prerequisites/Initial_Setup/5_Coding_Agents/README.md)

<a id="why-frontend-and-backend"></a>

## 🎨 Why a frontend and a backend

Because **anything in the browser belongs to the user.**

Ship notebook logic straight into a web page and your `OPENAI_API_KEY` goes with it, into
JavaScript anyone can read. One "view source" and your billing is theirs. Your system
prompt leaks the same way — and a rule the user can edit is not a rule.

So the work divides by who is allowed to know what:

|                    | **Frontend**                 | **Backend**                               |
|--------------------|------------------------------|-------------------------------------------|
| Runs on            | the user's device            | your server                               |
| Typical stack      | TypeScript / React           | Python / FastAPI                          |
| Knows your API key | **never**                    | yes                                       |
| Job                | collect input, render output | hold secrets, call the LLM, enforce rules |
| Deployed to        | Vercel                       | Vercel / Render                           |

```
browser  ──request──>  your backend  ──API key──>  OpenAI
   ▲                        │
   └──────── answer ────────┘
```

One extra hop versus the notebook, and that hop is the security boundary.

<a id="how-no-demo"></a>

## 🎨 How — no demo, by design

We are not building this in Session 1; today is about a machine that works. The reference
implementation is **[The AI Engineer Challenge](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge/tree/dc-challenge)**,
and we point you at it rather than rebuilding it here — but the machine you just validated
in Part 0 runs it *as-is*. Same stack: `uv sync`, Python 3.13, a per-project `.env`. Nothing
new to install.

Its shape is the split above made literal:

- **The backend is given to you** — a FastAPI service in
  [`api/`](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge/tree/dc-challenge/api)
  that holds the key and the system prompt and exposes `POST /api/chat` and `GET /api/health`.
  Open `api/index.py`: the secret lives on the server, exactly as the table above argues.
- **The frontend is yours to build** — `frontend/` ships empty on purpose. You *vibe-code* a
  UI that calls `POST /api/chat`, and never the model directly.
- **You deploy both together** — `npx vercel` from the repo root puts them on one domain; the
  provider keys go in the Vercel dashboard, never in the browser.
- **Provider-agnostic** — one `LLM_PROVIDER=openai|anthropic` switch, the same idea you met in Part 2.

> 🧭 **Same `AGENTS.md`, opposite instructions.** The Challenge repo also has an `AGENTS.md` —
> but it tells the agent to *build and commit*. The Challenge is where you let the agent write
> code, not where it holds back like this course's teaching-assistant `AGENTS.md` does. Same
> file, different context, different rules. That is the system role from Part 2, one more time.

### The AI Engineer Challenge: the full walkthrough

| # | Step                                                                                | Where it is covered                                                                                                                                                                                                                                                                |
|:-:|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | **Git** — fork, clone, set `upstream`, commit, push                                 | [Set Up Initial Repos](../00_Docs/Prerequisites/Initial_Setup/2_Set_Up_Initial_Repos/README.md), and Part 1 of the notebook                                                                                                                                                        |
| 2 | **LLM API** — the call, the roles, the system prompt                                | Parts 2-3 of the notebook                                                                                                                                                                                                                                                          |
| 3 | **Your IDE** — VS Code plus Claude Code, opened on the repo folder                  | [Initial Setup](../00_Docs/Prerequisites/Initial_Setup/README.md), [Coding Agents](../00_Docs/Prerequisites/Initial_Setup/5_Coding_Agents/README.md)                                                                                                                               |
| 4 | **Backend (provided)** — read `api/index.py`; the key and system prompt live here   | the repo's [`api/README.md`](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge/blob/dc-challenge/api/README.md), [Onramp Session 02](../00_Docs/Prerequisites/The_AI_Engineer_Onramp/Session_02_Back_End_Web_App_Development_&_Deployment_of_LLM_Applications/README.md) |
| 5 | **Frontend (you build)** — vibe-code a UI that calls `POST /api/chat`, never OpenAI | [Onramp Session 03](../00_Docs/Prerequisites/The_AI_Engineer_Onramp/Session_03_Connecting_Frontend_UIs_to_Backend_Deployments/README.md)                                                                                                                                           |
| 6 | **Deployment** — `npx vercel` from the repo root; both halves, one domain           | [Onramp Session 02](../00_Docs/Prerequisites/The_AI_Engineer_Onramp/Session_02_Back_End_Web_App_Development_&_Deployment_of_LLM_Applications/README.md)                                                                                                                            |
| 7 | **The complex end-to-end version**                                                  | [Onramp Session 04](../00_Docs/Prerequisites/The_AI_Engineer_Onramp/Session_04_Bulding_Complex_End_to_End_LLM_Applications/README.md)                                                                                                                                              |

The repo: **[The-AI-Engineer-Challenge](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge/tree/dc-challenge)**
· the challenge brief: **[aimakerspace.io/aie-challenge](https://aimakerspace.io/aie-challenge)**

> ℹ️ **Branch note for maintainers.** The repo links point at the **`dc-challenge`** branch,
> where the updated, provider-agnostic version lives. Switch them to `main` once it is merged.

> ℹ️ _If you didn't **really** understand The AI Engineer Challenge when you completed it,
> the [Onramp material](../00_Docs/Prerequisites/The_AI_Engineer_Onramp/README.md) is for
> you. If you're already a senior software engineer, it may not be._

---

<a id="build"></a>

# Build 🏗️

Run [`Life_As_An_AI_Engineer.ipynb`](./Life_As_An_AI_Engineer.ipynb) top to bottom.

Part 0 needs no API key, so start there: it tells you whether your environment is actually
working before you spend anything. **Every ✅ in Part 0 is the real deliverable of this
session.**

<a id="ship"></a>

# Ship 🚢

- [ ] Every cell in **Part 0** prints ✅ (or you know exactly which one doesn't, and why)
- [ ] `git remote -v` shows both `origin` **and** `upstream`
- [ ] One real LLM API call made, with its token counts read
- [ ] All five prompt patterns run, weak→strong difference seen in each
- [ ] The **refusal cell** in Pattern 5 either refused, or you can explain why it didn't
- [ ] **ACTIVITY #1** completed: three patterns stacked in one call, with your own persona
- [ ] The installer's own check reports **All good** —
      `bash ~/ai-eng/setup.sh --check` (Mac/Linux) or
      `powershell -ExecutionPolicy Bypass -File $HOME\ai-eng\setup.ps1 -Check` (Windows)

<a id="share"></a>

# Share 🚀

- Post your Part 0 output in the cohort channel. **If something failed, post that instead** — a broken setup found in week 1 is cheap; found in week 4 it costs you an assignment
- Record a Loom walking through your stacked-pattern activity and what the weak version got wrong
- Make a social media post about your setup and tag @AIMakerspace
- Share 3 lessons learned
- Share 3 lessons not learned

Here's a template to get your post started!

```
🚀 Day one of The AI Engineering Bootcamp! 🎉

Set up my full AI engineering environment and made my first LLM API calls today. 🤖

🔍 Three Key Takeaways:
1️⃣ Version control isn't about backups - it's about dev/staging/production being true at the same time. 🔀
2️⃣ As a user you write the message; as an engineer you write the system prompt. That asymmetry is the whole job. ⌨️
3️⃣ Anything in the browser belongs to the user - which is the entire reason backends exist. 🔐

A huge shoutout to the @AI Makerspace for their resources and guidance. 🙌

10 weeks to go. Let's build! 🌟
```

---

<a id="if-its-blocked"></a>

## 🧯 If it's blocked

### "`uv: command not found`" / "`claude: command not found`" / "`node: command not found`"

Nine times out of ten the tools are installed and simply **not loaded into this terminal**.
The installer does not touch every shell on purpose:

```bash
source ~/ai-eng/env.sh                  # Mac/Linux
. $HOME\ai-eng\env.ps1                  # Windows
```

Run that in **every new terminal** you use for coursework. If you started Jupyter from an
unloaded terminal, load it and then **restart the kernel** — the kernel inherited the old
environment.

Still missing after loading? Then it really isn't installed:
`bash ~/ai-eng/setup.sh --check` will say which one, and re-running without `--check`
installs just the missing piece.

### Part 0.1 says the venv isn't this folder's

Your kernel is pointing somewhere else — usually your system Python. In VS Code, click
the kernel picker (top right) and choose
`01_Life_As_An_AI_Engineer/.venv/bin/python`. Packages installed by `uv sync` are
invisible to any other interpreter.

### Part 0.2 says a package is missing, but `uv sync` succeeded

You almost certainly ran `uv sync` in a different folder. Each project folder has its own
`pyproject.toml` and its own `.venv`. `cd` into **this** folder and run it again, then
restart the kernel.

### "`No OPENAI_API_KEY`"

Did you `cp .env.example .env` **in this folder** and paste your key into it? No quotes,
no spaces around the `=`. Restart the kernel afterwards — `.env` is read at import time,
not continuously. And does the key have credit? A zero balance fails at the *request*,
not at auth, so the error reads differently.

### `git remote -v` shows no `upstream`

One-time setup, once per course:

```bash
git remote add upstream https://github.com/AI-Maker-Space/AIE11.git
git remote -v
```

### Pattern 5's refusal cell answered anyway

That is not a bug in the notebook, it is **the** bug in deployed RAG systems, and you just
reproduced it. The context didn't contain the answer and the model filled the gap from
training data without telling anyone. Read the note under that cell, then carry the
question into Session 2.


