<div align="center">
  <img
    src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719"
    width="200"
    alt="AI Makerspace logo"
  />
  <h1>Technical Challenge 1</h1>
  <p><strong>Your first retrieval app: out of the notebook and into a package you can run from a terminal.</strong></p>
</div>

---

## Overview

> **Read first:** [`02_Dense_Vector_Retrieval/README.md`](../../02_Dense_Vector_Retrieval/README.md) for setup, and work through `Pythonic_RAG.ipynb` before you start here.

The notebook has five stages: load a text file, split it, embed it, search by cosine similarity, present the top hits to a chat model. **This week it becomes an app** — a standalone Python project in this folder with its own `pyproject.toml`, `.env`, data, and terminal command. No `aimakerspace` imports.

The skeleton is provided (package, CLI, arguments, `.env` loading, the `Hit` with a citation). What's missing are the five stages: eight functions with contracts and `NotImplementedError` in the body. You fill those in. The question isn't *"did you get an answer out of it?"* but:

> **"Which of your own questions does your app get wrong, and which stage is responsible?"**

> ⚠️ **This is not production-ready, and you're not being asked to make it one.** Every search is a plain Python loop over every vector — no persistence, auth, tests, eval, server, or deployment, on purpose. This week buys the thing that makes the real versions make sense: knowing which stage to blame.

<table>
  <tr>
    <td width="120"><strong>Outcome</strong></td>
    <td>A small app you wrote, that answers questions about a body of text from your terminal, which you have broken on purpose and improved in one measured way.</td>
  </tr>
  <tr>
    <td><strong>Tools</strong></td>
    <td>Python, NumPy, the OpenAI Python SDK, <code>uv</code>. Session 2's <code>aimakerspace/</code> is a reference to read, not a dependency.</td>
  </tr>
  <tr>
    <td><strong>Due</strong></td>
    <td>End of the week. Post your repo link and Loom in the Maven Community.</td>
  </tr>
  <tr>
    <td><strong>Before you start</strong></td>
    <td>Your AIE11 repo synced, <code>uv</code> installed, and an OpenAI key with a little credit on it.</td>
  </tr>
</table>

---

<!-- deliverables:start -->
## 🏗️ Build | 🚢 Ship | 📤 Share

**Build** is you can run it. **Ship** is someone else can run it and you see your errors. **Share** is someone who isn't you has an opinion about it.

### 🏗️ Build

`uv run python -m retrieval_app "..."` answers a question from the command line with grounded context, citing the chunks it came from. Four questions are asked inside the notebook as you work — *not graded*, just comprehension checks:

| # | Question | Asked in |
| :---: | --- | --- |
| 1 | `text-embedding-3-small` returns 1536 dimensions. Can you change that, and what technique makes it possible | S2 |
| 2 | What the `async` approach to collecting embeddings buys you, and whether it buys anything at 21 chunks | S2 |
| 3 | Which knobs on the OpenAI API make output more reproducible | S2 |
| 4 | Which prompting strategy produces a more thoughtful answer, and what it's called | S2 |

### 🚢 Ship — the graded stuff, all from the steps below

