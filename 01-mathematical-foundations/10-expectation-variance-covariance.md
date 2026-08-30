# Module 1.10 — Expectation, Variance, Covariance, and Independence

## Capability
Describe center, spread, and co-movement of random variables and connect them to data/model behavior.

## Expectation
Expected value is a probability-weighted long-run average under a distribution.

It is not necessarily a value you will observe.

## Variance
Variance measures average squared deviation from the mean:

`Var(X) = E[(X - E[X])^2]`

Standard deviation is the square root of variance, returning to the original units.

## Covariance
Covariance describes whether two variables tend to move together relative to their means.

Positive: high values of one tend to accompany high values of the other.
Negative: high tends to accompany low.
Near zero: little linear co-movement—but **zero covariance does not universally imply independence**.

## Independence
Roughly, learning one variable gives no information about the other under the model.

Independence is stronger than "uncorrelated" in general.

## ML connection
- feature redundancy;
- covariance matrices;
- PCA later;
- uncertainty and noise;
- standardized features.

## Practice
Create two small numeric lists with positive covariance intuition, two with negative, and a nonlinear relationship that could fool a simple linear-correlation summary.

## Mastery
You can distinguish mean, variance, covariance, correlation, and independence conceptually.
