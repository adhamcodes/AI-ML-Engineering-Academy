# Module 06.6 — Transformer Block Anatomy

## Capability
Read a decoder/encoder block and explain residual, normalization, attention and feed-forward sublayers.

## Mental model / core ideas
Residual paths support information/gradient flow; normalization stabilizes activations; attention mixes positions; MLPs transform each position.

## Practice
Trace one block with tensor shapes and residual connections.

## Debugging / transfer task
Diagnose misplaced normalization/residual shape error conceptually.

## Build evidence
Implement a minimal block or inspect a small model source.

## Mastery check
Explain data flow from input hidden state to output.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
