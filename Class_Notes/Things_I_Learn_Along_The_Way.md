# The title says it all, Python tips I learn along the way of coding.
I have had issues importing specific variables from other scripts.
Let's say we have `script_a.py` and `script_b.py`. Inside `script_a.py`, there is variable x. But there is also a series of code that will run. I am not interested in running this code.
I just want the variable. Unfortunately, if I just type `from script_a import x` inside `script_b.py` it will not only import x but also run the whole script, which is very annoying.
In order to fix this, use `if __name__ == "__main__":`
This will ensure that whatever is inside this `if` statement will not run when calling stuff inside `script_b.py` from `script_a.py`.
```
# script_a.py
x = 42

def some_function():
    print("This is a function")

if __name__ == "__main__":
    # This code runs only when script_a.py is executed directly
    print("Script A is being run directly")
```

## Detecting when specific values are "On" and "Off" in order to get cumulative time and specific calculations.

Let's say you have a dataframe. You decide to plot time in the x axis and some other parameter in the y axis.
You want to figure out what's the maximum amount of time your y axis parameter dwells at a certain value.

For this, you can use boolean columns. One column detects when a value is either `True` or `False`, and the other column is the same boolean column but shifted by one index.

This helps the user identify where my y axis parameter changes:

```commandline
# Step 1: Find where y is 100
mask = df['y'] == 100

# Step 2: Identify the contiguous periods where y = 100
df['shifted'] = mask.shift(fill_value=False)  # Create a shifted column to detect changes

# Step 3: Create a group identifier for each contiguous block of True values
df['group'] = (mask != df['shifted']).cumsum()
```

Now, step 3 is nice because I am assigning a unique number with `.cumsum()`
everytime there is a change in y, i.e. everytime `mask != shifted`.
If `mask != shifted` then certainly, a change ocurred. 

Once I have uniquely identified where my y parameter meets my requirement, I can then use this to group by unique numbers and make my calculations:
```commandline
# Step 4: Filter for the groups where y = 100
dwell_groups = df[mask].groupby('group')

# Step 5: Calculate the duration of each dwell time
dwell_times = dwell_groups['time'].agg(lambda x: x.max() - x.min())
```


## Grabbing a specific value based on index number and column name
I have had instances where I try to pull out a specific value from a dataframe and assign it to a variable based on index number and column name. For this you can combine `.iloc[]` and `.getloc()`
```
column_name = 'A'
column_index = df.columns.get_loc('A') # Get's the index or number of column
value_in_cell = df.iloc[-1,column_index] # Can be -1 (last index) or whatever other condition you want it to be
```
## Filtering a column based on specific strings in the column names:

Example: filter columns ending with the string `a`:

```
import pandas as pd
import re

# Sample DataFrame
data = {'zebra': [1, 2, 3], 'gorilla': [4, 5, 6], 'mouse': [7, 8, 9], 'anaconda': [10, 11, 12]}
df = pd.DataFrame(data)

# Filter columns ending with 'a'
filtered_columns = df.filter(regex=r'a$') # Using $ after the string means "ends with a"
filtered_columns = df.filter(regex=r'^a') # Using ^ before the string means "starts with a"
print(filtered_columns)

# pandas.Dataframe.filter() let's you filter dataframes
# see documentation here: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.filter.html
```

