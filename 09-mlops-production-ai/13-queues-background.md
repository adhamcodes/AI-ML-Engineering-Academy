# Module 09.13 — Queues & Background Jobs

## Capability
Decouple long/variable work from request-response paths.

## Core model
Queues buffer jobs, enable retries and scaling, but introduce duplicate/out-of-order handling and operational state.

## Practice
Build a simple background-job pattern or simulate one.

## Debug / transfer
Handle duplicate delivery and poison job.

## Evidence to save
Worker/idempotency design + tests.

## Mastery
Request path does not wait for long AI job without reason.
