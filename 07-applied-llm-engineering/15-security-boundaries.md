# Module 07.15 — LLM Security & Data Boundaries

## Capability
Threat-model prompts, retrieval, tools and sensitive data.

## Mental model / core ideas
Treat retrieved/user/model content as untrusted data. Separate instructions from data, enforce permissions outside the model, minimize secrets and validate tool arguments.

## Practice
Run prompt-injection and malicious-document tests.

## Debugging / transfer task
Demonstrate why “ignore previous instructions” defenses alone are insufficient.

## Build evidence
Write a threat model and mitigations.

## Mastery check
Critical authorization is deterministic and testable.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
