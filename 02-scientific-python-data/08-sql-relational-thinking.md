# Module 2.8 — SQL and Relational Thinking

## Capability
Query normalized tables and reason about keys/relationships before ML data is flattened into a modeling table.

Core SQL:
- SELECT/WHERE/ORDER BY;
- aggregates and GROUP BY;
- JOINs;
- INSERT/UPDATE/DELETE awareness;
- primary/foreign keys;
- transaction intuition.

## Why ML engineers need SQL
Training data often originates in operational databases. You need to know what one row means, how tables relate, and how a query can accidentally duplicate observations or leak future events.

## Practice
Given `customers`, `orders`, and `support_tickets`, write queries to calculate historical features as of a cutoff date. Explicitly exclude information occurring after that date.

## Mastery
You can build a small analysis dataset from relational tables and defend its unit of observation and time boundary.
