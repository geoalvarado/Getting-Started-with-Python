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

## Using the agg() (aggregate attribute from Pandas)
This is a nice attribute you can use to apply one or more custom or existing function to your dataframe.
Example:
```
df['column'].agg([function1, function2])
```
Remember to always include list type [] square brackets when doing more than one function or activity


