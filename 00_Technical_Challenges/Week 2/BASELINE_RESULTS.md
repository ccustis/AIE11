# Technical Challenge 2 — Baseline Evaluation Results

**Project:** AIE11 · Week 2 · Agentic-RAG Search Service  
**Evaluation stage:** Baseline, **before augmentation**  
**Test interface:** FastAPI interactive docs (`POST /ask` at `http://127.0.0.1:8000/docs`)  
**Corpus:** `data/HealthWellnessGuide.txt`  
**Request parameter submitted:** `k = 3` for every question  
**Evidence:** The API responses, retrieved source identifiers/previews, and execution traces captured during tests 1–10

> **Scope of these results.** These are observations from one run of each question, not a statistical estimate of reliability. Tool behavior may vary across runs. The application currently reports source similarity scores as `0.0` placeholders; these are **not** retrieval-quality measurements. There were no recorded latency, token-usage, or dollar-cost measurements. An API response containing sources means the corresponding passages were retrieved, not necessarily that each passage supports every claim in the answer.

## Executive summary

| Classification | Count | Tests |
|---|---:|---|
| **Pass** — primary expected behavior observed | **8** | 1, 2, 3, 4, 5, 6, 8, 10 |
| **Fail** — a required factual answer was missed | **1** | 7 |
| **Ambiguous / routing concern** — answer appropriate, retrieval questionable | **1** | 9 |
| **Total** | **10** | 1–10 |

**Primary finding:** A compound hydration-and-sleep question (Test 7) retrieved relevant material on both topics but missed the chunk containing the guide's explicit **7–9 hours of sleep** recommendation. The agent incorrectly concluded that the guide contained no numeric recommendation. A follow-up sleep-only question (Test 8) retrieved chunk **17** and answered correctly. This points to **retrieval coverage for compound questions** and **overconfident conclusions from incomplete retrieval** as distinct, related weaknesses.

**Secondary finding:** A stock-price question phrased as “According to the wellness guide…” (Test 9) triggered an irrelevant wellness search, while essentially the same question without that framing (Test 10) did not. Because the wording explicitly requested the guide, the appropriateness of the Test 9 search is **ambiguous**, but its sources did not substantiate any stock-price claim.

## Test-by-test record

| # | Question submitted | Expected behavior | Observed behavior | Retrieved chunk IDs | Classification |
|---:|---|---|---|---|---|
| **1** | What is 125 times 8? | Answer **1,000**, without retrieval | Correct answer; `used_retrieval=false`; `sources=[]`; no tool call | None | **Pass** |
| **2** | According to the wellness guide, how many minutes of moderate-intensity aerobic activity should adults aim for each week? | Retrieve and report **at least 150 minutes/week** | Correct answer; `used_retrieval=true`; trace showed search → result → final answer | **1, 9, 44** | **Pass** |
| **3** | According to the wellness guide, what dose of ibuprofen should I take for a migraine? | Do not invent or recommend an unsupported dosage | Agent searched the guide and explicitly said it does **not** provide an ibuprofen dose; offered general caution | **32, 44, 31** | **Pass** |
| **4** | According to the wellness guide, what should a healthy morning routine and evening routine include? | Retrieve supporting material for **both** routines | Correctly synthesized morning routine from chunk 29, evening routine from chunk 30, and habit-building context from chunk 28 | **29, 28, 30** | **Pass** |
| **5** | According to the wellness guide, what clinical trial proves that lavender essential oil cures migraines? Provide the study name, publication year, and supporting source. | Reject unsupported claim; do not fabricate a study | Agent correctly said no clinical trial, year, or evidence of a cure was given; included a marginally relevant source | **32, 31, 30** | **Pass**, citation-quality observation |
| **6** | Hello! Can you briefly introduce yourself and explain what kinds of questions you can help me answer? | Respond conversationally; do not retrieve | Appropriate introduction; `used_retrieval=false`; `sources=[]` | None | **Pass** |
| **7** | According to the wellness guide, what are the daily recommendations for hydration and sleep? Identify the evidence supporting each recommendation. | Retrieve and report **8 glasses (64 oz)** of water and **7–9 hours** of sleep, with support for both | Correct hydration result, but incorrectly claimed guide gives **no specific sleep hours**; numeric sleep chunk not retrieved | **16, 15, 18** | **Fail** |
| **8** | According to the wellness guide, how many hours of sleep per night are recommended for adults? | Retrieve **7–9 hours** and substantiate it | Correct answer with chunk 17 explicitly containing the numeric recommendation | **17, 19, 18** | **Pass** |
| **9** | According to the wellness guide, what was the closing price of Apple stock yesterday? | Do not invent financial data; ideally avoid irrelevant wellness retrieval | Correctly declined to state a stock price but invoked wellness search, returning irrelevant apple/food and digital-wellness passages | **14, 29, 41** | **Ambiguous / routing concern** |
| **10** | What was the closing price of Apple stock yesterday? | Recognize unavailable out-of-scope data and avoid wellness retrieval | Correctly declined to supply live market data; `used_retrieval=false`; `sources=[]` | None | **Pass** |

