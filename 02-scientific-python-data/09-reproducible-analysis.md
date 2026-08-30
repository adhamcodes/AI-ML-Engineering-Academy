# Module 2.9 — Notebooks, Scripts, and Reproducible Analysis

## Capability
Explore interactively without creating a notebook that only works because cells were run in a secret order.

## Notebook strengths
- quick exploration;
- narrative + plots;
- iterative investigation.

## Notebook risks
- hidden state;
- out-of-order execution;
- duplicated transformation logic;
- huge outputs/files;
- hard-to-test pipelines.

## Professional pattern
Explore in a notebook, then move stable loading/cleaning/feature logic into functions/scripts/modules with tests where appropriate. Keep environment/data assumptions documented.

## Reproducibility checklist
- raw data source/version recorded;
- deterministic split/seed where needed;
- environment/dependencies recorded;
- transformations scripted;
- outputs reproducible from clean restart;
- no secrets/private raw data committed.

## Mastery
You can restart from a clean environment/process and reproduce the analysis result.
