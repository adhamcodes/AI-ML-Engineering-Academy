# Module 1.3 — Scalars, Vectors, and Matrices

## Capability
Recognize scalar/vector/matrix shapes, perform basic operations, and connect arrays of numbers to features, examples, and parameters.

## Mental model
- **Scalar:** one number.
- **Vector:** ordered list of numbers.
- **Matrix:** rectangular grid of numbers.

ML interpretation:
- one temperature → scalar;
- one customer's features `[age, income, visits]` → vector;
- many customers × many features → matrix.

## Shape matters
A matrix with 100 examples and 5 features has shape `100 × 5` if rows are examples and columns are features.

Never ignore shape. Many ML bugs are shape bugs wearing a fake moustache. 😭

## Operations
Vector addition works component by component when dimensions match.

Scalar multiplication scales every component.

Matrix addition requires compatible shape.

## Practice
Given:
`x = [2, -1, 4]`
`y = [3, 5, 0]`

Compute `x+y`, `2x`, and explain why adding `[1,2]` to x is undefined under ordinary vector addition.

A dataset has 2,000 rows and 12 feature columns. State the matrix shape and what one row represents.

## Transfer
A neural-network layer receives batches of 32 examples, each represented by 128 features. What two dimensions must appear somewhere in the input tensor shape?

## Mastery
You can explain the data meaning of dimensions, not merely calculate with grids.
