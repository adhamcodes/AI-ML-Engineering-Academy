# Module 1.1 — Algebra, Notation, Exponents, Logs, and Summations

## Capability
Manipulate the basic expressions that will appear everywhere in ML and translate notation into plain language.

## Why ML cares
Training code is full of expressions such as:

`y = wx + b`

`L = (1/n) Σ (y_i - ŷ_i)^2`

`p ∝ e^z`

If symbols themselves consume all your attention, the ML idea disappears. This module makes notation boring again.

## Core refresh
### Variables and equations
A variable is a symbol representing a value. Solving an equation means finding values that make both sides equal.

If `3x + 2 = 14`, isolate `x` by applying inverse operations to both sides.

### Powers
`x^2` means x multiplied by itself. Negative powers represent reciprocals: `x^-1 = 1/x` for nonzero x.

### Exponentials
An exponential function changes multiplicatively. `e^x` appears constantly in probability and neural networks.

### Logarithms
`log_b(x)` asks: **what power of b produces x?**

Natural log `ln(x)` uses base `e`.

Useful intuition: logarithms turn multiplication into addition and compress large scales.

### Sigma notation
`Σ` means repeated addition.

`Σ_{i=1}^n x_i` means add x1 through xn.

The index is not mystical. It is a compact loop.

## ML-flavored example
Mean squared error:

`MSE = (1/n) Σ (y_i - ŷ_i)^2`

Read it as:
1. for every example i, find prediction error;
2. square it;
3. add all squared errors;
4. divide by number of examples.

## Practice
- Solve: `5x - 7 = 18`.
- Simplify: `x^3 * x^2`.
- Rewrite `log_2(32)=5` as an exponential statement.
- Expand `Σ_{i=1}^4 (2i)` manually.
- Explain MSE in words without using sigma notation.

## Mastery
You can read compact notation as instructions rather than decoration.
