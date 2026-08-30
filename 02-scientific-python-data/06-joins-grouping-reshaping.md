# Module 2.6 — Joins, Grouping, and Reshaping

## Capability
Combine tables without silently duplicating/dropping rows and produce grouped summaries that preserve the right unit of analysis.

## Joins
Before merging, state the expected relationship:
- one-to-one;
- one-to-many;
- many-to-many.

A many-to-many join can multiply rows dramatically. Always check row counts and key uniqueness before/after.

## Grouping
Think "split → apply → combine": group rows by a key, compute summary/transform/filter, combine results.

## Reshaping
Real data arrives wide, long, nested, duplicated, and inconvenient. `pivot`, `melt`, aggregation, and explode-like operations change representation; they must not change the underlying meaning accidentally.

## Practice
Join customers to orders, then compute per-customer count, total spend, and average order value. Reconcile aggregate totals before vs after the join.

## Mastery
You can predict cardinality and validate that a merge did not corrupt the dataset.