## Detailed findings and trace notes

### Test 1 — Arithmetic without retrieval — PASS
- **Final answer:** 1,000.
- **Retrieval:** `false`; **sources:** empty.
- **Trace:** One agent response, without tool invocation.
- **Stage assessed:** Model tool-selection / routing. No unnecessary search observed.

### Test 2 — Exercise recommendation — PASS
- **Final answer:** At least 150 minutes of moderate-intensity aerobic activity per week.
- **Retrieval:** `true`; **sources:** chunks **1, 9, 44**.
- **Trace:** Agent requested `search_wellness_knowledge`; tool returned guide excerpts; agent answered.
- **Evidence assessment:** Chunk 1 contained the relevant 150-minute recommendation.
- **Stage assessed:** Retrieval selection, evidence retrieval, and source parsing.

### Test 3 — Medication dosage beyond the corpus — PASS
- **Final answer:** The guide does **not** give an ibuprofen dose for migraines; it lists non-pharmacologic headache remedies and advises appropriate professional/label guidance.
- **Retrieval:** `true`; **sources:** chunks **32, 44, 31**.
- **Trace:** One wellness search followed by a final response.
- **Evidence assessment:** Chunk 32 lists headache remedies; chunk 31 describes headache triggers. No invented dosage was given. Chunk 44 is general wellness context rather than direct dosage evidence.
- **Stage assessed:** Knowing when retrieved material is insufficient to justify an answer.

### Test 4 — Morning plus evening routine — PASS
- **Final answer:** A combined morning and evening routine supported by guide passages.
- **Retrieval:** `true`; **sources:** chunks **29, 28, 30**.
- **Trace:** One search, then synthesis.
- **Evidence assessment:** Chunk 29 describes morning habits; chunk 30 describes evening wind-down; chunk 28 describes habit-building.
- **Stage assessed:** Combining evidence from multiple chunks.

### Test 5 — Unsupported lavender clinical-trial claim — PASS WITH CITATION-QUALITY OBSERVATION
- **Final answer:** The guide names **no clinical trial**, **no publication year**, and **no evidence proving a migraine cure**; it only mentions lavender among possible natural headache remedies.
- **Retrieval:** `true`; **sources:** chunks **32, 31, 30**.
- **Trace:** Search → returned excerpts → evidence-limited response.
- **Evidence assessment:** Chunk 32 mentions lavender; chunk 31 gives headache context. Chunk 30 concerns evening routines and only brushes against the headache section; it does not substantively support the claim.
- **Stage assessed:** Grounded refusal was successful; returning all retrieved passages as citations can reduce citation precision.

### Test 6 — Greeting / capabilities — PASS
- **Final answer:** A wellness-assistant introduction and description of areas it supports.
- **Retrieval:** `false`; **sources:** empty.
- **Trace:** One agent response, no tool invocation.
- **Stage assessed:** Avoiding unnecessary retrieval for conversational turns.

### Test 7 — Hydration and sleep combined — FAIL
- **Final answer:** Correctly reported **8 glasses (64 ounces)** of water, but incorrectly stated that the guide **does not specify the number of hours of sleep**.
- **Retrieval:** `true`; **sources:** chunks **16, 15, 18**.
- **Trace:** One combined query: `daily recommendations for hydration and sleep; identify the evidence supporting each recommendation`.
- **Evidence assessment:** Chunk 15 contains the hydration number, chunk 16 covers hydration tips and sleep background, and chunk 18 covers sleep-hygiene practices. None of those returned chunks included the explicit **7–9 hours** passage found later in chunk 17.
- **Likely failure stages:** Retrieval coverage / chunk ranking for multi-topic query; answer formation also overclaimed what could be concluded from limited results.
- **Concrete correction target:** Recover chunk 17 (or equivalent explicit duration evidence) for this compound question and use it in the answer.

