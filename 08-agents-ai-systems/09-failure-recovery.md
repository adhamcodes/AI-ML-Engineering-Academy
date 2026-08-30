# Module 08.9 — Tool Failure & Recovery

## Capability
Handle unavailable, slow, partial or invalid tools predictably.

## Core model
Recovery can retry, use fallback, ask user, re-plan or fail safely; it should not invent tool results.

## Practice
Inject timeout/429/5xx/malformed output and define policy.

## Debug / transfer
Catch an agent hallucinating success after tool failure.

## Evidence to save
Failure matrix and traces.

## Mastery
Every critical tool failure has explicit outcome.
