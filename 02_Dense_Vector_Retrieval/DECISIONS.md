# Week 1 — RAG Design Decisions

## Context

For the AI Makerspace Week 1 technical challenge, I built the `Pythonic_RAG.ipynb` wellness assistant. The baseline pipeline loads a text guide, splits it into chunks, creates embeddings, retrieves relevant passages with similarity search, and uses those passages to inform a language-model answer. Activity #1 called for an enhancement and comparison with the baseline.

## Decision 1 — Add source metadata, rather than change the embedding model or distance metric

**What changed:** I extended the in-memory vector database with a mapping from passage text to the source filename and chunk number. The enhanced retrieval path adds these details to each returned passage.

**Why:** I wanted to test whether information that is traceable *inside* a retrieval system becomes more transparent *in the final answer*. This also kept the experiment focused: the underlying embedding model, vectors, and similarity-search method remained the same.

**What would change this decision:** I would replace or rework this approach if the system ingested multiple documents, if chunks could contain duplicate text, if metadata needed filtering or persistence, or if source references proved incorrect. A production version should store structured metadata using stable chunk IDs instead of a text-keyed in-memory dictionary.

**How to reverse it:** Use the original `VectorDatabase` and `rag_pipeline` without the `MetadataVectorDatabase` wrapper. The original pipeline is preserved for comparison.

## Decision 2 — Reuse existing embeddings

**What changed:** I reused the vectors from the baseline database rather than generating a second set of document embeddings.

**Why:** This avoids extra embedding calls and helps isolate the effect of adding source information.

**What would change this decision:** I would re-embed if the chunking strategy, source content, embedding model, or dimensionality changed. Both original and enhanced pipelines must then use compatible query and document embeddings.

## Decision 3 — Compare both retrieval and final answers

**What changed:** I asked both pipelines the same sleep-related question and compared the top three passages, their ranking and scores, and the generated answers.

**Why:** A metadata change can work in retrieval without changing what readers see. Evaluating only the final answer would miss that distinction.

**Observed results:** All three retrieved passages matched and were ranked identically. Differences in similarity scores were very small (approximately 0.00002–0.00007). The answers covered essentially the same recommendations; the enhanced answer still used generic source labels rather than explicit filenames and chunk identifiers.

**What would change this decision:** Before claiming a measurable improvement in answer quality, I would test more queries, include known-answer evaluations, check citations against source text, control generation variability where possible, and measure latency and cost. A future design could explicitly format citations from the retrieved metadata in application code instead of relying on the model to reproduce them.

## Decision 4 — Keep this as a learning prototype

**What changed:** Source metadata is attached in memory for a single known guide, without a persistent metadata store or multi-document ingestion.

**Why:** This is sufficient to demonstrate the design tradeoff in the assignment without introducing unrelated complexity.

**What would change this decision:** If the pipeline became a user-facing application or handled many sources, I would add persistent metadata, stable document/chunk identifiers, source validation, update/delete handling, and automated tests.

## Main learning

Adding source details made retrieved material easier to inspect, but it did not automatically produce more transparent final citations. Retrieval traceability and user-facing transparency are separate design and evaluation questions.

## Reproducibility

Run the notebook from the `02_Dense_Vector_Retrieval` directory in a newly opened terminal, after `uv sync` and with a valid `OPENAI_API_KEY` in the local, ignored `.env` file. A full clean-terminal execution must be confirmed on the local machine; success in an existing Jupyter kernel alone is not sufficient.
