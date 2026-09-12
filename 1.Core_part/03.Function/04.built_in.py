# 1. """ """ — Docstring

# A docstring is a string written inside a function, class, or module to describe what it does.
# """ """ is actually a triple-quoted string. When placed as 
# the first statement inside a function/class/module, Python treats it as its docstring.

def add(a, b):
    """This function adds two numbers."""
    return a + b

print(add.__doc__)  # Give me the documentation of the add function.
print(add.__name__) # give me the name of the add function."


# __name__ - It tells you the name of the current module/file.

