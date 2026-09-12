# Error Handling in Python

Error handling allows a program to handle runtime errors gracefully instead of crashing.

## 1. Types of Errors

### Syntax Error

Occurs when Python syntax is incorrect.

```python
if age > 18
    print("Adult")
```

```text
SyntaxError
```

### Exceptions

Exceptions occur while the program is running.

```python
result = 10 / 0
```

```text
ZeroDivisionError
```

Common exceptions:

| Exception | Example |
|---|---|
| `ValueError` | `int("abc")` |
| `TypeError` | `"10" + 5` |
| `ZeroDivisionError` | `10 / 0` |
| `IndexError` | `arr[10]` |
| `KeyError` | `data["missing"]` |
| `FileNotFoundError` | Opening a missing file |
| `AttributeError` | Using a missing attribute |
| `NameError` | Using an undefined variable |

---

# 2. `try` and `except`

Use `try` for code that may cause an exception and `except` to handle it.

```python
try:
    result = 10 / 0

except:
    print("Something went wrong")
```

Output:

```text
Something went wrong
```

### Better: Catch Specific Exceptions

```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")
```

Catching specific exceptions is preferred because it makes the code clearer.

---

# 3. Getting the Error Message

Use `as` to store the exception object.

```python
try:
    num = int("hello")

except ValueError as e:
    print(e)
```

Example output:

```text
invalid literal for int() with base 10: 'hello'
```

You can also inspect it:

```python
print(type(e))
```

---

# 4. Multiple `except` Blocks

Different exceptions can have different handlers.

```python
try:
    num = int(input("Enter number: "))
    result = 100 / num

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

- Invalid text → `ValueError`
- `0` → `ZeroDivisionError`

---

# 5. Handling Multiple Exceptions Together

If different exceptions need the same handling:

```python
try:
    result = 10 / 0

except (ZeroDivisionError, ValueError):
    print("Invalid operation")
```

You can also get the exception:

```python
except (ValueError, TypeError) as e:
    print(e)
```

---

# 6. `else`

The `else` block runs **only when no exception occurs**.

```python
try:
    num = int(input("Enter number: "))

except ValueError:
    print("Invalid number")

else:
    print("You entered:", num)
```

Flow:

```text
try
 |
 +-- Error ------> except
 |
 +-- No Error ---> else
```

---

# 7. `finally`

The `finally` block **always executes**, whether an exception occurs or not.

```python
try:
    result = 10 / 2

except ZeroDivisionError:
    print("Cannot divide")

finally:
    print("Program finished")
```

Even if there is an error:

```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide")

finally:
    print("Program finished")
```

Output:

```text
Cannot divide
Program finished
```

---

# 8. Complete `try-except-else-finally`

```python
try:
    num = int(input("Enter number: "))
    result = 100 / num

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)

finally:
    print("Execution completed")
```

### Meaning

```text
try      → Risky code
except   → Handle error
else     → Runs if there is no error
finally  → Always runs
```

---

# 9. `raise`

`raise` is used to manually create an exception.

```python
age = 15

if age < 18:
    raise ValueError("Age must be 18 or above")
```

Output:

```text
ValueError: Age must be 18 or above
```

### `raise` with `try-except`

```python
try:
    age = 15

    if age < 18:
        raise ValueError("Age must be 18 or above")

except ValueError as e:
    print("Error:", e)
```

Output:

```text
Error: Age must be 18 or above
```

### Easy way to remember

```text
raise  → Create/report an error
except → Handle an error
```

---

# 10. Custom Exceptions

You can create your own exception class.

```python
class InsufficientBalanceError(Exception):
    pass
```

Use it:

```python
balance = 1000
withdraw = 2000

try:
    if withdraw > balance:
        raise InsufficientBalanceError("Insufficient balance")

except InsufficientBalanceError as e:
    print(e)
```

Output:

```text
Insufficient balance
```

Custom exceptions are useful in larger applications.

---

# 11. Custom Exception with `__init__`

A custom exception can store additional information.

```python
class InsufficientBalanceError(Exception):

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

        super().__init__(
            f"Balance: {balance}, Withdrawal: {amount}"
        )
```

Usage:

```python
balance = 1000
amount = 2000

try:
    if amount > balance:
        raise InsufficientBalanceError(balance, amount)

except InsufficientBalanceError as e:
    print(e)
```

---

# 12. Exception Hierarchy

Python exceptions are organized into a hierarchy.

```text
BaseException
│
├── SystemExit
├── KeyboardInterrupt
│
└── Exception
    │
    ├── ValueError
    ├── TypeError
    ├── ArithmeticError
    │   └── ZeroDivisionError
    │
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    │
    ├── OSError
    │   └── FileNotFoundError
    │
    └── ...
```

Most application-level exceptions inherit from:

```python
Exception
```

---

# 13. `except Exception`

You can catch most normal runtime exceptions using:

```python
try:
    result = 10 / 0

except Exception as e:
    print("Error:", e)
```

However, if you know the exact exception, prefer the specific exception:

```python
except ValueError:
    ...
```

instead of:

```python
except Exception:
    ...
