# Module 08.8 — Persistence & Durable Execution

## Capability
Resume long-running workflows after process/network failures.

## Core model
Persist state at safe checkpoints and make side effects idempotent so replay does not duplicate actions.

## Practice
Simulate crash after a tool call and resume.

## Debug / transfer
Detect duplicate email/payment/write on replay.

## Evidence to save
Crash/restart integration test.

## Mastery
System resumes from explicit durable state.