- [ ] **All eight stubs filled in**, so the command runs rather than raising `NotImplementedError`
- [ ] **Every answer cites its sources** (chunk or chapter)
- [ ] **One augmentation**, with the same ten questions re-run and before/after recorded
- [ ] **A diagram** of your pipeline. Hand drawn and photographed is fine, [mermaid](https://mermaid.ai) is better
- [ ] **`DECISIONS.md`**: what you changed, why, what would change it back
- [ ] It runs **from a clean terminal**, not just your kernel

### 📤 Share

- [ ] **A Loom (≤ 5 min)**: your app answering two questions, and your before/after
- [ ] **One real person asked three questions of it**, and what they said, in their words
- [ ] Your repo link posted in [our community on Maven](https://bit.ly/fde1-maven-community)
- [ ] A social post tagging **@AIMakerspace** with three lessons learned
<!-- deliverables:end -->

---

## Official documentation

Prefer these to blog posts and your agent's memory of them.

| Tool | What you use it for here | Docs |
| --- | --- | --- |
| OpenAI Embeddings | chunks into vectors; the `dimensions` parameter | [platform.openai.com — Embeddings](https://platform.openai.com/docs/api-reference/embeddings/create) |
| OpenAI Chat Completions | the answer call, and the `seed` / `temperature` knobs | [platform.openai.com — Chat](https://platform.openai.com/docs/api-reference/chat/create) |
| uv | `uv sync`, `uv add`, `uv run` | [docs.astral.sh/uv](https://docs.astral.sh/uv/) |

---

## Setting expectations

**Budget four to six hours** across the week. The functions are short; understanding *why* each has the signature it has is what takes the time.

| Step | What it is | Rough time |
| :---: | --- | --- |
| 1 | Run the notebook, then read it | 1–1.5 hrs |
| 2 | Fill in the five stages | 1.5–2 hrs |
| 3 | Write ten questions, find the failures | 45 min |
| 4 | Make one change, measure it | 1–2 hrs |
| 5 | Diagram and decision | 40 min |
| 6 | Show it to one person, and share | 30 min + their calendar |

> **Do Step 3 before Step 4.** Questions you wrote yourself turn Step 4 from "I added a feature" into "I fixed a failure I can point at." The other way round, you can't defend the augmentation.

---

## What you are building

Everything's in this folder. **✏️ is yours to write; ✅ is already done.**

```
00_Technical_Challenges/Week 1/
├── pyproject.toml          ✅ deps: numpy, openai, python-dotenv
├── .env.example            ✅ cp to .env, add your key
├── data/
│   └── HealthWellnessGuide.txt   ✅ the corpus that ships. 16,206 characters.
├── retrieval_app/
│   ├── __main__.py         ✅ the command line, wired to all five stages
│   ├── corpus.py           ✏️ load_corpus, split_corpus
│   ├── index.py            ✏️ embed_texts, cosine_similarity, build_index, search
│   └── answer.py           ✏️ build_messages, answer
├── DECISIONS.md            ✏️ what you changed, why, what would change it back
└── diagram.png             ✏️ your pipeline, drawn by you
```

Each stub has a docstring with arguments, return type, and a hint. **Read it before you write the body** — the signatures aren't arbitrary, and a couple quietly tell you something you'll need for Step 4.

> **Your coding agent is a teaching assistant here, not autocomplete.** The repo's [`AGENTS.md`](../../AGENTS.md) puts Claude Code and Codex into instructor mode: they explain, debug, and review, but decline to write your app. The code is a couple of hundred lines; the understanding is the assignment.

---

## Your corpus

`data/HealthWellnessGuide.txt` ships with this folder and everything below works on it — but you don't have to use it. Drop any `.txt` into `data/` and the app finds it:

```bash
rm data/HealthWellnessGuide.txt
cp ~/Downloads/my_own_notes.txt data/
# or keep both and pick:
uv run python -m retrieval_app "..." --corpus data/my_own_notes.txt
```

Pick something you actually want to ask questions of — your notes, a team handbook, board game rules, a transcript. Four requirements:

| Requirement | Why |
| --- | --- |
| **Plain `.txt`, utf-8** | `load_corpus` reads text. PDF parsing is a Step 4 augmentation, not a prerequisite |
| **10,000–50,000 characters** | under ~5k there aren't enough chunks for `k` to matter; over ~50k you can't eyeball what came back |
| **Facts it keeps in two places** | your "needs 2 chunks" question has to be writable at all |
| **A clear edge** | you need to know what it does *not* cover, or you can't write the decline question |

> ⚠️ **Don't pick something famous.** A corpus the model already memorised (Wikipedia, Python docs, Shakespeare) answers correctly even with retrieval broken, because the answer is in the model, not your chunks — so you lose the ability to attribute a failure to a stage. Obscure beats interesting.

---

## Step 1: Run the notebook, then read the library

```bash
cd 02_Dense_Vector_Retrieval
uv sync
cp .env.example .env     # then set OPENAI_API_KEY=sk-...
```

Open `Pythonic_RAG.ipynb`, **select `.venv` as your kernel**, run it top to bottom, and answer the four openers. Embed the corpus **once**; every query after pays **twice** — one embedding call for the question, one chat call for the answer. Then read the library you're about to reimplement:

| # | Open | Find |
| :---: | --- | --- |
| a | `text_utils.py` → `CharacterTextSplitter.split` | the loop steps by `chunk_size - chunk_overlap`, so the guide becomes **21 chunks**, and chunks are cut mid-word (*"tilting p..."*). Nothing here knows what a sentence is — which of your questions would that ruin? |
| b | `vectordatabase.py:18` | `defaultdict(np.array)` **keyed on the chunk's own text**; `search` scores *every* vector and sorts. What happens on kernel restart? What does this cost at 21 million chunks? |
| c | `vectordatabase.py` → `search` | returns the top `k`, always exactly `k`, **no threshold anywhere** — while the prompt tells the model to say *"I don't have information about that."* Ask about something the guide never heard of: whose job is it to notice nothing matched? |

---

## Step 2: Fill in the five stages

```bash
cd "00_Technical_Challenges/Week 1"
uv sync
cp .env.example .env     # then set OPENAI_API_KEY=sk-...
uv run python -m retrieval_app "What exercises help with lower back pain?"
```

That command already works and tells you the first thing you haven't written. Work in order — each file depends on the one before it, and finishing one moves the error along:

| File | Functions | Your check |
| --- | --- | --- |
| `corpus.py` | `load_corpus`, `split_corpus` | the chunk count matches the formula below |
| `index.py` | `embed_texts`, `cosine_similarity`, `build_index`, `search` | two similar sentences score high; two unrelated ones low |
| `answer.py` | `build_messages`, `answer` | an answer appears, with its sources listed |

Session 2's `aimakerspace/` has a version of most of these. **Reading it and writing your own is the assignment. Pasting it in is not** — you'll explain this code in a Loom. Three things the skeleton decided for you:

1. **It runs outside Jupyter**, so no `nest_asyncio` and no `async`. Work out why a script doesn't need them.
2. **Every answer cites its sources.** `Hit` has a `chunk_id`; `__main__.py` prints a citation per hit. An untraceable answer is usually something the LLM made up.
3. **The command prints its trace** to `stderr` (corpus, chunk count, index time, total). A fresh process holds no vectors, so it re-embeds every chunk on **every question** — watch that number.

> **`search` returns "up to `k`" hits, not exactly `k`.** The signature isn't stopping you from returning fewer, or none.

### Does my splitter work?

The app prints two numbers to check against each other:

```
corpus HealthWellnessGuide.txt: 16,206 characters -> 21 chunks
```

A loop stepping by `chunk_size - chunk_overlap` over N characters gives `ceil(N / (chunk_size - chunk_overlap))` chunks. Defaults 1000/200 → step 800:

| Corpus | Expected on defaults |
| --- | --- |
| 16,206 chars (shipped guide) | `ceil(16206/800)` = **21** |
| 10,000 chars | 13 |
| 40,000 chars | 50 |

Doesn't match? That's your bug, found before you've spent a cent on embeddings.

**✅ Deliverables:** all 8 stubs filled in and running from a clean terminal;

---

## Step 3: 10 questions, what fails?

| Kind | What it has to do | Example |
| --- | --- | --- |
| **Lookup** | one fact, one chunk. The easy case | "How many minutes of aerobic activity per week?" |
| **Needs 2 chunks** | two facts your corpus keeps apart. Does `k=3` reach both? | "What should my morning *and* evening routine look like?" |
| **Decline** | something your corpus doesn't cover. **Correct answer is a refusal** | "What dose of ibuprofen for a migraine?" |

Run all 10. ✅/❌ with **one line naming a stage, not a mood**:

```markdown
| # | Question | ✅/❌ | What went wrong, where |
|---|----------|------|------------------------|
| 1 | Aerobic activity per week? | ✅ | top chunk was Chapter 1. clean |
| 2 | Morning and evening routine? | ❌ | retrieval — 3 morning chunks, 0 evening. k too small |
| 3 | Ibuprofen dose for a migraine? | ❌ | returned 3 headache chunks. model answered from them |
```

"Wrong chunk retrieved", "right chunk, model ignored it", "chunk cut in half" are 3 different bugs with 3 different fixes. **The skill is telling them apart** — which means reading the retrieved chunks and scores, not just the answer.

> Expect 3–5 failures out of 10. 10/10 means your questions were too kind; 2/10, check your key and chunk count before blaming the technique.

---

## Step 4: One change, measure it

Pick **one** — and pick the one that **fixes a failure from Step 3.** It's not about size; it's that you can name the failure it was for and show the numbers either side.

| Augmentation | What failure it targets | Size |
| --- | --- | --- |
| **Score threshold, so `search` can return nothing** | decline question answered from irrelevant chunk | a few lines in `search` |
| **Tune `chunk_size`/`chunk_overlap`** | chunks cut mid-word, incomplete answers | 2 numbers |
| **Raise or lower `k`** | questions that need 2 chunks but got 1 | 1 number |
| **Save index to disk** (`np.save` + chunks) | re-embedding every chunk, every command | load-or-build branch |
| **Fewer `dimensions` or different model** | cost, speed. Ties to opener #1 | 1 API argument |
| **Rewrite prompt** in `build_messages` | model ignoring context, or answering anyway | free. Often most effective |


> **"My score didn't move"** is a finding. Write what you expected, what happened, and your best explanation for the gap. A documented null result beats a vague improvement.

**✅ Deliverables:** the augmentation working in your app; before/after on your 10 questions including regressions; a one-paragraph vibe check — does it *feel* better, and does that match the numbers?

---

## Step 5: Diagram, decision

**Diagram** — paper, drawing app, or a Mermaid block, not a box labeled "RAG". Draw the 5 stages and what flows on each arrow (string, list of strings, `(n_chunks, 1536)` matrix, list of `Hit`s, messages, string). Mark the 2 arrows that call OpenAI, and where your Step 4 change sits. If you can't draw it without opening your code, you just found the part you don't understand yet.

**Decision** in `DECISIONS.md` — 3 short answers, not an essay:

| Field | What it means |
| --- | --- |
| **What I changed** | Your augmentation. 1 sentence |
| **Why** | Which of your 10 failures it targeted. Before/after |
| **What would change my mind** | The condition under which you'd undo it |

That third one is what everybody skips and gets asked about. *"I added a 0.25 score floor so search can return nothing. Fixed my decline question. Cost me 1 true answer at 0.23. I'd raise the floor if users saw confident answers from bad chunks; drop it if the corpus grew enough that everything scored lower"* is an engineering position. *"Threshold is better"* is a preference.

**✅ Deliverables:** the diagram (data types on arrows, paid calls marked); `DECISIONS.md` with all 3 fields.

---

## If it's blocked

- **`No OPENAI_API_KEY found`** — Did you `cp .env.example .env` **in this folder** and add your key (no quotes, no spaces around `=`)? And does the key have credit? Zero balance fails at *request*, not auth.
- **`No module named retrieval_app` / `openai`** — `python -m` searches your current directory, so run from `00_Technical_Challenges/Week 1/` with `uv run python -m ...`. Plain `python` lacks the deps; run `uv sync` if you haven't.
- **Chunk count is wrong** — `split_corpus` should step by `chunk_size - chunk_overlap`; stepping by `chunk_size` gives too few, by `chunk_overlap` far too many. Check against `ceil(characters / (chunk_size - chunk_overlap))`.
- **Retrieval returns nothing useful / scores 0.3–0.5** — Run `--show-chunks` and read what came back. Those absolute scores are normal for cosine over prose; the **gap** between top hit and 4th hit is what matters, and what you choose a threshold against.
- **Every score is 1.000** — You're comparing a vector to itself, or `build_index` and `search` use different embedding models. A query embedded with a different model than the index **fails silently** — the most common silent bug here.
- **It answers my decline question anyway** — Expected; the most common failure in deployed RAG. `search` isn't obliged to return `k` hits, and your prompt isn't obliged to answer. Which should own it?

---

## Your final submission

Sync your fork first, then commit and push:

```bash
git checkout main && git pull upstream main && git push origin main
```

Post **your repo link and Loom** in [Maven](https://maven.com/aimakerspace/ai-eng-bootcamp/11/home). Your repo should contain your runnable app plus, `DECISIONS.md`, and your diagram, all in `00_Technical_Challenges/Week 1/`. **After the deadline, comment on at least 2 other students' submissions** — read their `DECISIONS.md` and leave something specific.

> **Never commit secrets.** `.env` is gitignored for a reason. Run `git diff --staged` before you push. A key in a public repo is scraped in minutes, and deleting the commit doesn't help — rotate it.

---

Everything after this week assumes you have an app that answers from your data, can say where the answer came from, and that you know which stage to look at when an answer is wrong. **That's the whole deliverable.**
