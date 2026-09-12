# Method Overloading and Method Overriding in Python

## 1. Method Overloading

### Definition

**Method overloading** means using the same method name with different parameter combinations.

Conceptually:

```text
add(a, b)
add(a, b, c)
```

The method name is the same, but the parameters are different.

### Important: Python Does Not Support Traditional Method Overloading

Python does not support traditional method overloading like Java or C++.

For example:

```python
class Calculator:

    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c
```

The second `add()` replaces the first one.

Python only keeps the latest definition of `add()`.

Therefore:

```python
c = Calculator()

c.add(10, 20)
```

produces an error because Python sees:

```python
add(self, a, b, c)
```

and `c` was not supplied.

---

## 2. Why Python Does Not Need Traditional Overloading as Much

Python is dynamically typed.

A single method can often work with different compatible types:

```python
class Calculator:

    def add(self, a, b):
        return a + b


c = Calculator()

print(c.add(10, 20))
print(c.add(10.5, 20.5))
print(c.add("Hello ", "Python"))
```

Output:

```text
30
31.0
Hello Python
```

So Python often uses flexible functions instead of defining many methods with the same name.

---

# 3. Achieving Overloading-Like Behavior in Python

Python commonly uses:

- Default arguments
- `*args`
- `**kwargs`
- Type checking
- `@overload` for type hints

---

## 3.1 Using Default Arguments

```python
class Calculator:

    def add(self, a, b, c=0):
        return a + b + c


c = Calculator()

print(c.add(10, 20))
print(c.add(10, 20, 30))
```

Output:

```text
30
60
```

For:

```python
c.add(10, 20)
```

Python uses:

```text
a = 10
b = 20
c = 0
```

For:

```python
c.add(10, 20, 30)
```

Python uses:

```text
a = 10
b = 20
c = 30
```

### When to use

Use default arguments when you have a small number of optional parameters.

---

## 3.2 Using `*args`

`*args` allows a method to accept a variable number of positional arguments.

```python
class Calculator:

    def add(self, *numbers):
        return sum(numbers)


c = Calculator()

print(c.add(10, 20))
print(c.add(10, 20, 30))
print(c.add(10, 20, 30, 40))
```

Output:

```text
30
60
100
```

For:

```python
c.add(10, 20)
```

`numbers` becomes:

```python
(10, 20)
```

For:

```python
c.add(10, 20, 30)
```

`numbers` becomes:

```python
(10, 20, 30)
```

### Remember

```text
*args → variable number of positional arguments
```

---

## 3.3 Using `**kwargs`

`**kwargs` accepts a variable number of keyword arguments.

```python
class Student:

    def show(self, **kwargs):
        for key, value in kwargs.items():
            print(key, "=", value)


s = Student()

s.show(name="Vishal")

s.show(
    name="Vishal",
    age=25,
    course="Python"
)
```

`kwargs` is a dictionary:

```python
{
    "name": "Vishal",
    "age": 25,
    "course": "Python"
}
```

### Remember

```text
*args     → positional arguments
**kwargs  → keyword arguments
```

---

## 3.4 Checking the Number of Arguments

We can manually decide what to do based on the number of arguments.

```python
class Calculator:

    def add(self, *args):

        if len(args) == 2:
            return args[0] + args[1]

        elif len(args) == 3:
            return args[0] + args[1] + args[2]

        else:
            return "Invalid number of arguments"


c = Calculator()

print(c.add(10, 20))
print(c.add(10, 20, 30))
print(c.add(10))
```

Output:

```text
30
60
Invalid number of arguments
```

This is **overloading-like behavior**, not traditional method overloading.

---

## 3.5 Checking Argument Types

Python can use `isinstance()` to choose behavior based on the type.

```python
class Printer:

    def print_data(self, data):

        if isinstance(data, int):
            print("Integer:", data)

        elif isinstance(data, str):
            print("String:", data)

        elif isinstance(data, list):
            print("List:", data)


p = Printer()

p.print_data(100)
p.print_data("Python")
p.print_data([10, 20, 30])
```

Output:

```text
Integer: 100
String: Python
List: [10, 20, 30]
```

---

# 4. `@overload` in Python

Python provides `@overload` through the `typing` module.

It is mainly used for:

- Type checkers
- IDEs
- Static analysis
- Better type hints

It does **not** create multiple runtime implementations.

Example:

```python
from typing import overload


class Calculator:

    @overload
    def add(self, a: int, b: int) -> int:
        ...

    @overload
    def add(self, a: str, b: str) -> str:
        ...

    def add(self, a, b):
        return a + b
```

The actual implementation is:

```python
def add(self, a, b):
    return a + b
```

The overloaded definitions describe the valid signatures to type-checking tools.

---

# 5. Method Overriding

## Definition

**Method overriding** occurs when a child class provides its own implementation of a method that already exists in the parent class.

Python fully supports method overriding.

Example:

```python
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


d = Dog()

d.sound()
```

Output:

```text
Dog barks
```

The parent class contains:

```python
Animal.sound()
```

The child class defines:

```python
Dog.sound()
```

The child implementation overrides the inherited implementation.

---

# 6. Why Use Method Overriding?

Overriding allows child classes to provide **specialized behavior**.

For example:

