# Module 04.3 — Loss Functions & Objectives

## Capability
Choose and interpret losses appropriate to regression/classification rather than using defaults blindly.

## Mental model / core ideas
The loss translates prediction quality into an optimization signal; it is not always the same as the business metric.

## Practice
Compare MSE, MAE, binary cross-entropy and multiclass cross-entropy on toy examples.

## Debugging / transfer task
A classifier reports high accuracy but training loss behaves strangely: inspect label encoding/logit/loss mismatches.

## Build evidence
Implement small NumPy versions of MSE and binary cross-entropy with numerical safeguards.

## Mastery check
Explain what the loss rewards, its assumptions, and one mismatch with deployment goals.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
