# Phase 2 Flagship — Messy Data Quality & EDA Project

Choose a non-toy public dataset with enough mess to require judgment: missing values, multiple tables or mixed types, inconsistent categories, time data, duplicates, or suspicious fields.

## Deliverables
- `README.md` — question, dataset source, limitations;
- `DATA_DICTIONARY.md` — unit of observation and field meanings;
- `QUALITY_REPORT.md` — missingness, duplicates, ranges, anomalies, leakage risks;
- reproducible loading/cleaning code;
- SQL extraction/query if relational data is used;
- EDA notebook/report with purposeful visualizations;
- `DECISIONS.md` — every major cleaning decision and its justification;
- clean derived dataset or reproducible generation script;
- tests/checks for important invariants.

## Forbidden shortcuts
- deleting all missing rows without analysis;
- treating identifiers as meaningful numeric features without justification;
- using future information in historical features;
- hand-editing the cleaned CSV as the source of truth.

## Portfolio standard
A reviewer should see data-engineering judgment, not only pandas syntax.
