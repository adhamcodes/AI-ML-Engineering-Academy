# Module 04.14 — GPU Execution & Mixed Precision

## Capability
Use accelerators safely and understand device/precision tradeoffs.

## Mental model / core ideas
GPU speedups depend on parallel workload and transfer costs. Lower precision can increase throughput/memory efficiency but requires numerically safe training.

## Practice
Move model/data/device coherently; profile CPU vs GPU; try autocast/scaler where supported.

## Debugging / transfer task
Diagnose device mismatch, OOM and unstable mixed-precision training.

## Build evidence
Write a device-aware training script that also runs on CPU.

## Mastery check
You can explain why “GPU available” does not guarantee faster training.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
