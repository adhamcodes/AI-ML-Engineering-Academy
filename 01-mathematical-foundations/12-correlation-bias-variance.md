# Module 1.12 — Correlation and Bias/Variance Thinking

## Capability
Use correlation cautiously and understand the first intuition behind the statistical/ML bias–variance tradeoff.

## Correlation
Correlation standardizes linear co-movement, often to a range from -1 to +1.

It can be useful but dangerous:
- correlation does not establish causation;
- outliers can distort it;
- nonlinear relationships may have weak linear correlation;
- aggregating subgroups can hide/reverse patterns.

Always visualize and understand the data-generating context.

## Bias–variance intuition
A model can fail because it is:
- too rigid to capture the pattern (**high bias / underfitting**), or
- too sensitive to training-data quirks (**high variance / overfitting**).

This is not yet the full formal decomposition. It is a mental model for later model selection and regularization.

## Thought experiment
Fit:
1. a straight line to strongly curved data;
2. a degree-30 polynomial through 20 noisy points.

Which failure mode do you expect in each case? What might happen on new data?

## Mastery
You can explain why a strong correlation is not automatically a causal feature and why training fit alone cannot determine model quality.
