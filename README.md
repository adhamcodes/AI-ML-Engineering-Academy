# AI/ML Engineering Academy

**Free • self-guided • mastery-based • project-driven**

A complete learning path for building broad **AI/ML engineering capability**, from a mathematics rebuild through classical machine learning, deep learning, modern LLM systems, agents, MLOps, production engineering, and AI system design.

This is not a certificate checklist and not a collection of links. The learning loop is:

> **learn → explain → practice → debug → build → assess → repair weaknesses → pass the gate**

## Start in 60 seconds

1. Open **[START-HERE.md](START-HERE.md)**.
2. Read the **[Self-Study Operating System](SELF_STUDY_SYSTEM.md)** once before Phase 0.
3. Complete Phase 0 honestly; do not skip the diagnostic because a topic name looks familiar.
4. Use the matching controlled lab from **[LAB_MAP.md](LAB_MAP.md)** as you progress.
5. Keep your own work and progress outside the canonical curriculum repository. Start from **[PROGRESS_TEMPLATE.md](PROGRESS_TEMPLATE.md)**.
6. Advance by mastery gates, not by calendar completion.

## Who this is for

- learners rebuilding weak or forgotten mathematics
- programmers moving toward ML/AI engineering
- self-taught learners who need demonstrable evidence rather than certificates
- students/professionals who want a structured path instead of tutorial hopping

You should have—or build concurrently—normal programming and software-engineering foundations.

## Roadmap at a glance

| Phase | Outcome | Typical effort |
|---|---|---:|
| [0 — Orientation & Diagnostic](00-orientation/README.md) | role map, environment, diagnostic, learning contract | 2–4 days |
| [1 — Mathematical Foundations](01-mathematical-foundations/README.md) | math used by ML, rebuilt from fundamentals | 4–6 weeks |
| [2 — Scientific Python & Data](02-scientific-python-data/README.md) | NumPy, data work, EDA, SQL, reproducibility | 3–4 weeks |
| [3 — Classical Machine Learning](03-classical-machine-learning/README.md) | end-to-end predictive modelling and evaluation | 6–8 weeks |
| [4 — Deep Learning & PyTorch](04-deep-learning-pytorch/README.md) | train and debug neural-network systems | 8–10 weeks |
| [5 — Vision & NLP Foundations](05-vision-nlp-foundations/README.md) | representation/model foundations before transformers | 4–6 weeks |
| [6 — Transformers & LLM Foundations](06-transformers-llm-foundations/README.md) | tokenization, attention, transformers, inference | 6–8 weeks |
| [7 — Applied LLM Engineering](07-applied-llm-engineering/README.md) | evaluated RAG/LLM systems and security | 6–8 weeks |
| [8 — Agents & AI Systems](08-agents-ai-systems/README.md) | bounded tool-using systems with recovery/evals | 4–6 weeks |
| [9 — MLOps & Production AI](09-mlops-production-ai/README.md) | test, package, serve, deploy, observe | 6–8 weeks |
| [10 — AI System Design](10-ai-system-design/README.md) | architecture and tradeoff reasoning | 4–6 weeks |
| [11 — Career Engineering](11-career-engineering/README.md) | portfolio, open source, interviews, applications | continuous |

Full detail: **[ROADMAP.md](ROADMAP.md)** · curriculum map: **[CURRICULUM_MAP.md](CURRICULUM_MAP.md)** · executable labs: **[LAB_MAP.md](LAB_MAP.md)**

## What makes this an academy instead of a roadmap

The repository includes native lessons, curated primary/practice/reference resources, active exercises, debugging and transfer tasks, integrated projects, closed-assistance assessments, remediation loops, mastery gates, portfolio standards, specialization maps, and a controlled executable lab layer.

The labs now provide stable data and real systems for the capabilities that previously existed mainly as specifications: leakage diagnosis, broken PyTorch training, tiny transformer implementation, local RAG evaluation, bounded-agent trajectory checks, and production service work.

## Compute policy

The required path is designed for CPU-first study and small controlled experiments. Heavy GPU training is an optional extension, not a graduation requirement.

Optional framework dependencies are listed in [`requirements-labs.txt`](requirements-labs.txt).

## Quality gates

This repository validates its phase structure, local links, and dependency-free lab smoke tests on both Linux and Windows through GitHub Actions.

Run the same checks locally:

```bash
python scripts/validate_academy.py
python scripts/run_smoke_tests.py
```

Framework-specific learner labs have their own contracts/evaluators and are intentionally not solved by CI on your behalf.

## Employment philosophy

Do not wait for every specialization. The academy contains earlier readiness gates, including **ML Foundation Ready**, **Junior Applied AI Ready**, and **AI/ML Engineer Ready**. Passing a gate means you have evidence worth presenting; it does not guarantee employment.

## AI assistance

AI is allowed as a tutor where stated and intentionally restricted at selected assessments. Read **[AI_ASSISTANCE_POLICY.md](AI_ASSISTANCE_POLICY.md)**. The goal is both independent competence and responsible AI-assisted engineering.

## Study with a friend

Use the same curriculum, but keep separate code/progress repositories. Attempt closed assessments independently first. Afterward, compare explanations, review each other's code, and discuss different solutions rather than copying one learner's submission.

## Resource policy

Core material is designed to remain navigable even when tools change. External resources are curated by learning objective and tagged by freshness. See **[RESOURCE_STANDARD.md](RESOURCE_STANDARD.md)** and **[resources/RESOURCE_REGISTRY_2026.md](resources/RESOURCE_REGISTRY_2026.md)**.

## License & contributions

Educational content is CC BY 4.0; code examples are MIT-licensed. See **[LICENSE.md](LICENSE.md)**. Contributions should preserve prerequisites, mastery gates, and assessment integrity; see **[CONTRIBUTING.md](CONTRIBUTING.md)**.

> Start here: **[START-HERE.md](START-HERE.md)**
