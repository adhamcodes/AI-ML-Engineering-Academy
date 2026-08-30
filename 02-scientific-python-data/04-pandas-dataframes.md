# Module 2.4 — DataFrames, Indexing, and Data Types

## Capability
Load tabular data, inspect schema, select/filter safely, and distinguish labels, positions, and dtypes.

A DataFrame is not "Excel inside Python." It is a labeled tabular data structure with explicit types and vectorized operations.

Core tasks:
- `head`, shape, columns, dtypes;
- selecting columns;
- filtering rows;
- label vs positional indexing;
- sorting;
- creating derived columns;
- importing/exporting CSV/Parquet where available.

## Practice
Load a small CSV and produce a `DATA_PROFILE.md` containing row count, column meanings, dtypes, unique-value observations, suspicious ranges, and possible identifiers/targets.

## Common mistake
A numeric-looking identifier should not automatically become a meaningful numeric feature. Schema meaning matters more than dtype.

## Mastery
You inspect a dataset before manipulating it and can explain every selected column's role.
