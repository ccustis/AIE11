"""Stage 1: load, split, embed the corpus, and hand back a retriever.

YOUR CODE GOES HERE. `build_retriever` raises NotImplementedError.

You did all of this in the Session 4 notebook (`Agentic_RAG_From_Scratch.ipynb`,
Task 4). Two differences here:
  - `api.py` calls this exactly once, in the FastAPI lifespan, and holds the retriever for
    the life of the process — never once per request (Week 1's CLI re-embedded every run).
  - Qdrant is **on disk**, not `:memory:`. It memory-maps its files, so the collection
    survives restarts — you embed once, ever, and later boots load from disk for free.
"""

from pathlib import Path

from langchain_core.retrievers import BaseRetriever
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient, models
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
QDRANT_PATH = Path(__file__).resolve().parent.parent / "qdrant_storage"  # on-disk, gitignored

# gpt-5.4-mini: newest-gen, strong tool-calling, fast + cheap for repeated runs.
# (gpt-5.6-luna/terra are reasoning-only and can't tool-call over chat completions.)
CHAT_MODEL = "gpt-5.4-mini"
EMBEDDING_MODEL = "text-embedding-3-small"


def build_retriever(corpus_path: Path, k: int = 3) -> BaseRetriever:
    """Load the corpus, split it, embed it into Qdrant, and return a retriever.

    Args:
        corpus_path: the .txt file to index.
        k: how many chunks the retriever returns per query.

    Returns:
        A LangChain retriever (`vector_store.as_retriever(...)`) ready to `.invoke(query)`.

    The moves, all from Session 4 Task 4 (now on disk):
      1. `TextLoader(corpus_path).load()` -> Documents.
      2. `RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)` -> chunks.
      3. `OpenAIEmbeddings(model=EMBEDDING_MODEL)`, and an on-disk client:
             client = QdrantClient(path=str(QDRANT_PATH))
         Create the collection only if it's missing (`client.collection_exists(name)`), build a
         `QdrantVectorStore`, and `.add_documents(chunks)` ONLY when the collection is empty
         (`client.count(name).count == 0`) — otherwise reuse what's already on disk.
      4. `vector_store.as_retriever(search_kwargs={"k": k})`.

    Two things persistence forces you to get right:
      - Idempotency: don't re-create or re-embed an index that already exists, or you pay to
        embed every boot (and `create_collection` throws on a collision). Guard both.
      - `chunk_id`: the chunk's position in the split list is the only id you have. Stamp it
        into metadata (`chunk.metadata["chunk_id"] = i`) BEFORE adding — it's what makes
        `Source.chunk_id` mean anything, and once on disk you can't add it retroactively.

    Note: on-disk Qdrant locks its folder to one client, so one server owns it at a time.
    Delete `qdrant_storage/` if you change the corpus, chunking, or embedding model.
    Hosted/shared instead? Run a Qdrant server and swap the client for
    `QdrantClient(url="http://localhost:6333")` — that's the multi-process production path.
    """
    
    
    # 1. Load the source document
    documents = TextLoader(corpus_path).load()

    # 2. Split the document into overlapping chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )

    chunks = text_splitter.split_documents(documents)

    # 3. Assign each chunk a unique identifier
    for i, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = i

    # 4. Initialize the OpenAI embedding model
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)

    # 5. Initialize persistent Qdrant storage
    QDRANT_PATH.mkdir(parents=True, exist_ok=True)

    client = QdrantClient(path=str(QDRANT_PATH))

    collection_name = "wellness_guide"

    # 6. Create the collection only if it is missing
    if not client.collection_exists(collection_name):
        client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(
                size=1536,
                distance=models.Distance.COSINE,
            ),
        )

    # 7. Connect the collection to LangChain
    vector_store = QdrantVectorStore(
        client=client,
        collection_name=collection_name,
        embedding=embeddings,
    )

    # 8. Embed documents only if the collection is empty
    if client.count(collection_name).count == 0:
        vector_store.add_documents(chunks)

    # 9. Return a retriever configured for k results
    return vector_store.as_retriever(
        search_kwargs={"k": k}
    )

