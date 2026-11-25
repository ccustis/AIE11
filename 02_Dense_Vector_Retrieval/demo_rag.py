"""Command-line demonstration for the AIE11 Pythonic RAG Build + Ship activity.

Place this file in 02_Dense_Vector_Retrieval and run, from a fresh terminal:
    uv sync
    uv run --env-file .env python demo_rag.py

This script reuses the course's text loader, splitter, vector database, and ChatOpenAI
wrappers, but runs independently of any Jupyter kernel. OpenAI API credits are used.
"""

import asyncio
import os
from pathlib import Path

from aimakerspace.text_utils import CharacterTextSplitter, TextFileLoader
from aimakerspace.vectordatabase import VectorDatabase
from aimakerspace.openai_utils.chatmodel import ChatOpenAI
from aimakerspace.openai_utils.prompts import SystemRolePrompt, UserRolePrompt


QUESTION_1 = "What are some natural remedies for improving sleep quality?"
QUESTION_2 = "What exercises help with lower back pain?"
SOURCE_NAME = "HealthWellnessGuide.txt"


class MetadataVectorDatabase(VectorDatabase):
    """Attach filename and chunk index to retrieved text without changing the vectors."""

    def __init__(self, existing_db):
        super().__init__(embedding_model=existing_db.embedding_model)
        self.vectors = existing_db.vectors
        self.chunk_metadata = {}

    def add_source_metadata(self, chunks, source_name):
        for index, chunk in enumerate(chunks, start=1):
            if chunk in self.vectors:
                self.chunk_metadata[chunk] = {
                    "source": source_name,
                    "chunk_id": index,
                }

    def search_by_text(self, query, k=3):
        results = super().search_by_text(query, k=k)
        enriched_results = []
        for text, score in results:
            info = self.chunk_metadata.get(text, {})
            source = info.get("source", "Unknown")
            chunk_id = info.get("chunk_id", "Unknown")
            enriched_results.append(
                (f"[Source: {source} | Chunk: {chunk_id}]\n{text}", score)
            )
        return enriched_results


SYSTEM_PROMPT = SystemRolePrompt(
    "You are a helpful personal wellness assistant. Answer only from the "
    "provided document passages. If they do not support an answer, say so. "
    "Keep your answer concise and cite the provided source labels. "
    "Remind users to consult a professional when medical advice is relevant."
)
USER_PROMPT = UserRolePrompt(
    "Relevant document passages:\n{context}\n\nQuestion: {question}\n"
    "Answer using only the document passages above."
)


def answer_question(db, llm, question, k=3):
    results = db.search_by_text(question, k=k)
    context = "\n\n".join(
        f"[Source {index}]: {passage}"
        for index, (passage, score) in enumerate(results, start=1)
    )
    response = llm.run(
        [
            SYSTEM_PROMPT.create_message(),
            USER_PROMPT.create_message(context=context, question=question),
        ]
    )
    return response, results


def print_answer(title, question, answer):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")
    print(f"Question: {question}\n")
    print(answer)


def main():
    folder = Path(__file__).resolve().parent
    os.chdir(folder)

    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit(
            "OPENAI_API_KEY is missing. Run with: uv run --env-file .env python demo_rag.py"
        )

    if not (folder / "data" / SOURCE_NAME).exists():
        raise SystemExit(f"Missing source document: data/{SOURCE_NAME}")

    print("AIE11 — Week 1 RAG Command-Line Demonstration")
    print("Loading wellness guide, splitting passages, and building embeddings...")
    documents = TextFileLoader(f"data/{SOURCE_NAME}").load_documents()
    chunks = CharacterTextSplitter().split_texts(documents)
    original_db = asyncio.run(VectorDatabase().abuild_from_list(chunks))

    enhanced_db = MetadataVectorDatabase(original_db)
    enhanced_db.add_source_metadata(chunks, source_name=SOURCE_NAME)
    llm = ChatOpenAI()

    # Question 1: original vs enhanced, same source material and question.
    original_answer, original_results = answer_question(original_db, llm, QUESTION_1)
    enhanced_answer, enhanced_results = answer_question(enhanced_db, llm, QUESTION_1)

    print_answer("QUESTION 1 — ORIGINAL", QUESTION_1, original_answer)
    print_answer("QUESTION 1 — WITH SOURCE METADATA", QUESTION_1, enhanced_answer)

    print(f"\n{'=' * 68}\nBEFORE / AFTER RETRIEVAL CHECK\n{'=' * 68}")
    for i, ((text_before, score_before), (text_after, score_after)) in enumerate(
        zip(original_results, enhanced_results), start=1
    ):
        meta_label, _, underlying_text = text_after.partition("\n")
        same_passage = text_before == underlying_text
        print(f"Result {i}: {meta_label}")
        print(
            f"  Passage unchanged: {same_passage} | "
            f"Original score: {float(score_before):.3f} | "
            f"Enhanced score: {float(score_after):.3f}"
        )

    # Question 2: the enhanced app answering a different question.
    second_answer, _ = answer_question(enhanced_db, llm, QUESTION_2)
    print_answer("QUESTION 2 — WITH SOURCE METADATA", QUESTION_2, second_answer)

    print(f"\n{'=' * 68}\nDEMO COMPLETE\n{'=' * 68}")
    print("Finding: source information is visible during retrieval, but the model")
    print("may still cite generic 'Source 1' labels in its final answer.")


if __name__ == "__main__":
    main()
