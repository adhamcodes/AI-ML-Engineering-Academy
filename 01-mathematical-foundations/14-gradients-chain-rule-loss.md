# Module 1.14 — Gradients, Chain Rule, and Loss Surfaces

## Capability
Understand how derivatives across many parameters form a gradient and why the chain rule powers backpropagation.

## Gradient
For scalar function `L(w1,...,wn)`, the gradient is the vector of partial derivatives:

`∇L = [∂L/∂w1, ..., ∂L/∂wn]`

It points in the direction of steepest local increase under the usual Euclidean interpretation. Moving in the negative-gradient direction locally reduces L for a sufficiently small step.

## Loss surface
Imagine model parameters as coordinates and loss as height. Training searches for low regions of this landscape.

Real neural-network loss surfaces are enormously high-dimensional; the landscape image is intuition, not a literal 3D picture.

## Chain rule
If `y=f(g(x))`, a change in x affects g, which affects f.

`dy/dx = (df/dg)(dg/dx)`

Neural networks are composed functions, so backpropagation repeatedly applies this dependency rule efficiently.

## Trace exercise
Let:
`u=2x`
`y=u^2`

Find `dy/dx` using the chain rule and verify by simplifying y first.

## ML transfer
If a parameter affects loss only through several intermediate layers, chain rule propagates its influence through those steps.

## Mastery
You can explain backpropagation's mathematical foundation without saying "PyTorch just calculates it."
