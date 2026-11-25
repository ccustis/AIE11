# Week 1 retrieval app

The green nodes are the citation change from the notebook experiment: retrieved hits keep their index row, and the prompt is told to cite that id instead of renumbering passages as Source 1.

```mermaid
flowchart TD
    D["corpus path"] --> L["load_corpus: string"]
    L --> S["split_corpus: list of strings"]
    S --> E["embed_texts: OpenAI embeddings"]
    E --> M["build_index: matrix, shape n by 1536"]
    Q["question string"] --> QE["embed the question: OpenAI embeddings"]
    M --> R["search: score every row"]
    QE --> R
    S --> R
    R --> H["list of Hit: chunk_id, text, score"]
    H --> P["build_messages: cite chunk_id, not Source 1"]
    Q --> P
    P --> C["answer: OpenAI chat, temperature 0"]
    C --> A["answer string"]
    H --> CIT["printed citations"]

    classDef changed fill:#e6f4ee,stroke:#26836a,color:#133e34;
    class H,P,CIT changed;
    classDef paid fill:#fff4e5,stroke:#b86e00,color:#3d2a00;
    class E,QE,C paid;
```

OpenAI is called in three places: once to embed the chunks, once to embed the question, and once to write the answer. A new process embeds the chunks again. It does not keep the matrix.
