# Module 1.2 — Functions and Graphs

## Capability
Treat a function as an input-output rule, interpret its graph, and reason about slope, shape, domain, range, composition, and transformations.

## Mental model
A function is a machine:

`input x → rule f → output f(x)`

In ML, a model is fundamentally a function—often a huge parameterized one.

## Core ideas
- **Domain:** allowed inputs.
- **Range:** possible outputs.
- **Function value:** `f(3)` means run input 3 through the rule.
- **Graph:** visual relationship between input and output.
- **Slope/rate of change:** how output changes when input moves.
- **Composition:** output of one function becomes input to another: `f(g(x))`.

## Examples
`f(x)=2x+1` is linear. Every +1 in x changes output by +2.

`f(x)=x^2` is nonlinear. The rate of change itself changes with x.

A neural network is composed functions: layer after layer transforms representations.

## Prediction drill
Without plotting software, predict the rough shape of:
- `y=x`
- `y=x^2`
- `y=|x|`
- `y=e^x`
- `y=ln(x)`

Then verify with a graphing tool.

## ML transfer
Suppose loss `L(w)` is plotted against one model parameter w. What would a low point mean? What might the slope near that point tell an optimizer?

## Mastery
You can move between equation, table, verbal description, and graph.
