# Module 1.9 — Random Variables and Distributions

## Capability
Treat uncertain quantities as random variables and reason about distributions rather than single observed values.

## Random variable
A random variable maps outcomes of an uncertain process to numbers.

Examples:
- number of support tickets tomorrow;
- response latency;
- sampled height;
- model error on a randomly drawn example.

## Distribution
A probability distribution describes how probability is allocated across possible values.

Useful families to recognize:
- Bernoulli: one yes/no trial;
- Binomial: number of successes across fixed trials;
- Categorical: one of multiple categories;
- Normal/Gaussian: continuous bell-shaped model under certain conditions;
- Uniform: equal density/probability over a defined range/set.

You do not need to force every dataset into a named distribution.

## PMF vs PDF intuition
Discrete variables can assign probability mass to individual values. Continuous distributions use density; probability over an interval comes from area, not the density at one exact point.

## Practice
Choose a plausible random-variable model for:
- coin flip;
- class label among 5 categories;
- number of conversions among 100 independent trials (under simplifying assumptions);
- measurement noise roughly clustered around zero.

Then state one reason the idealized model could be wrong in real data.

## Mastery
You can describe uncertainty with a distribution and understand that a model assumption is not reality itself.
