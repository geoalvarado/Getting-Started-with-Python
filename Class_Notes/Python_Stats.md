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
	•	n → Number of trials (e.g., number of coin flips)
	•	p → Probability of success in each trial (e.g., probability of getting heads)
	•	size → Number of random samples to generate (default is 1)

Use Cases:
	•	Simulating coin flips (or any repeated binary outcome)
	•	Modeling success/failure experiments (e.g., number of defective items in a batch)
	•	Testing probabilistic algorithms (e.g., A/B testing, reliability modeling)

Would you like a specific example applied to something you’re working on?
