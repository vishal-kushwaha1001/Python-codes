# `del` vs `__del__` in Python

## `del`

`del` is used to delete a variable, list item, or object attribute.

``` python
x = 10
del x

numbers = [10, 20, 30]
del numbers[1]
print(numbers)  # [10, 30]
```

## `__del__()`

`__del__()` is a special method that may be called when an object is
being destroyed.

``` python
class Student:
    def __del__(self):
        print("Object destroyed")

student = Student()
del student
```

## Difference

  -----------------------------------------------------------------------
  `del`                               `__del__()`
  ----------------------------------- -----------------------------------
  Python statement                    Special method

  Deletes references/items/attributes Runs during object finalization

  Used explicitly                     Called by Python when appropriate
  -----------------------------------------------------------------------

**Remember:** `del` removes a reference; `__del__()` is related to
object destruction.
