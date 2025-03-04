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
