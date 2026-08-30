# Module 3.2 — Train, Validation, and Test Design

## Capability
Create evaluation splits that mimic deployment rather than randomly slicing everything by habit.

Roles:
- train: fit model parameters;
- validation/CV: choose models/hyperparameters;
- test: final unbiased-ish estimate after choices are frozen.

Special structures require special splits:
- time → train on past, validate/test on future;
- repeated entities → keep same person/device/group from leaking across sets;
- spatial/site data → consider site/group separation.

## Practice
Design splits for monthly sales forecasting, patient visits, and user-event classification. Explain why ordinary random split could be optimistic in each.

## Mastery
Your split reflects the real future use case.
