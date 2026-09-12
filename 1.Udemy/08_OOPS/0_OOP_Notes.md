# OOPs in Python — Complete Notes

> **OOPs = Object-Oriented Programming System**
>
> OOP is a programming approach where a program is designed around **objects** that contain **data (attributes)** and **behavior (methods)**.

---

# 1. What is OOP?

In procedural programming, we generally organize code around functions.

In OOP, we organize code around **objects**.

For example, a real-world `Student` can have:

- Data → name, age, marks
- Behavior → study(), attend_class(), display_result()

```python
class Student:
    def study(self):
        print("Student is studying")

student1 = Student()

student1.study()
```

Here:

- `Student` → class
- `student1` → object
- `study()` → method

---

# 2. Why Use OOP?

OOP is useful because it provides:

- Code reusability
- Better organization
- Data protection
- Easier maintenance
- Modularity
- Abstraction
- Polymorphism
- Inheritance

OOP becomes especially useful when applications become large.

---

# 3. Class

A **class** is a blueprint/template for creating objects.

```python
class Student:
    pass
```

The class itself does not represent one specific student. It defines what a student object can contain.

Example:

```python
class Student:
    name = "Vishal"
    age = 22
```

---

# 4. Object

An **object** is an instance of a class.

```python
class Student:
    name = "Vishal"

student1 = Student()

print(student1.name)
```

Output:

```text
Vishal
```

We can create multiple objects from the same class:

```python
student1 = Student()
student2 = Student()
student3 = Student()
```

Each object is a separate instance.

---

# 5. Class vs Object

| Class | Object |
|---|---|
| Blueprint | Actual instance |
| Logical definition | Real entity |
| Does not represent one specific instance | Represents a specific instance |
| `Student` | `student1` |
| Defines attributes/methods | Uses attributes/methods |

Example:

```python
class Car:
    pass

car1 = Car()
car2 = Car()
```

`Car` is the class.

`car1` and `car2` are objects.

---

# 6. Attributes

Attributes are variables associated with an object or class.

There are mainly two important types:

1. Instance attributes
2. Class attributes

---

## 6.1 Instance Attributes

Instance attributes belong to a particular object.

They are usually created using `self`.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Vishal", 22)
student2 = Student("Aman", 20)

print(student1.name)
print(student2.name)
```

Output:

```text
Vishal
Aman
```

Each object has its own `name` and `age`.

---

## 6.2 Class Attributes

A class attribute belongs to the class and is shared by instances unless an instance overrides it.

```python
class Student:
    school = "ABC School"

student1 = Student()
student2 = Student()

print(student1.school)
print(student2.school)
```

Both objects can access the same class attribute.

---

# 7. `__init__()` Constructor

`__init__()` is commonly called the **constructor** in Python.

It runs automatically when an object is created.

All classes have a function called  `__init__()` , which is always executed when the class is beging initiated.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Vishal", 22)
```

When this executes:

```python
Student("Vishal", 22)
```

Python automatically calls:

```python
__init__(student1, "Vishal", 22)
```

Conceptually, `self` refers to the newly created object.

### Important

Strictly speaking, `__new__()` creates the object and `__init__()` initializes it. In everyday Python discussions, `__init__()` is commonly called the constructor.

---

# 8. `self`

`self` refers to the **current object**.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

student1 = Student("Vishal")
student1.display()
```

Here:

```python
self.name
```

means:

> the `name` attribute belonging to the current object.

`self` is not a special keyword. It is a naming convention, but you should always use `self` by convention.

---

# 9. Methods

A method is a function defined inside a class.

```python
class Student:
    def study(self):
        print("Student is studying")

student1 = Student()
student1.study()
```

---

# 10. Types of Methods

Python classes commonly use:

1. Instance methods
2. Class methods
3. Static methods

---

## 10.1 Instance Method

Works with a particular object.

```python
class Student:
    def display(self):
        print("Hello Student")

student1 = Student()
student1.display()
```

It normally receives `self`.

---

## 10.2 Class Method

A class method works with the class rather than a particular instance.

Use `@classmethod`.

```python
class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

