# Module 1.8 — Probability, Conditional Probability, and Bayes' Rule

## Capability
Reason about uncertainty, conditional events, and how evidence updates beliefs.

## Probability
Probability assigns a number between 0 and 1 to uncertainty under a model.

Important distinction:
- `P(A)` — probability of A;
- `P(A|B)` — probability of A given that B is known.

These are often very different.

## Product intuition
`P(A and B) = P(A|B) P(B)`.

This simply says: probability of reaching B and then A under B.

## Bayes' rule
Bayes reverses conditioning:

`P(A|B) = P(B|A)P(A) / P(B)`

Mental model:
> posterior = evidence compatibility × prior / overall evidence frequency

## Example — rare condition
A test can be highly accurate yet a positive result may still have modest probability of the condition when the condition itself is rare. The base rate matters.

Do not memorize the slogan. Build a table of 10,000 hypothetical people and count outcomes.

## Practice
- Explain `P(spam | contains-link)` vs `P(contains-link | spam)`.
- Construct a frequency table for a rare-event test.
- Identify the prior, likelihood, evidence, and posterior in one scenario.

## ML transfer
Classification outputs and Bayesian models require careful interpretation of probability. Evaluation also depends on prevalence/base rates.

## Mastery
You stop confusing reversed conditional probabilities.
