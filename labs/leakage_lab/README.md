# Classical ML Leakage Lab

`make_dataset.py` generates a synthetic classification dataset with a deliberately forbidden feature named `future_outcome`.

`broken_pipeline.py` trains with that feature and reports suspiciously perfect validation performance.

Your job:

1. generate the dataset,
2. explain why the metric is unbelievable,
3. identify the leakage source,
4. create a leakage-safe split and feature pipeline,
5. compare a simple baseline with at least two model families,
6. freeze a test set before tuning,
7. report validation vs final test performance separately.

The forbidden feature simulates information that would only exist after the prediction moment.
