# Module 3.8 — Feature Engineering

## Capability
Create features that encode available domain information without leaking the target/future.

Examples:
- ratios;
- counts/windows using only past events;
- log transforms;
- interactions;
- category grouping;
- date-derived features.

Every engineered feature needs an availability timestamp: **could this value really be known when prediction happens?**

## Practice
For customer churn at date T, design ten candidate features and annotate each with source, window, and availability. Reject any future-derived feature.

## Mastery
You improve representation through domain reasoning rather than random feature explosion.
