# Module 04.5 — Backpropagation from First Principles

## Capability
Derive a small network gradient and connect the derivation to autograd.

## Mental model / core ideas
Backprop is efficient chain-rule reuse through a graph, not a separate mysterious learning algorithm.

## Practice
Differentiate a 2-layer scalar network by hand and compare with PyTorch.

## Debugging / transfer task
Locate the mathematical effect of a saturated activation on upstream gradients.

## Build evidence
Implement a tiny manual-gradient training step in NumPy.

## Mastery check
Explain local derivatives, upstream gradient and parameter update in your own words.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
