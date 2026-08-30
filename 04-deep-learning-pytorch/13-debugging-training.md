# Module 04.13 — Neural-Network Debugging

## Capability
Use a systematic debugging ladder for bad training rather than tuning blindly.

## Mental model / core ideas
Verify data/labels → shapes/ranges → tiny-batch overfit → loss/gradients → optimizer → regularization → scale.

## Practice
Make a tiny model overfit 20 examples; inspect gradients/activations; establish a simple baseline.

## Debugging / transfer task
Receive a system with shuffled labels, wrong target dtype, excessive LR and eval-mode bug; isolate causes one by one.

## Build evidence
Create your own `DL_DEBUG_CHECKLIST.md` backed by evidence from experiments.

## Mastery check
You can distinguish data, code, optimization and generalization failures.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
