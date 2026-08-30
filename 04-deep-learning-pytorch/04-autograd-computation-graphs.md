# Module 04.4 — Autograd & Computation Graphs

## Capability
Explain automatic differentiation and inspect gradients in PyTorch.

## Mental model / core ideas
Operations create a graph linking outputs to parameters. Reverse-mode autodiff applies the chain rule backward through that graph.

## Practice
Build a scalar/tensor expression in PyTorch, call backward, and verify gradients manually.

## Debugging / transfer task
Find why a gradient is None or unexpectedly disconnected after detach/no_grad/in-place misuse.

## Build evidence
Create a gradient-inspection utility for a tiny network.

## Mastery check
You can predict which tensors receive gradients and why.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
