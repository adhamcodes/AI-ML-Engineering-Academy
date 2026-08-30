# Module 3.7 — Preprocessing and Pipelines

## Capability
Fit preprocessing only on training data and chain transformations with the estimator so cross-validation remains honest.

Common steps:
- scaling numeric features;
- imputing missing values;
- encoding categories;
- feature selection/transformation.

scikit-learn `Pipeline` exists so transformers and final estimator can be fit/cross-validated together. Use `ColumnTransformer` for heterogeneous columns.

## Practice
Build a numeric+categorical preprocessing pipeline and prove the imputer/scaler are fit only inside training folds.

## Mastery
No preprocessing statistic is learned from validation/test data.
