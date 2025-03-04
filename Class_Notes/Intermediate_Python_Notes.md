# Notes regarding intermediate Python tools
## Looping data structures
### Arrays
To loop through a dictionary, use this:
`for key, val in my_dict.items() :`

To loop through a NumPy array, use this:
`for val in np.nditer(my_array) :`

To loop through rows and columns in a DataFrame:
`for row, column in df.iterrows():`

The best way to add a column to a DataFrame is with apply:
`df['NEW_COLUMN] = df['OLD_COLUMN'].apply()`

When looping for 'specific times' use `range()` with the number of times you would like to loop inside the parenthesis


# Data Manipulation with Pandas

## Cool attributes to use:

### DF Attributes

`df.head()` shows the first six rows of the DF

`df.columns()` and `df.index()` shows the number of rows and columns

## Tip: Not all attributes need parenthesis:

Whether you use parentheses depends on whether the attribute is a method (function) or a variable (property).

Methods (functions) require parentheses because they need to be called.

```
class Example:
    def greet(self):
        return "Hello!"
obj = Example()
print(obj.greet())  # ✅ Calls the method -> "Hello!"
print(obj.greet)    # ❌ Prints the method object, not the result
```

Variables (properties) do not need parentheses because they just store values.

```
class Example:
    def __init__(self):
        self.message = "Hello!"

obj = Example()
print(obj.message)  # ✅ Accesses the attribute -> "Hello!"
```

If you're unsure whether an attribute needs parentheses, you can check if it's callable using:

`callable(obj.attribute)`.

# Using Pandas

## Using the agg()
This is a nice attribute you can use to apply one or more custom or existing function to your dataframe.
Example:
```
df['column'].agg([function1, function2])
```
Remember to always include list type [] square brackets when doing more than one function or activity

## Counting values from a DF:
You can use this to sort values you see on a dataframe:
```
df_sorted = df['column'].value_counts()
```
Where:
```
Series.value_counts(
    normalize=False, 
    sort=True, 
    ascending=False, 
    bins=None, 
    dropna=True
)
```

## Using the `.groupby()` and `.agg()` attributes to summarize dataframes with functions for statistics:

If you have a dataframe `df` and you would like to summarize statistics grouping specific columns and statistical calculations, you can use the following:
```
stats = df.groupby('column_to_group')['column_to_perform_calcs'].agg(min,max,mean)
```

This is basically grouping the dataframe by a specific column and then calculating the min, max, and mean of the given column inside the square brackets. (I know, this terminology is confusing but this is how the `groupby()` attribute works...)

## Example of creating a Pivot Table:
```
import pandas as pd
import numpy as np

# Example of creating a pivot table
pivot_table = df.pivot_table(values='Weight', index='Color', aggfunc=np.median)
```

## Filtering a DataFrame based on a list of column values with `.isin()`:
```
# where:
list_of_values_in_column = ['a','b','c']
df[df['column'].isin(list_of_values_in_column)])


```
## Shorter way to generate dictionaries:
This is usefull when using an attribute with multiple keys and items where a dictionary is needed:
In this case, `dict(facecolor='lightgray', alpha=0.5)` is the same as `{'facecolor':'lightgray','alpha':0.5}`
Very handy!


## Plotting missing values
Creates a bar chart that highlights which values are missing!
```
import matplotlib.pyplot as plt
df.isna().sum().plot(kind="bar")
plt.show()
```

## Sorting Values
Read more about it here:
`https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html`

## Best way to rename a column from a DF

If you don’t want to create a new DataFrame and instead modify it directly:
```
df.rename(columns={"A": "Alpha", "B": "Beta"}, inplace=True)
```
If you want to create a new DF:

```
import pandas as pd

df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

df = df.rename(columns={"A": "Alpha"})  # Renaming column "A" to "Alpha"
print(df)
```

or rename multiple columns:

```
df = df.rename(columns={"A": "Alpha", "B": "Beta"})
print(df)
```

You can also rename using a function:
```
df.columns = df.columns.str.lower()
```

If you would like to convert a dictionary into a Dataframe, you can use this:

```
df = pd.DataFrame([dict])
```
Square brackets `[]` ensure that the dictionary is in `list` format since dataframe creation expects multiple values.

Also, sometimes you may want to rename the index from the standard formatting Pandas uses `0` to anything you want.
For this, use the following:
```
df.index = ['A']
```
Square brackets `[]` ensure we follow the Data Frame creation methodology.

If you want to create an array that goes from x to y, splitted by z you can use `np.linspace`:
```commandline
array = np.linspace(1,100,2)
```

This generates an array from 1 to 100 splitted into two's (2,4,6, etc.)

## Getting the shape of a DataFrame with Numpy attribute `.shape`
You can use this attribute that returns a tuple with the shape of the dataframe (number of rows, numbers of columns):

```
df.shape  #Returns (rows, columns)
```
