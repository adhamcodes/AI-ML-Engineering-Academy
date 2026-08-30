# Module 06.12 — Fine-Tuning & Parameter-Efficient Adaptation

## Capability
Understand full fine-tuning vs adapters/LoRA-style adaptation and dataset/evaluation requirements.

## Mental model / core ideas
Adaptation changes model behavior through supervised/preference/objective data. PEFT trains a small parameter subset/low-rank adapters, reducing memory/compute but not removing data-quality risk.

## Practice
Fine-tune a small model or simulate adapter workflow on modest compute.

## Debugging / transfer task
Detect overfit/data contamination/evaluation leakage.

## Build evidence
Write an adaptation decision memo including baseline and eval plan.

## Mastery check
Explain why prompting/RAG/fine-tuning are different interventions.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
