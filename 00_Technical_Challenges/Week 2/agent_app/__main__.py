"""`python -m agent_app` -> load the key, start the server. Written for you.

    uv run python -m agent_app                 # http://127.0.0.1:8000
    uv run python -m agent_app --port 9000      # pick another port

Open http://127.0.0.1:8000/docs to try /ask without a frontend at all.
"""

import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="agent_app", description=__doc__)
    parser.add_argument("--host", default="127.0.0.1", help="interface to bind (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8000, help="port to serve on (default: 8000)")
    parser.add_argument("--reload", action="store_true", help="auto-reload on code changes (dev)")
    args = parser.parse_args(argv)

    # Load OPENAI_API_KEY from the .env next to this package, before anything imports the client.
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
    if not os.environ.get("OPENAI_API_KEY"):
        print("No OPENAI_API_KEY found.", file=sys.stderr)
        print("  cp .env.example .env    then put your key in it", file=sys.stderr)
        return 2

    import uvicorn

    uvicorn.run("agent_app.api:app", host=args.host, port=args.port, reload=args.reload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
