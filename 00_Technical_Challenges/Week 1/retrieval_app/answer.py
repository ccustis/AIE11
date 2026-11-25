"""Stage 5: turn retrieved chunks into an answer.

YOUR CODE GOES HERE. The prompt is yours to write — it is the cheapest thing
in the pipeline to change and often the most effective.
"""

from .index import Hit, client

CHAT_MODEL = "gpt-4.1-mini"


def build_messages(question: str, hits: list[Hit]) -> list[dict]:
    """Assemble the messages list sent to the chat model.

    Args:
        question: the user's question.
        hits: what search() returned. May be empty.

    Returns:
        A list of {"role": ..., "content": ...} dicts — a system message
        setting the rules, and a user message carrying the context and the
        question.

    Three things your prompt has to decide, and they are real decisions:
      1. How do you label each chunk in the context so the model can refer to
         it? (hit.chunk_id exists for this.)
      2. What should it do when the context does not contain the answer? Say
         so explicitly, or it will answer from the nearest chunk regardless.
      3. What happens when `hits` is empty? Write that branch deliberately.

    Hint: Session 2's RAG_SYSTEM_TEMPLATE is a good starting point, and a
    better one once you have read Step 3's failures and edited it.
    """
    if hits:
        context = "\n\n".join(
            f"[chunk {hit.chunk_id}] (score {hit.score:.3f})\n{hit.text}"
            for hit in hits
        )
    else:
        context = "(no passages were retrieved)"

    system = (
        "You are a personal wellness assistant. Answer only from the retrieved "
        "passages. Each passage is already labeled with its chunk id; cite those "
        "ids, such as [chunk 4], and do not renumber them as Source 1, Source 2. "
        "If the passages do not contain the answer, or if no passages were "
        "retrieved, say: I don't have information about that in the wellness guide. "
        "Do not fill the gap from outside knowledge. Keep the answer concise, and "
        "remind the reader to consult a healthcare professional for medical advice."
    )
    user = (
        f"Retrieved passages:\n{context}\n\n"
        f"Question: {question}\n\n"
        "Answer using only the passages above, and cite the chunk ids you used."
    )
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]


def answer(question: str, hits: list[Hit]) -> str:
    """Call the chat model and return its reply as a string.

    Hint: `client().chat.completions.create(model=CHAT_MODEL, messages=...)`,
    then dig out `.choices[0].message.content`. Look up what `temperature`
    does to your results when you run the same question twice.
    """
    response = client().chat.completions.create(
        model=CHAT_MODEL,
        messages=build_messages(question, hits),
        temperature=0,
    )
    return response.choices[0].message.content or ""
