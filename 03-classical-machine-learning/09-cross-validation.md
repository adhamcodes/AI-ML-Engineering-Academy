# Module 3.9 — Cross-Validation

## Capability
Estimate model-selection performance across multiple train/validation partitions while respecting data structure.

K-fold CV reduces dependence on one split, but it is not automatically valid. Use stratified/group/time-aware splitters when the problem requires them.

Do preprocessing inside the pipeline within each fold.

## Practice
Compare plain KFold, StratifiedKFold, GroupKFold/time split on synthetic structured datasets. Explain which deployment assumption each encodes.

## Mastery
You choose the CV scheme before comparing models and do not tune on the final test set.