Student.change_school("XYZ School")

print(Student.school)
```

`cls` refers to the class.

---

## 10.3 Static Method

A static method does not automatically receive `self` or `cls`.

Use `@staticmethod`.

```python
class Math:

    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(10, 20))
```

Use static methods when the operation logically belongs to the class but does not need object/class state.

---

# 11. Instance vs Class vs Static Method

| Method | First Parameter | Works With |
|---|---|---|
| Instance method | `self` | Object |
| Class method | `cls` | Class |
| Static method | None automatically | Neither object nor class state |

Example:

```python
class Demo:

    def instance_method(self):
        print("Instance method")

    @classmethod
    def class_method(cls):
        print("Class method")

    @staticmethod
    def static_method():
        print("Static method")
```

---

# 12. Four Pillars of OOP

The four major pillars are:

1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

---

# 13. Encapsulation

**Encapsulation** means keeping data and the methods that operate on that data together, while controlling how the internal state is accessed or changed.

Python uses naming conventions and mechanisms such as:

- Public
- `_protected` convention
- `__private` name mangling
- Properties

---

## 13.1 Public Members

Public members can be accessed normally.

```python
class Student:
    def __init__(self):
        self.name = "Vishal"

student = Student()

print(student.name)
```

---

## 13.2 Protected Convention `_name`

A single underscore indicates:

> This member is intended for internal/subclass use.

It is a convention, not strict access control.

```python
class Student:
    def __init__(self):
        self._marks = 80

student = Student()

print(student._marks)
```

Python still allows access.

---

## 13.3 Private Name Mangling `__name`

Double underscore triggers **name mangling**.

```python
class Student:
    def __init__(self):
        self.__marks = 80

student = Student()

# print(student.__marks)  # AttributeError
```

Internally, Python changes the name approximately to:

```text
_Student__marks
```

So this can technically be accessed:

```python
print(student._Student__marks)
```

But this is generally not the intended public interface.

---

# 14. Getter and Setter

A getter reads data.

A setter changes data, usually after validation.

```python
class Student:
    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")

student = Student(80)

print(student.get_marks())

student.set_marks(95)

print(student.get_marks())
```

---

# 15. `@property`

Python provides a cleaner way to create getter/setter-style interfaces.

```python
class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            raise ValueError("Marks must be between 0 and 100")

student = Student(80)

print(student.marks)

student.marks = 95

print(student.marks)
```

This lets us write:

```python
student.marks
```

instead of:

```python
student.get_marks()
```

---

# 16. Inheritance

**Inheritance** allows one class to reuse and extend another class.

The existing class is commonly called:

- Parent class
- Base class
- Superclass

The new class is commonly called:

- Child class
- Derived class
- Subclass

Example:

```python
class Animal:
    def eat(self):
        print("Animal eats")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


dog = Dog()

dog.eat()
dog.bark()
```

`Dog` inherits `eat()` from `Animal`.

---

# 17. Types of Inheritance

Python supports several inheritance patterns:

1. Single inheritance
2. Multiple inheritance
3. Multilevel inheritance
4. Hierarchical inheritance
5. Hybrid inheritance

---

## 17.1 Single Inheritance

One child inherits from one parent.

```python
class Animal:
    pass


class Dog(Animal):
    pass
```

---

## 17.2 Multiple Inheritance

One class inherits from multiple parents.

```python
class Father:
    def skills(self):
        print("Driving")


class Mother:
    def talent(self):
        print("Cooking")


class Child(Father, Mother):
    pass


child = Child()

child.skills()
child.talent()
```

---

## 17.3 Multilevel Inheritance

Inheritance occurs in multiple levels.

```python
class Grandparent:
    def house(self):
        print("House")


class Parent(Grandparent):
    def car(self):
        print("Car")


class Child(Parent):
    def bike(self):
        print("Bike")


child = Child()

child.house()
child.car()
child.bike()
```

---

## 17.4 Hierarchical Inheritance

Multiple child classes inherit from the same parent.

```python
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    pass


class Cat(Animal):
    pass
