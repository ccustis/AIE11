"""The command line. This file is written for you: read it, don't rewrite it.

    uv run python -m retrieval_app "your question here"
    uv run python -m retrieval_app "..." --corpus data/my_own_notes.txt

It is already wired to all five stages. Right now it stops at the first
NotImplementedError and tells you which file to open. Fill in the stubs in
corpus.py, then index.py, then answer.py, and this same command starts working.
"""

import argparse
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv

from . import answer as answer_stage
from . import corpus as corpus_stage
from . import index as index_stage

APP_DIR = Path(__file__).resolve().parent
DATA_DIR = APP_DIR.parent / "data"


def find_corpus() -> tuple[Path | None, list[Path]]:
    """Find the .txt file to search, whatever it happens to be called.

    Swapping corpora is meant to be a file drop, not a code edit: put your own
    .txt in data/ and this finds it. Two files in there and it will not guess
    which you meant, so it asks for --corpus instead.

    Returns:
        (the corpus, every .txt found). The first is None when there is not
        exactly one candidate, and then the caller explains what to do.
    """
    found = sorted(DATA_DIR.glob("*.txt"))
    return (found[0] if len(found) == 1 else None), found


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="retrieval_app", description=__doc__)
    parser.add_argument("question", help="the question to answer")
    parser.add_argument("-k", type=int, default=3, help="how many chunks to retrieve (default: 3)")
    parser.add_argument("--corpus", type=Path, default=None, help="the .txt file to search (default: the one in data/)")
    parser.add_argument("--show-chunks", action="store_true", help="print the retrieved text, not just the citations")
    args = parser.parse_args(argv)

    # Load OPENAI_API_KEY from the .env file next to this package.
    load_dotenv(APP_DIR.parent / ".env")
    if not os.environ.get("OPENAI_API_KEY"):
        print("No OPENAI_API_KEY found.", file=sys.stderr)
        print("  cp .env.example .env    then put your key in it", file=sys.stderr)
        return 2

    corpus_path = args.corpus
    if corpus_path is None:
        corpus_path, found = find_corpus()
        if corpus_path is None:
            if not found:
                print(f"No .txt file in {DATA_DIR}/", file=sys.stderr)
                print("  Put one there, or point at it with --corpus", file=sys.stderr)
            else:
                print(f"More than one .txt in {DATA_DIR}/ - say which one:", file=sys.stderr)
                for candidate in found:
                    print(f"  --corpus data/{candidate.name}", file=sys.stderr)
            return 2
    if not corpus_path.is_file():
        print(f"No such corpus file: {corpus_path}", file=sys.stderr)
        return 2

    started = time.perf_counter()

    text = corpus_stage.load_corpus(corpus_path)
    chunks = corpus_stage.split_corpus(text)
    # Both numbers are printed on purpose. Your chunk count is checkable from
    # the character count: see "Does my splitter work?" in the README.
    print(f"corpus {corpus_path.name}: {len(text):,} characters -> {len(chunks)} chunks", file=sys.stderr, flush=True)

    matrix = index_stage.build_index(chunks)
    indexed = time.perf_counter()
    print(f"indexed in {indexed - started:.2f}s", file=sys.stderr, flush=True)

    hits = index_stage.search(args.question, chunks, matrix, k=args.k)
    reply = answer_stage.answer(args.question, hits)

    print(f"\nQ: {args.question}\n")
    print(reply)

    # Every answer names its sources. This is not decoration: an answer a user
    # cannot trace is a rumour, and in Week 4 you debug wrong answers by chunk.
    print("\nSources:")
    if not hits:
        print("  (none retrieved)")
    for hit in hits:
        print(f"  {hit.citation()}")
        if args.show_chunks:
            print(f"      {' '.join(hit.text.split())[:400]}...")

    sys.stdout.flush()
    print(f"\ntotal {time.perf_counter() - started:.2f}s", file=sys.stderr, flush=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except NotImplementedError as exc:
        print(f"\n  Not written yet: {exc}\n", file=sys.stderr)
        print("  Start with corpus.py, then index.py, then answer.py.", file=sys.stderr)
        raise SystemExit(1)
