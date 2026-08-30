# Phase 1 Mastery Gate — Mathematics Without Magic

**Mode:** mostly closed-solution assistance. Calculator and a blank notebook are allowed. For selected reference questions, the assessment will say when notes are allowed.

## Part A — Explain
From memory, explain in plain language:
- function;
- vector vs matrix;
- dot product;
- matrix transformation;
- span/rank intuition;
- conditional probability;
- expectation and variance;
- sample vs population;
- correlation warning;
- derivative;
- gradient;
- learning rate.

If your explanation is only a formula, it is incomplete.

## Part B — Compute
Complete a small set of hand calculations involving:
- algebra/logs/summations;
- vector operations and dot products;
- matrix-vector multiplication;
- Bayes using frequencies;
- expectation/variance of a tiny discrete distribution;
- simple derivative/partial derivative;
- two gradient-descent steps.

## Part C — Translate
Take this expression:

`L(w) = (1/n) Σ (y_i - w·x_i)^2`

Explain every symbol and describe the computation as pseudocode.

## Part D — Diagnose misconceptions
Correct statements such as:
- "zero correlation means independence";
- "a 99% accurate medical test means a positive result has 99% probability of disease";
- "matrix multiplication is element-by-element multiplication";
- "gradient descent guarantees the global minimum";
- "a larger sample fixes biased data collection."

## Part E — ML-flavored transfer
Given a two-feature linear model and a tiny dataset:
1. compute several predictions;
2. compute a simple squared-error loss;
3. reason which weight direction should lower loss;
4. explain what you would expect an optimizer to do.

## Pass standard
Pass when you can **compute + explain + transfer**. If arithmetic is shaky but reasoning is sound, repair arithmetic. If formulas are correct but meaning is absent, repeat conceptual work before advancing.

## Repair map
- algebra/functions → Modules 1.1–1.2 + OpenStax targeted practice
- linear algebra → Modules 1.3–1.7 + visual intuition + selected problems
- probability/statistics → Modules 1.8–1.12 + frequency-table exercises
- calculus/optimization → Modules 1.13–1.15 + derivative/gradient tracing