```

---

# 14. Bare `except`

You may see:

```python
try:
    risky_operation()

except:
    print("Error")
```

Avoid this in normal application code because it can catch exceptions you may not intend to handle.

Prefer:

```python
except Exception as e:
    print(e)
```

or, better:

```python
except ValueError as e:
    print(e)
```

---

# 15. Exception Chaining

Sometimes one exception causes another exception.

Python supports exception chaining using:

```python
raise NewException(...) from original_exception
```

Example:

```python
try:
    num = int("abc")

except ValueError as e:
    raise RuntimeError("Failed to process number") from e
```

This preserves the original cause of the error.

---

# 16. `finally` and Resources

`finally` is useful for cleanup.

```python
file = None

try:
    file = open("data.txt", "r")
    data = file.read()

except FileNotFoundError:
    print("File not found")

finally:
    if file:
        file.close()
```

For files, a better approach is usually `with`:

```python
with open("data.txt", "r") as file:
    data = file.read()
```

The file is automatically closed.

---

# 17. Error Handling in Functions

```python
def divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        return "Cannot divide by zero"


print(divide(10, 2))
print(divide(10, 0))
```

Output:

```text
5.0
Cannot divide by zero
```

---

# 18. Let the Caller Handle the Error

A function does not always need to handle the exception itself.

```python
def divide(a, b):
    return a / b
```

The caller can handle it:

```python
try:
    result = divide(10, 0)

except ZeroDivisionError:
    print("Cannot divide by zero")
```

This can be useful when the caller needs to decide what should happen after the error.

---

# 19. Error Handling in Classes

Example:

```python
class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount
        return self.balance
```

Usage:

```python
account = BankAccount(1000)

try:
    account.withdraw(1500)

except ValueError as e:
    print(e)
```

Output:

```text
Insufficient balance
```

---

# 20. Practical Banking Example

```python
class InsufficientBalanceError(Exception):
    pass


class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        if amount > self.balance:
            raise InsufficientBalanceError(
                "Insufficient balance"
            )

        self.balance -= amount
        return self.balance


account = BankAccount(5000)

try:
    amount = int(input("Enter withdrawal amount: "))

    balance = account.withdraw(amount)

except ValueError as e:
    print("Invalid input:", e)

except InsufficientBalanceError as e:
    print("Transaction failed:", e)

else:
    print("Withdrawal successful")
    print("Remaining balance:", balance)

finally:
    print("Transaction completed")
```

Flow:

```text
User Input
    ↓
  try
    ↓
Validation
    ↓
raise exception if invalid
    ↓
 except
    ↓
Handle error

No error
    ↓
  else
    ↓
Success

finally
    ↓
Always execute
```

---

# 21. `assert`

`assert` checks an assumption.

```python
age = 15

assert age >= 18, "Age must be 18 or above"
```

Output:

```text
AssertionError: Age must be 18 or above
```

`assert` is mainly useful for debugging and internal assumptions.

For user input validation, prefer:

```python
if age < 18:
    raise ValueError("Age must be 18 or above")
```

---

# 22. Logging Errors

Real applications often use `logging` instead of only `print()`.

```python
import logging

logging.basicConfig(level=logging.ERROR)

try:
    result = 10 / 0

except ZeroDivisionError:
    logging.exception("Division failed")
```

`logging.exception()` is especially useful inside an `except` block because it includes traceback information.

---

# 23. EAFP vs LBYL

### EAFP

**Easier to Ask Forgiveness than Permission**

Try the operation and handle the exception if it fails.

```python
try:
    print(data[key])

except KeyError:
    print("Key doesn't exist")
```

### LBYL

**Look Before You Leap**

Check first, then perform the operation.

```python
if key in data:
    print(data[key])
else:
    print("Key doesn't exist")
```

Python often uses EAFP when directly attempting the operation is simpler.

---

# 24. Common Mistakes

### Don't silently ignore errors

Avoid:

```python
try:
    risky_code()

except:
    pass
```

The error completely disappears.

### Don't catch everything unnecessarily

Instead of:

```python
except Exception:
    print("Error")
```

prefer a specific exception when possible:

```python
except ValueError:
    print("Invalid value")
```

### Don't use exceptions for ordinary decisions

Use:

```python
if age >= 18:
    print("Allowed")
```

instead of intentionally raising and catching an exception for a normal condition.

---

# 25. Quick Reference

| Keyword | Purpose |
|---|---|
| `try` | Code that may raise an exception |
| `except` | Handle an exception |
| `else` | Runs when no exception occurs |
| `finally` | Always runs |
| `raise` | Manually raise an exception |
| `assert` | Check an assumption |
| `Exception` | Base class for most normal exceptions |

## Basic Pattern

```python
try:
    result = risky_operation()

except ValueError as e:
    print("Invalid value:", e)

except ZeroDivisionError as e:
    print("Cannot divide:", e)

else:
    print("Success:", result)

finally:
    print("Done")
```

## Remember

```text
try      → Try the operation
except   → Handle the failure
else     → Handle success
finally  → Always execute
raise    → Create/propagate an exception
assert   → Check an assumption
```