### Test 8 — Sleep question alone — PASS
- **Final answer:** Adults typically need **7–9 hours per night**.
- **Retrieval:** `true`; **sources:** chunks **17, 19, 18**.
- **Trace:** Focused query: `recommended hours of sleep per night for adults`.
- **Evidence assessment:** Chunk **17** explicitly states the 7–9-hour guidance.
- **Diagnostic significance:** Compared with Test 7, a more focused query successfully found the needed passage. This strengthens the case for experimenting with multi-topic retrieval coverage, though it does not prove the sole cause of the failure.

### Test 9 — Stock question phrased as a guide query — AMBIGUOUS / ROUTING CONCERN
- **Final answer:** Correctly said the wellness guide does not cover stock prices; no price was invented.
- **Retrieval:** `true`; **sources:** chunks **14, 29, 41**.
- **Trace:** Agent called the wellness search tool with query `Apple stock closing price yesterday`.
- **Evidence assessment:** Chunk 14 refers to eating an *apple*; chunks 29 and 41 contain routine and digital-wellness content. None concerns financial markets.
- **Interpretation:** This is an unnecessary search under a strict out-of-scope routing policy, but because the user explicitly asked *according to the wellness guide*, consulting the guide can be seen as reasonable verification. Marked **ambiguous** rather than a definitive failure.

### Test 10 — Direct stock-price question — PASS
- **Final answer:** Agent said it could not look up live market data and directed the user to market-data sources, without inventing a number.
- **Retrieval:** `false`; **sources:** empty.
- **Trace:** One agent response without tool invocation.
- **Diagnostic significance:** Removing the phrase *according to the wellness guide* changed routing behavior versus Test 9.

## Candidate improvements — NOT YET IMPLEMENTED

1. **Primary candidate: multi-topic retrieval coverage.** Test a retrieval augmentation that can issue focused searches for separable sub-questions (for example, hydration and sleep), merge results, deduplicate by `chunk_id`, and preserve the existing `[source chunk_id=... score=...]` contract. Compare whether Test 7 starts retrieving the explicit **7–9-hour** passage and whether the answer improves. Evaluate added tool calls, latency, and API cost if measured.
2. **Alternative: source relevance / evidence filtering.** Test whether the service can avoid displaying tangentially related chunks (as in Test 5) while retaining chunks that support factual claims.
3. **Alternative: out-of-scope routing.** Introduce a clearly defined scope decision and evaluate Test 9 alongside Test 10. Avoid treating Test 9 as conclusive evidence of a bug without clarifying the intended policy.

**Important:** The challenge requires selecting **one** augmentation based on baseline evidence, rerunning **all the same 10 questions**, and recording any gains, regressions, or null results. Do not report a post-augmentation improvement until it has been measured.

## Re-evaluation protocol (after the augmentation)

- Keep the **same 10 question wordings** and submit `k=3` again to `POST /ask`.
- For each response, record: correctness, `used_retrieval`, returned `chunk_id` values, tool-call count/sequence from `trace`, and any unsupported or missing claims.
- Compare each result to this baseline. Give special attention to Tests **5, 7, 8, 9, 10**, since those best distinguish source quality, coverage, and routing.
- Count any new failures as **regressions**, even if Test 7 improves.
- If possible, measure wall-clock latency and request/tool counts in both versions. These were **not captured** in this baseline, so a quantitative cost or latency comparison cannot be made retrospectively.
- Save the final choice, evidence, tradeoffs, and reversal criteria in `DECISIONS.md`.

## Submission checklist associated with this evaluation

- [x] Run notebook exercises and answer Questions #1–#4.
- [x] Implement the five missing functions.
- [x] Confirm `/health` reports `{"status":"ok","agent_ready":true}`.
- [x] Confirm basic direct-answer and retrieval flows through `POST /ask`.
- [x] Complete the 10-question baseline and identify shortcomings.
- [ ] Implement **one** evidence-motivated augmentation.
- [ ] Rerun all 10 questions and record before/after outcomes and regressions.
- [ ] Build original frontend showing answer and sources.
- [ ] Create architecture diagram and complete `DECISIONS.md`.
- [ ] Verify app works from a clean terminal; review staged Git diff for secrets; push to personal fork.
- [ ] Have a real person ask three questions and capture their feedback in their own words.
- [ ] Record ≤5-minute Loom, share repo and Loom in Maven, and post three lessons learned tagging `@AIMakerspace`.
