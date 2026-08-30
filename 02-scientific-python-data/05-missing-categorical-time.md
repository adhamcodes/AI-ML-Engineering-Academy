# Module 2.5 — Missing, Categorical, and Time Data

## Capability
Treat special data types as domain information rather than cleaning annoyances.

## Missing data
Ask **why** it is missing before choosing drop/fill/impute. Missingness may itself carry information or reveal collection failures.

## Categorical data
Categories can be unordered (`country`) or ordered (`low < medium < high`). Arbitrarily converting category labels to integers can create fake numerical distance.

## Time data
Parse timestamps deliberately, track timezone assumptions, derive time features only when legitimate, and never let future information leak into past predictions.

## Practice
Given a customer table with missing income, categorical plan, signup timestamp, and cancellation timestamp, write a treatment plan for each field before coding.

## Mastery
You can justify handling from the data-generating process, not just invoke `.fillna(0)`.
