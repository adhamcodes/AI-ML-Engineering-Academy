# Module 1.15 — Gradient Descent and Optimization Intuition

## Capability
Explain and manually simulate basic gradient descent, learning-rate effects, and optimization failure modes.

## Core update
For parameter vector w:

`w_new = w_old - η ∇L(w_old)`

where η (eta) is the learning rate.

Interpretation:
1. measure local uphill direction;
2. step the opposite way;
3. repeat.

## Learning rate
Too small:
- painfully slow progress;
- may appear stuck.

Too large:
- overshoot;
- oscillation;
- divergence.

There is no single universally correct learning rate.

## Manual example
`L(w)=w^2`, gradient `2w`.
Start w=4, learning rate 0.1.

Update 1: `w = 4 - 0.1*8 = 3.2`.

Compute several more steps and watch |w| shrink.

## Real-world caveats
Modern training uses mini-batches and optimizers such as SGD variants/Adam. Loss surfaces can contain flat regions, saddles, noise, and complex geometry. Basic gradient descent is the conceptual foundation, not the whole story.

## Debugging thought experiment
Training loss becomes NaN after increasing learning rate 100×. Why is optimization a more plausible first suspect than "the dataset is too easy"?

## Mastery
You can connect derivative → gradient → update → training behavior.