```

Both `Dog` and `Cat` inherit from `Animal`.

---

## 17.5 Hybrid Inheritance

A combination of multiple inheritance patterns.

```text
       A
      / \
     B   C
      \ /
       D
```

This can lead to the **diamond inheritance** problem.

Python handles method lookup using MRO.

---



# 18. `super()`

`super()` is used to access behavior from a parent class according to Python's method resolution order.

Example:

```python
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


dog = Dog("Tommy", "Labrador")

print(dog.name)
print(dog.breed)
```

Without `super()`, you might have to repeat the parent initialization logic.

---

# 19. Polymorphism

**Polymorphism** means "many forms."

The same interface or operation can behave differently for different objects.

There are two types of polymorphism :

1. Method Overriding 
2. Methord Overloding


Example:

```python
class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```

Output:

```text
Bark
Meow
```

The same:

```python
animal.sound()
```

produces different behavior depending on the object.

---

# 21.1  Method Overriding

When a child class provides its own implementation of a method inherited from the parent, it is called **method overriding**.

```python
class Animal:
    def sound(self):
        print("Animal sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


dog = Dog()

dog.sound()
```

Output:

```text
Bark
```

---

# 21.2 Method Overloding

**Method overloading** means having multiple methods with the **same name** but different numbers or types of parameters.

For example, Java supports:

```java
add(int a, int b)
add(int a, int b, int c)
```

> Python does **not support traditional method overloading** like Java or C++.

---

### What Happens in Python?

```python
class Calculator:

    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c
```

The second `add()` **replaces** the first one.

```python
c = Calculator()
c.add(10, 20)
```

This causes an error because the surviving method requires `a`, `b`, and `c`.

```text
TypeError: Calculator.add() missing 1 required positional argument: 'c'
```

Python commonly achieves overloading-like behavior using:

- Default arguments
- `*args`
- `**kwargs`
- Type checking
- `@overload` for type hints

---

# 22. Operator Overloading

Python allows classes to define how operators behave for their objects.

This is done using special methods, also called **dunder methods**.

Example:

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)


a = Number(10)
b = Number(20)

c = a + b

print(c.value)
```

Output:

```text
30
```

Here:

```python
a + b
```

internally uses:

```python
a.__add__(b)
```

---

# 23. Common Dunder Methods

Dunder means **double underscore**.

Common examples:

| Method | Purpose |
|---|---|
| `__init__` | Initialize object |
| `__new__` | Create object |
| `__str__` | User-friendly string |
| `__repr__` | Developer-oriented representation |
| `__len__` | `len(obj)` |
| `__add__` | `+` |
| `__sub__` | `-` |
| `__mul__` | `*` |
| `__eq__` | `==` |
| `__lt__` | `<` |
| `__gt__` | `>` |
| `__contains__` | `in` |
| `__iter__` | Iteration |
| `__next__` | Next item |

---

# 24. `__str__()` vs `__repr__()`

```python
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student: {self.name}"

    def __repr__(self):
        return f"Student({self.name!r})"


student = Student("Vishal")

print(student)
print(repr(student))
```

### `__str__()`

Used for a readable representation intended mainly for users.

### `__repr__()`

Used for an unambiguous/developer-oriented representation.

---

# 25. Abstraction

**Abstraction** means exposing the essential interface while hiding implementation details.

Python provides abstract base classes through the `abc` module.

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Bark")


dog = Dog()
dog.sound()
```

Because `Animal` has an abstract method, it cannot normally be instantiated until the abstract requirements are implemented.

---

# 26. Abstract Class

An abstract class defines a common interface for subclasses.

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class Card(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Card")
```

Now different payment classes follow the same interface.

---

# 27. Composition

Composition means building a class using objects of other classes.

It represents a strong **has-a** relationship.

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()


car = Car()

car.start()
```

A `Car` **has an** `Engine`.

---

# 28. Aggregation

Aggregation is also a **has-a** relationship, but the contained object can exist independently.

```python
class Teacher:
    def teach(self):
        print("Teaching")


class School:
    def __init__(self, teacher):
        self.teacher = teacher


teacher = Teacher()
school = School(teacher)
```

The `Teacher` object exists independently of the `School` object.

---

# 29. Composition vs Inheritance

### Inheritance

Represents:

```text
IS-A
```

Example:

```text
Dog IS-A Animal
```

```python
class Dog(Animal):
    pass
```

### Composition

Represents:

```text
HAS-A
```

Example:

```text
Car HAS-A Engine
```

```python
class Car:
    def __init__(self):
        self.engine = Engine()
```

A useful design rule:

> Prefer composition over inheritance when inheritance does not represent a genuine subtype relationship.

---

# 30. Association

Association means two independent objects are related or interact.

Example:

```python
class Teacher:
    def teach(self, student):
        print("Teaching", student.name)


class Student:
    def __init__(self, name):
        self.name = name


student = Student("Vishal")
teacher = Teacher()

teacher.teach(student)
```

Teacher and Student can exist independently.

---

# 31. Instance Variables vs Class Variables

```python
class Employee:
    company = "ABC"

    def __init__(self, name):
        self.name = name


e1 = Employee("Aman")
e2 = Employee("Vishal")
```

Here:

```text
company → class variable
name    → instance variable
```

`company` is shared through the class unless shadowed.

`name` belongs separately to each instance.

---

# 32. Class Variable Modification

```python
class Employee:
    company = "ABC"


e1 = Employee()
e2 = Employee()

Employee.company = "XYZ"

print(e1.company)
print(e2.company)
```

Both see the updated class attribute.

But:

```python
e1.company = "PQR"
```

creates an instance attribute named `company` on `e1`, which shadows the class attribute for that instance.

---

# 33. Object Identity

Every object has an identity.

```python
class Student:
    pass


a = Student()
b = Student()

print(a is b)
```

Output:

```text
False
```

`is` checks whether two references point to the same object.

`==` checks equality according to the object's equality behavior.

---

# 34. `is` vs `==`

```python
a = [1, 2]
b = [1, 2]

print(a == b)
print(a is b)
```

Output:

```text
True
False
```

Why?

- `a == b` → values are equal
- `a is b` → they are different objects

---

# 35. Method Resolution Order (MRO)

MRO determines the order in which Python searches classes for an attribute or method.

```python
class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")


class C(A):
    def show(self):
        print("C")


class D(B, C):
    pass


d = D()

d.show()

print(D.mro())
```

Python uses the **C3 linearization** algorithm to calculate MRO.

---

# 36. MRO Example

For:

```text
       A
      / \
     B   C
      \ /
       D
```

A simplified MRO is:

```text
D → B → C → A → object
```

Check it with:

```python
print(D.mro())
```

or:

```python
print(D.__mro__)
```

---

# 37. `super()` and MRO

`super()` does not simply mean "my direct parent."

It follows the MRO.

Example:

```python
class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")
        super().show()


class C(B):
    def show(self):
        print("C")
        super().show()


c = C()

c.show()
```

Output:

```text
C
B
A
```

---

# 38. Multiple Inheritance and Cooperative `super()`

For multiple inheritance, classes should generally cooperate with `super()` rather than directly naming a parent.

```python
class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")
        super().show()


class C(A):
    def show(self):
        print("C")
        super().show()


class D(B, C):
    def show(self):
        print("D")
        super().show()


d = D()
d.show()
```

The MRO controls the chain.

---

# 39. Encapsulation with Properties

A common Pythonic pattern is:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value


account = BankAccount(1000)

print(account.balance)

account.balance = 2000
```

The property provides a controlled interface.

---

# 40. Read-Only Property

A property without a setter can behave as read-only through the normal interface.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2


circle = Circle(5)

print(circle.area)
```

Trying:

```python
circle.area = 100
```

raises an error because no setter is defined.

---

# 41. Inheritance with `__init__`

If a child defines its own `__init__()`, the parent's `__init__()` is not automatically called.

```python
class Parent:
    def __init__(self):
        print("Parent")


class Child(Parent):
    def __init__(self):
        print("Child")
```

To call the parent initialization:

```python
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child")
```

---

# 42. Method Overloading in Python

Traditional compile-time method overloading like Java/C++ is **not supported in the same way**.

This:

```python
class Calculator:

    def add(self, a):
        return a

    def add(self, a, b):
        return a + b
```

does not create two overloaded methods.

The second definition replaces the first.

Python commonly achieves flexible arguments using:

- Default arguments
- `*args`
- `**kwargs`
- `functools.singledispatch` in suitable cases

Example:

```python
class Calculator:
    def add(self, a, b=0):
        return a + b


calc = Calculator()

print(calc.add(10))
print(calc.add(10, 20))
```

---

# 43. Method Overriding vs Overloading

| Overriding | Overloading |
|---|---|
| Usually involves inheritance | Same class/interface idea |
| Child changes inherited behavior | Multiple call signatures |
| Supported naturally | Not traditional Java-style in Python |
| Runtime polymorphism | Often achieved with defaults/`*args` etc. |

---

# 44. Dynamic Typing and Polymorphism

Python determines types at runtime.

```python
def calculate_area(shape):
    return shape.area()
```

Any object that provides a compatible `area()` method can work.

This is one reason Python code can be highly flexible.

---

# 45. `isinstance()`

Checks whether an object is an instance of a class or its subclasses.

```python
class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
```

Output:

```text
True
True
```

---

# 46. `issubclass()`

Checks whether one class is a subclass of another.

```python
class Animal:
    pass


class Dog(Animal):
    pass


print(issubclass(Dog, Animal))
```

Output:

```text
True
```

---

# 47. Object Lifecycle

A simplified object lifecycle is:

```text
Class definition
      ↓
Object creation
      ↓
__new__()
      ↓
__init__()
      ↓
Object used
      ↓
Object becomes unreachable
      ↓
Garbage collection / cleanup
```

`__del__()` exists, but it should not generally be relied upon for critical resource cleanup.

For files, sockets, locks, database connections, etc., prefer context managers such as `with`.

---

# 48. `__new__()` vs `__init__()`

```python
class Student:
    def __new__(cls, name):
        print("Creating object")
        return super().__new__(cls)

    def __init__(self, name):
        print("Initializing object")
        self.name = name


student = Student("Vishal")
```

Conceptually:

```text
__new__()  → creates/returns the instance
__init__() → initializes the instance
```

---

# 49. `__del__()`

`__del__()` may be called when an object is finalized, but its exact timing is not something application logic should depend on.

```python
class Demo:
    def __del__(self):
        print("Object finalized")
```

For important cleanup, use:

```python
with open("data.txt") as file:
    data = file.read()
```

instead of depending on `__del__()`.

---

# 50. Dataclasses

For classes that mainly store data, `dataclasses` can reduce boilerplate.

```python
from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int
    marks: float


student = Student("Vishal", 22, 85.5)

print(student)
```

Dataclasses can automatically provide useful methods such as:

- `__init__`
- `__repr__`
- `__eq__`

depending on configuration.

---

# 51. Class Method as Alternative Constructor

A class method is often used to provide an alternative way to create objects.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))


student = Student.from_string("Vishal,22")

print(student.name)
print(student.age)
```

This pattern is very common in Python.

---

# 52. Static Method Use Case

Use a static method when a utility logically belongs to the class but does not need object/class state.

```python
class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9 / 5) + 32


print(Temperature.celsius_to_fahrenheit(25))
```

---

# 53. Nested Classes

A class can be defined inside another class.

```python
class Outer:

    class Inner:
        def show(self):
            print("Inner class")


obj = Outer.Inner()

obj.show()
```

Nested classes are relatively uncommon and should be used only when the relationship improves the design.

---

# 54. Abstract Properties

Properties can also be abstract.

```python
from abc import ABC, abstractmethod


class Shape(ABC):

    @property
    @abstractmethod
    def area(self):
        pass


class Square(Shape):

    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side ** 2
```

---

# 55. Multiple Abstract Methods

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")
```

The subclass must implement the abstract requirements before it can be instantiated.

---

# 56. Interface-Like Design in Python

Python does not have a separate `interface` keyword like Java.

Interface-like designs can be created using:

- Abstract Base Classes (`ABC`)
- Protocols (`typing.Protocol`)
- Duck typing

Example using `Protocol`:

```python
from typing import Protocol


class Speaker(Protocol):
    def speak(self) -> None:
        ...


class Dog:
    def speak(self):
        print("Bark")


def make_speak(obj: Speaker):
    obj.speak()


make_speak(Dog())
```

This supports structural typing: the object is acceptable because it has the required structure.

---

# 57. SOLID Principles

SOLID is a group of object-oriented design principles.

### S — Single Responsibility Principle

A class should have one main responsibility.

Bad:

```python
class Employee:
    def calculate_salary(self):
        pass

    def save_to_database(self):
        pass

    def send_email(self):
        pass
```

Better design separates responsibilities when the system becomes complex.

---

### O — Open/Closed Principle

Software entities should generally be:

- Open for extension
- Closed for modification

Polymorphism and abstractions can help.

---

### L — Liskov Substitution Principle

A subtype should be usable wherever its base type is expected without breaking the intended behavior.

---

### I — Interface Segregation Principle

Prefer small, focused interfaces rather than one large interface that forces classes to implement irrelevant methods.

---

### D — Dependency Inversion Principle

High-level code should depend on abstractions rather than tightly coupling itself to low-level implementations.

---

# 58. OOP Example — E-Commerce

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class Card(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Card")


class Order:

    def __init__(self, amount, payment_method):
        self.amount = amount
        self.payment_method = payment_method

    def checkout(self):
        self.payment_method.pay(self.amount)


order1 = Order(1500, UPI())
order2 = Order(2500, Card())

order1.checkout()
order2.checkout()
```

This example demonstrates:

- Class
- Object
- Encapsulation
- Abstraction
- Inheritance
- Polymorphism
- Composition
- Dependency on an abstraction/interface-like contract

---

# 59. Real-World OOP Structure

A larger application might look like:

```text
Application
│
├── User
│   ├── name
│   ├── email
│   └── login()
│
├── Product
│   ├── name
│   ├── price
│   └── display()
│
├── Cart
│   ├── items
│   ├── add_item()
│   └── total()
│
├── Order
│   ├── items
│   ├── amount
│   └── place_order()
│
└── Payment
    ├── pay()
    └── refund()
```

Each class has a meaningful responsibility.

---

# 60. Complete OOP Example

```python
from abc import ABC, abstractmethod


class User:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"User: {self.name}")


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class Card(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Card")


class Order:

    def __init__(self, user, products, payment):
        self.user = user
        self.products = products
        self.payment = payment

    def total(self):
        return sum(product.price for product in self.products)

    def checkout(self):
        amount = self.total()
        self.payment.pay(amount)


user = User("Vishal")

products = [
    Product("Keyboard", 1000),
    Product("Mouse", 500)
]

payment = UPI()

order = Order(user, products, payment)

user.display()

print("Total:", order.total())

order.checkout()
```

This combines several OOP concepts into one example.

---

# 61. Important OOP Terms

| Term | Meaning |
|---|---|
| Class | Blueprint |
| Object | Instance of a class |
| Attribute | Data associated with class/object |
| Method | Function inside a class |
| `self` | Current instance |
| `cls` | Class reference in class methods |
| `__init__` | Initializes an instance |
| `__new__` | Creates/returns an instance |
| Encapsulation | Bundling state/behavior and controlling access |
| Inheritance | Reusing/extending another class |
| Polymorphism | Same interface, different behavior |
| Abstraction | Expose essential interface, hide details |
| Composition | HAS-A relationship |
| Association | Objects interact/are related |
| Aggregation | Weaker HAS-A relationship |
| Overriding | Replacing inherited behavior |
| Overloading | Multiple signatures; not traditional in Python |
| MRO | Method lookup order |
| `super()` | Delegates to the next class in MRO |
| `@property` | Attribute-style controlled access |
| `@classmethod` | Method receiving class |
| `@staticmethod` | Method with no automatic instance/class argument |

---

# 62. Most Important Interview Differences

## Class vs Object

```text
Class  = Blueprint
Object = Instance
```

---

## Instance Variable vs Class Variable

```text
Instance variable → belongs to object
Class variable    → belongs to class
```

---

## Instance Method vs Class Method vs Static Method

```text
Instance → self
Class    → cls
Static   → no automatic self/cls
```

---

## Inheritance vs Composition

```text
Inheritance  → IS-A
Composition  → HAS-A
```

---

## `is` vs `==`

```text
is  → identity
==  → equality
```

---

## `__str__` vs `__repr__`

```text
__str__  → user-friendly representation
__repr__ → developer-oriented representation
```

---

## `__init__` vs `__new__`

```text
__new__  → creates/returns instance
__init__ → initializes instance
```

---

# 63. Four Pillars — Quick Revision

```text
                 OOP
                  │
      ┌───────────┼───────────┐
      │           │           │
Encapsulation  Inheritance  Polymorphism
      │                       │
      └──────── Abstraction ──┘
```

### Encapsulation

Protect/control object state.

### Inheritance

Reuse and extend existing classes.

### Polymorphism

Same interface, different behavior.

### Abstraction

Expose what is necessary and hide implementation details.

---

# 64. When Should You Use OOP?

OOP is especially useful when:

- The application is large.
- There are many related entities.
- Objects have both state and behavior.
- You need reusable components.
- You need clear boundaries between responsibilities.
- You expect the system to grow.

For very small scripts, simple functions and data structures may be clearer than creating many classes.

---

# 65. Best Practices

### 1. Keep classes focused

Avoid giant classes.

### 2. Prefer meaningful names

```python
class BankAccount:
    ...
```

is better than:

```python
class Data:
    ...
```

### 3. Prefer composition when appropriate

Do not use inheritance just to reuse a few lines of code.

### 4. Keep attributes controlled

Use properties when validation or invariants are needed.

### 5. Use `super()` correctly

Especially with cooperative multiple inheritance.

### 6. Avoid unnecessary private attributes

Python relies heavily on conventions and good interfaces.

### 7. Use abstractions where they provide value

Do not create abstract classes simply because OOP has them.

### 8. Follow single responsibility

A class should have a clear purpose.

---

# 66. OOP Learning Roadmap

A good order for learning Python OOP is:

```text
1. Class
   ↓
2. Object
   ↓
3. Attributes
   ↓
4. self
   ↓
5. __init__
   ↓
6. Instance methods
   ↓
7. Class variables
   ↓
8. Class methods
   ↓
9. Static methods
   ↓
10. Encapsulation
   ↓
11. Properties
   ↓
12. Inheritance
   ↓
13. super()
   ↓
14. Method overriding
   ↓
15. Polymorphism
   ↓
16. Abstraction / ABC
   ↓
17. Composition
   ↓
18. MRO
   ↓
19. Dunder methods
   ↓
20. Dataclasses
   ↓
21. SOLID & design principles
```

---

# 67. Final Cheat Sheet

```python
# CLASS
class Student:
    school = "ABC"

    # CONSTRUCTOR / INITIALIZER
    def __init__(self, name):
        self.name = name

    # INSTANCE METHOD
    def display(self):
        print(self.name)

    # CLASS METHOD
    @classmethod
    def change_school(cls, school):
        cls.school = school

    # STATIC METHOD
    @staticmethod
    def add(a, b):
        return a + b


# OBJECT
student = Student("Vishal")

student.display()

Student.change_school("XYZ")

print(Student.add(10, 20))
```

Inheritance:

```python
class Animal:
    def sound(self):
        print("Animal sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


dog = Dog()

dog.sound()
```

Abstraction:

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

Property:

```python
class Account:

    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
```

---

# 68. One-Line Summary

> **OOP in Python is a way of designing programs around objects that combine state and behavior, using concepts such as classes, objects, encapsulation, inheritance, polymorphism, abstraction, composition, and special methods to build reusable and maintainable software.**
