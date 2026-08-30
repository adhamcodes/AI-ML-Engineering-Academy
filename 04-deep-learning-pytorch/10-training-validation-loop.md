# Module 04.10 — Training & Validation Loops

## Capability
Write a clean training loop from an empty file and keep train/eval semantics correct.

## Mental model / core ideas
Each epoch coordinates forward pass, loss, backward, optimizer step and evaluation. Validation measures generalization without parameter updates.

## Practice
Reconstruct a loop without copying; add metrics, device handling and no_grad/inference context.

## Debugging / transfer task
Repair code that forgets zero_grad, model.train/model.eval, or accidentally backprops validation loss.

## Build evidence
Package train_one_epoch/evaluate functions with tests on a tiny dataset.

## Mastery check
You can write and explain the loop independently.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
