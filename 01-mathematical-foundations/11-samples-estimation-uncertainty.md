# Module 1.11 — Samples, Populations, Estimation, and Uncertainty

## Capability
Stop treating a dataset as the entire universe and reason about what can and cannot be inferred from a sample.

## Population vs sample
- **Population:** target set/process you care about.
- **Sample:** observations you actually collected.

Machine learning almost always learns from a sample and hopes to generalize to future/unseen data from the target process.

## Estimator
An estimator uses sample data to estimate an unknown population quantity.

Example: sample mean estimates population mean under assumptions.

## Sampling variability
Take a different sample and you usually get a different estimate. That variability is not necessarily a bug—it is part of uncertainty.

## Bias
A sampling/measurement process can systematically miss the population you claim to model.

A million biased observations do not magically become representative.

## Confidence intuition
A confidence interval is produced by a procedure with a repeated-sampling coverage interpretation under assumptions. Do not reduce it to "there is a 95% probability the fixed parameter is inside" without understanding the framework.

At this stage, focus on uncertainty rather than formal inferential proofs.

## ML transfer
Train/validation/test splits, distribution shift, and evaluation all depend on whether samples represent deployment conditions.

## Practice
A company trains a hiring model only on employees hired by the old process. Identify at least two ways the sample could fail to represent future applicants.

## Mastery
You ask "sampled from what process?" before trusting a metric.
