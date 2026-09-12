# Decorators in Python

A **decorator** is a function that adds extra behavior to another function **without changing its original code**.

## Basic Example

```python
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


@decorator
def hello():
    print("Hello!")


hello()
```

### Output

```text
Before function
Hello!
After function
```

## How `@decorator` Works

This:

```python
@decorator
def hello():
    print("Hello!")
```

is the same as:

```python
def hello():
    print("Hello!")

hello = decorator(hello)
```

So, `@decorator` is simply **syntactic sugar**.

---

## Decorator with Arguments

Use `*args` and `**kwargs` when the function can have different arguments.

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Function started")

        result = func(*args, **kwargs)

        print("Function ended")
        return result

    return wrapper


@decorator
def add(a, b):
    return a + b


print(add(10, 20))
```

### Output

```text
Function started
Function ended
30
```

## Real-World Use Cases

Decorators are commonly used for:

- Logging
- Authentication
- Authorization
- Validation
- Timing function execution
- Caching
- Error handling
- Access control

## Simple Flow

```text
Original Function
       ↓
   Decorator
       ↓
    Wrapper
       ↓
Extra Behavior + Original Function
```

## Key Point

> A decorator allows you to **modify or extend a function's behavior without modifying its source code**.

# `@wraps` in Python

`@wraps(func)` is used with decorators to **preserve the metadata of the original function**.

```python
from functools import wraps


def my_decorators(func):
    @wraps(func)
    def wrapper():
        print("before function execution ")
        func()
        print("After Function executed")
        
    return wrapper

@my_decorators
def greet():
    print("hello , this is decorators")

greet()    
print(greet.__name__)

```

**Without @wraps**

```python
print(greet.__name__)
# wrapper

```

**With @wraps**

```python

print(greet.__name__)
# greet

```

## Key Point

> @wraps(func) tells Python that the wrapper is wrapping the original func, so the original function's metadata is preserved.

# Authentication Decorator

The `auth_Admin` decorator checks whether the user has the required role before allowing the function to execute.

```python
from functools import wraps


def auth_Admin(func):
    
    @wraps(func)
    def wrapper(role):
        if role != "admin":
            print("Access Denied : Admins only")
            return None
        else :
            return func(role)
    return wrapper


@auth_Admin
def teaching(role):
    print("Access Granted to head Master Admin")
    
teaching("admin")
teaching("user")

```
### key points : 
> - role == "admin" → Original function executes.
> - role != "admin" → Access is denied.
> - func(role) → Calls the original decorated function.
> - return None → Stops execution when access is denied.