```python
class Animal:

    def sound(self):
        print("Some animal sound")


class Dog(Animal):

    def sound(self):
        print("Bark")


class Cat(Animal):

    def sound(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

Output:

```text
Bark
Meow
```

Both classes inherit from `Animal`, but each provides its own implementation of `sound()`.

This is an important example of **polymorphism**.

---

# 7. Method Overriding with `super()`

Sometimes the child method needs to execute the parent implementation as well.

Use `super()`.

```python
class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog barks")


d = Dog()

d.sound()
```

Output:

```text
Animal sound
Dog barks
```

Here:

```python
super().sound()
```

calls the parent's `sound()` method.

---

## 7.1 Overriding `__init__()`

Constructors can also be overridden.

```python
class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course


s = Student("Vishal", "Python")

print(s.name)
print(s.course)
```

Output:

```text
Vishal
Python
```

The child provides a new `__init__()`, but uses:

```python
super().__init__(name)
```

to initialize the parent part.

---

# 8. Overriding and Polymorphism

Method overriding is closely related to runtime polymorphism.

```python
class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Bark")


class Cat(Animal):

    def sound(self):
        print("Meow")


def make_sound(animal):
    animal.sound()


make_sound(Dog())
make_sound(Cat())
```

Output:

```text
Bark
Meow
```

The function doesn't need to know whether it received a `Dog` or `Cat`.

It simply calls:

```python
animal.sound()
```

The appropriate overridden method is executed.

---

# 9. Overloading vs Overriding

| Feature | Method Overloading | Method Overriding |
|---|---|---|
| Meaning | Same method name with different parameter combinations | Child changes inherited method behavior |
| Classes involved | Usually same class | Parent and child classes |
| Inheritance required | No | Yes |
| Method name | Same | Same |
| Parameters | Different signatures | Usually same/similar purpose |
| Traditional Python support | No | Yes |
| Main purpose | Different ways to call a method | Specialized child behavior |
| Common Python technique | Default arguments, `*args` | Inheritance |
| `super()` | Not related | Commonly used |
| Polymorphism | Can be related | Strongly related |

---

# 10. Easy Way to Remember

## Overloading

Think:

> **Many ways to call the same method.**

```text
Same class
     ↓
Same method name
     ↓
Different parameters
```

Example:

```python
add(a, b)
add(a, b, c)
```

In Python, use:

```python
def add(self, a, b, c=0):
```

or:

```python
def add(self, *args):
```

---

## Overriding

Think:

> **Child changes the behavior inherited from parent.**

```text
Parent
  ↓
method()
  ↓
Child
  ↓
method()  ← new implementation
```

Example:

```python
class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Bark")
```

---

# 11. Complete Example

This example shows both concepts together.

```python
class Calculator:

    # Overloading-like behavior
    def add(self, a, b, c=0):
        return a + b + c


class ScientificCalculator(Calculator):

    # Method overriding
    def add(self, a, b, c=0):
        print("Scientific Calculator")
        return a + b + c


c1 = Calculator()

print(c1.add(10, 20))
print(c1.add(10, 20, 30))


c2 = ScientificCalculator()

print(c2.add(10, 20))
```

Output:

```text
30
60
Scientific Calculator
30
```

Here:

```text
Calculator
    │
    └── add(a, b, c=0)
          │
          └── Overloading-like behavior
              using default argument


ScientificCalculator
    │
    └── add(a, b, c=0)
          │
          └── Overriding
```

---

# 12. Common Mistakes

## Mistake 1: Defining the Same Method Twice

```python
class Test:

    def show(self):
        print("Hello")

    def show(self, name):
        print(name)
```

The second method replaces the first.

Python does not keep both versions.

---

## Mistake 2: Thinking Overriding Requires Different Parameters

Overriding is about **changing inherited behavior**, not simply changing parameters.

Better example:

```python
class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Bark")
```

---

## Mistake 3: Forgetting `super()`

If the child needs the parent's implementation too:

```python
class Dog(Animal):

    def sound(self):
        super().sound()
        print("Bark")
```

Without `super()`, the parent implementation is not automatically executed when the child overrides the method.

---

# 13. Quick Cheat Sheet

```text
METHOD OVERLOADING
------------------

Meaning:
Same method name + different parameters

Python:
Traditional overloading ❌

Common alternatives:
Default arguments
*args
**kwargs
Type checking
@overload for type hints
```

```text
METHOD OVERRIDING
-----------------

Meaning:
Child class provides a new implementation
of a method inherited from the parent.

Python:
Fully supported ✅

Usually involves:
Parent class
    ↓
Child class
    ↓
Same method name
    ↓
New implementation
```

---

# 14. Final Difference

```text
                 OVERLOADING
                      │
                      ↓
          "How many ways can
           I call this method?"
                      │
                      ↓
             Different inputs


                 OVERRIDING
                      │
                      ↓
          "How should the child
           implement this method?"
                      │
                      ↓
             Different behavior
```

### One-line memory trick

> **Overloading = same method, different ways to call it.**

> **Overriding = same inherited method, different implementation.**

### Python-specific rule

> **Python does not support traditional method overloading by defining the same method multiple times. The latest definition replaces the previous one. Python does support method overriding through inheritance.**
