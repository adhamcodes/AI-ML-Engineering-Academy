# Module 06.2 — Vocabulary, Embeddings & Output Heads

## Capability
Trace token IDs into vector representations and back to token probabilities.

## Mental model / core ideas
Embedding tables map IDs to vectors; decoder language models transform contextual representations and project them to vocabulary logits.

## Practice
Trace tensor shapes from token IDs to embeddings to logits.

## Debugging / transfer task
Find confusion between static token embedding and contextual hidden state.

## Build evidence
Inspect embedding/output shapes of a small open model.

## Mastery check
Explain each major tensor without hand-waving.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
