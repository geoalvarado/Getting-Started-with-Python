# Python Statistics Notes
Notes I have taken in regards to python statistics:

## Generating an array of random numbers. Specifying min and max values, as well as the array size:
```
from scipy.stats import uniform
rand_array = uniform.cdf(0, 5, size=10)
```
A couple of things to consider. `scipy` is pythons most famous library to use for mathematical analysis. For statistical analysis specifically, you can use the `stats` module.

Inside `stats`, you can find `uniform` which has some functions that can help generating distributions and arrays good for calculations. 

Go here for more info on cdf: `https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.Uniform.cdf.html`

# Creating a binary array based on probability distribution

binom.rvs() is a function from SciPy’s scipy.stats module that generates random samples from a binomial distribution.

```
scipy.stats.binom.rvs(n, p, size=None)
```

Where:
n: Number of trials (e.g., number of coin flips)

p: Probability of success in each trial (e.g., probability of getting heads)

size: Number of random samples to generate (default is 1)

Use Cases:
Simulating coin flips (or any repeated binary outcome)

Modeling success/failure experiments (e.g., number of defective items in a batch)

Testing probabilistic algorithms (e.g., A/B testing, reliability modeling)

# Using Probability Mass Functions (PMF) in Python Scipy Stats:

The `scipy.stats` module in Python provides several probability mass functions (PMF) for discrete distributions. A PMF gives the probability that a discrete random variable is exactly equal to some value. Here's an overview of some commonly used PMF functions:

`binom.pmf(k, n, p, loc=0)`: Binomial distribution PMF. It returns the probability of getting exactly k successes in n independent trials, where the probability of success in a single trial is p. loc shifts the distribution.

```
    from scipy.stats import binom
    # Probability of 2 successes in 5 trials with p=0.3
    probability = binom.pmf(2, 5, 0.3)
    print(probability) # Output: 0.3087
```

`poisson.pmf(k, mu, loc=0)`: Poisson distribution PMF. It returns the probability of k events occurring in a fixed interval of time or space if these events occur with a known average rate mu.

```
    from scipy.stats import poisson
    # Probability of 3 events with an average rate of 2
    probability = poisson.pmf(3, 2)
    print(probability) # Output: 0.1804
```

Now, let's talk about scipy stat's `.cdf`...

# Using Cummulative Distribution Functions (PMF) in Python Scipy Stats:

In SciPy's stats module, CDF functions compute the cumulative distribution function for various probability distributions. The CDF at a value x is the probability that a random variable, following a given distribution, will be less than or equal to x.

Common CDF functions in scipy.stats:
```
cdf(x, *args, loc=0, scale=1): This is a general method available for continuous distributions.
x: The value(s) at which to evaluate the CDF.
*args: Shape parameters specific to the distribution.
loc: Location parameter (default is 0).
scale: Scale parameter (default is 1).
```

```
from scipy.stats import norm, t, expon

# Normal distribution
x = 1.96
prob_norm = norm.cdf(x)
print(f"P(Z <= {x}) for normal distribution: {prob_norm}")

# Student's t-distribution with 10 degrees of freedom
x = 2.23
prob_t = t.cdf(x, df=10)
print(f"P(T <= {x}) for t-distribution (df=10): {prob_t}")

# Exponential distribution with default parameters
x = 1
prob_exp = expon.cdf(x)
print(f"P(X <= {x}) for exponential distribution: {prob_exp}")
```

Key Distributions and their CDF Functions:

```
Normal (Gaussian): norm.cdf(x, loc=0, scale=1)
Student's t: t.cdf(x, df, loc=0, scale=1)
Exponential: expon.cdf(x, loc=0, scale=1)
Chi-squared: chi2.cdf(x, df, loc=0, scale=1)
F: f.cdf(x, dfn, dfd, loc=0, scale=1)
Gamma: gamma.cdf(x, a, loc=0, scale=1)
Beta: beta.cdf(x, a, b, loc=0, scale=1)
Uniform: uniform.cdf(x, loc=0, scale=1)
Binomial: binom.cdf(k, n, p, loc=0)
Poisson: poisson.cdf(k, mu, loc=0)
```

These CDF functions are essential tools for statistical analysis, hypothesis testing, and constructing confidence intervals. They provide a way to determine the probability of a random variable falling within a specified range, given its distribution.
