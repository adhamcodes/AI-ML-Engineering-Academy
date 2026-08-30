# Module 07.7 — RAG Pipeline Anatomy

## Capability
Build ingestion→chunk→index→retrieve→context→generate with traceable boundaries.

## Mental model / core ideas
RAG changes model inputs by retrieving external evidence; it does not make the model inherently truthful.

## Practice
Build a minimal RAG baseline with trace logs for retrieval/context/output.

## Debugging / transfer task
Find failure due to missing evidence vs bad generation.

## Build evidence
Create component-level tests.

## Mastery check
You can localize failures to retrieval, context construction or generation.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
