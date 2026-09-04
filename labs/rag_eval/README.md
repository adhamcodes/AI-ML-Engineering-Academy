# Local RAG Evaluation Lab

This lab uses a tiny local corpus so retrieval experiments are reproducible and free.

Run:

```bash
python evaluator.py
```

The included lexical retriever is only a baseline. Improve chunking/retrieval/reranking while keeping `questions.json` frozen during comparison.

Report retrieval hit rate separately from answer quality. A generation model cannot recover evidence that retrieval never supplied.
