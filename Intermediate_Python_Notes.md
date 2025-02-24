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
