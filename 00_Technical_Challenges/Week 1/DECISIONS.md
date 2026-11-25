# Decisions

One row one decision. This week is the first one. By Week 5 this file will explain what decisions you made during this bootcamp.

## Retrieval, week 1

**What I changed**

I label every retrieved passage with its real chunk id in the prompt, and the app prints that same id under the answer. I did not switch embedding models or the distance metric, and I reuse one embedding of the corpus per run.

**Why**

The notebook experiment attached a filename and chunk number to each passage, then still wrapped those passages as Source 1, Source 2, and Source 3. The top three sleep passages stayed the same and the scores barely moved (about 0.00002–0.00007), but the written answer kept the generic source labels. The failure was in the prompt, not in retrieval. Citing `chunk_id` directly is the fix that experiment pointed at: the label in the answer is the row in the index.

**What would change my mind**

I would go back to generic source numbers if chunk ids confused readers more than they helped, or if a later corpus reused the same text in two places so a text-keyed id collided. I would re-embed, instead of reusing vectors, if the chunk size, the guide, or the embedding model changed.
