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
