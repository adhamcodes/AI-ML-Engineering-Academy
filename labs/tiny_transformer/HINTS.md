# Progressive Hints

## Hint 1

Write down the expected shape of `Q @ K^T` before touching code.

## Hint 2

The scale depends on the key/query feature dimension, not sequence length.

## Hint 3

The mask should mark positions whose key index is greater than the current query index.

## Hint 4

Normalize scores across candidate key positions so each query produces a distribution over what it may attend to.
