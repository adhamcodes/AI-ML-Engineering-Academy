# Public Release Audit

Repository: **AI/ML Engineering Academy**

## Current rebuild verification — 2026-09-04

The release gate is now executable and continuous rather than a one-time Markdown scan.

GitHub Actions verifies on both Linux and Windows using Python 3.12 and 3.14:

- all 12 phase directories and required phase files exist,
- every controlled lab mapped by `LAB_MAP.md` exists,
- local Markdown links resolve inside the repository,
- actionable TODO/TBD/FIXME placeholders are rejected,
- unexpected empty files are rejected,
- common committed-secret patterns are rejected,
- dependency-free lab smoke tests pass,
- the known-broken agent implementation is rejected by its evaluator.

A separate framework red-team job installs the declared lab dependencies and verifies that:

- the deliberately leaked classical-ML pipeline produces suspiciously near-perfect validation behavior,
- the PyTorch evaluator rejects the deliberately broken training project,
- the tiny-transformer behavioral contract rejects the unimplemented starter.

The MLOps container gate builds the supplied Docker image, boots it, verifies `/health`, and sends a real `/predict` request through the mapped container port.

### Result

**PASS** when the current `Academy quality gates` workflow is green. A green workflow proves the checks above; it does not claim that external resources can never change or that every possible learner solution is correct.

## Historical v1.0 audit

Before the executable rebuild, the v1.0 publication audit scanned **233 Markdown files** across **12 phase directories** and reported zero broken local links, curriculum placeholder markers, credential-like patterns, personal-name references, or missing phase README/RESOURCES/ASSESSMENT files. It inventoried **30 external URLs**.

Those counts are preserved here as historical evidence only; they are not current file-count claims after the executable lab rebuild.
