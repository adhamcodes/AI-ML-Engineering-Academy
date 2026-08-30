# Module 1.13 — Derivatives and Partial Derivatives

## Capability
Interpret derivatives as local rates of change and partial derivatives as sensitivity to one variable while holding others fixed.

## Derivative intuition
For function `f(x)`, derivative `f'(x)` describes how rapidly f changes for a tiny change in x near that point.

Geometrically: slope of the tangent line.

Computationally: local sensitivity.

## Why ML cares
Training asks:
> If I nudge this parameter, how does the loss change?

That is derivative language.

## Examples
`f(x)=x^2` has derivative `2x`.

At x=3, slope is 6: a small positive increase in x increases f by roughly 6 times that small change.

## Partial derivative
If `L(w1,w2)` depends on many parameters, `∂L/∂w1` measures local change with respect to w1 while holding w2 fixed.

A model with millions of parameters has millions of such sensitivities; gradients collect them.

## Practice
- Explain derivative of position with respect to time.
- Differentiate simple powers such as `x^3`, `5x`, constant 7.
- For `f(x,y)=x^2+3y`, calculate partial derivatives with respect to x and y.
- Interpret signs of derivatives near a point.

## Depth boundary
We need operational calculus, not epsilon-delta proof mastery.

## Mastery
You can read a derivative as sensitivity rather than a memorized symbol-manipulation ritual.
