# Inheritance vs Composition vs Aggregation in Python

These are three important object-oriented design relationships:

1. **Inheritance** → IS-A
2. **Composition** → HAS-A, strong ownership
3. **Aggregation** → HAS-A, weak/independent ownership

---

# 1. Inheritance

## Definition

**Inheritance** allows a child class to acquire properties and methods from a parent class.

It represents an:

> **IS-A relationship**

Example:

```python
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Barking")


dog = Dog()

dog.eat()
dog.bark()
```

Output:

```text
Eating
Barking
```

`Dog` inherits `eat()` from `Animal`.

Relationship:

```text
Dog IS-A Animal
```

---

## Syntax

```python
class Child(Parent):
    pass
```

Example:

```python
class Animal:
    pass


class Dog(Animal):
    pass
```

---

## When to Use Inheritance

Use inheritance when there is a genuine **IS-A** relationship.

Examples:

```text
Dog IS-A Animal
Car IS-A Vehicle
Manager IS-A Employee
Circle IS-A Shape
SavingsAccount IS-A BankAccount
```

---

## Advantages

- Code reuse
- Method overriding
- Supports polymorphism
- Represents hierarchical relationships
- Reduces duplicate code

---

## Disadvantages

- Creates tight coupling between parent and child
- Deep inheritance hierarchies can become difficult to maintain
- Changes in the parent can affect children
- Not appropriate for every code-reuse situation

---

# 2. Composition

## Definition

**Composition** is a relationship where one class contains an object of another class and strongly owns that object.

It represents a:

> **HAS-A relationship**

Example:

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

Relationship:

```text
Car HAS-A Engine
```

The `Car` creates its own `Engine`:

```python
self.engine = Engine()
```

This represents strong ownership.

---

## Structure

```text
Car
 │
 └── Engine
```

The `Engine` is a component of the `Car`.

---

## Another Example

```python
class CPU:

    def process(self):
        print("Processing")


class Computer:

    def __init__(self):
        self.cpu = CPU()

    def start(self):
        self.cpu.process()


computer = Computer()

computer.start()
```

Relationship:

```text
Computer HAS-A CPU
```

---

## When to Use Composition

Use composition when an object is naturally **made up of** other objects.

Examples:

```text
Car HAS-A Engine
Computer HAS-A CPU
House HAS-A Room
Order HAS-A PaymentProcessor
Smartphone HAS-A Camera
```

---

## Advantages

- Flexible design
- Lower coupling than inheritance
- Components can be replaced
- Encourages separation of responsibilities
- Easier to test individual components
- Good for building complex objects from smaller objects

---

# 3. Aggregation

## Definition

**Aggregation** is also a **HAS-A relationship**, but the contained object can exist independently of the container.

It represents:

> **Weak ownership / independent lifetime**

Example:

```python
class Teacher:

    def __init__(self, name):
        self.name = name


class Department:

    def __init__(self, teacher):
        self.teacher = teacher


teacher = Teacher("Vishal")

department = Department(teacher)
```

Here the `Teacher` object was created independently:

```python
teacher = Teacher("Vishal")
```

Then it was passed into:

```python
department = Department(teacher)
```

The teacher can exist without the department.

Relationship:

```text
Department HAS-A Teacher
```

but:

```text
Teacher can exist independently
```

---

# 4. Composition vs Aggregation

Both represent:

```text
HAS-A
```

The main difference is **ownership and lifetime**.

## Composition

The containing object creates/owns the component.

```python
class Car:

    def __init__(self):
        self.engine = Engine()
```

Conceptually:

```text
Car
 └── Engine
```

The engine is strongly associated with the car.

---

## Aggregation

The contained object is created independently and passed to the container.

```python
engine = Engine()

car = Car(engine)
```

Conceptually:

```text
Engine ──────→ Car
   │
   └── can exist independently
```

---

# 5. Side-by-Side Examples

## Inheritance

```python
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Barking")
```

Relationship:

```text
Dog IS-A Animal
```

---

## Composition

```python
class Engine:
    pass


class Car:

    def __init__(self):
        self.engine = Engine()
```

Relationship:

```text
Car HAS-A Engine
Engine strongly belongs to Car
```

---

## Aggregation

```python
class Teacher:
    pass


class Department:

    def __init__(self, teacher):
        self.teacher = teacher


teacher = Teacher()

department = Department(teacher)
```

Relationship:

```text
Department HAS-A Teacher
Teacher exists independently
```

---

# 6. The Biggest Difference

Think about **ownership**.

### Inheritance

```text
Parent
   ↓
Child
```

There is no "contained object."

It is an **IS-A** relationship.

---

### Composition

```text
Container
   ↓ owns
Component
```

The component is strongly owned by the container.

---

### Aggregation

```text
Container
   ↓ uses/references
Independent Object
```

The referenced object has its own independent existence.

---

# 7. Lifecycle / Lifetime

This is a useful way to distinguish composition and aggregation.

## Composition

The component is conceptually tied to the lifecycle of the containing object.

Example:

```python
class House:

    def __init__(self):
        self.room = Room()
```

The house creates the room.

```text
House created
    ↓
Room created

House destroyed
    ↓
Room is no longer part of that House
```

The exact Python garbage-collection behavior depends on whether other references to the component exist, but conceptually the relationship represents strong ownership.

---

## Aggregation

The object can exist before, after, or independently of the container.

```python
teacher = Teacher()

department = Department(teacher)
```

If the department is removed:

```python
del department
```

the teacher can still exist if another reference points to it:

```python
print(teacher)
```

Therefore:

```text
Aggregation → independent lifetime
```

---

# 8. Composition vs Aggregation Example

Consider a university.

### Composition

A `House` has `Room`s:

```python
class Room:
    pass


class House:

    def __init__(self):
        self.room = Room()
```

The house creates the room.

```text
House
 └── Room
```

### Aggregation

A `Department` has `Teacher`s:

```python
class Teacher:

    def __init__(self, name):
        self.name = name


class Department:

    def __init__(self, teacher):
        self.teacher = teacher


teacher = Teacher("Vishal")

department = Department(teacher)
```

The teacher exists independently.

```text
Teacher
   ↑
   │
Department
```

The teacher could potentially belong to another department or be referenced elsewhere.

---

# 9. Important Python Point

Python does not have a special `composition` or `aggregation` keyword.

Both are normally implemented using **object references**.

For example:

```python
self.engine = Engine()
```

or:

```python
self.teacher = teacher
```

The distinction comes from the **design and ownership relationship**, not from special Python syntax.

---

# 10. Dependency Injection

Aggregation is commonly seen when an object is passed into another object.

```python
class Engine:

    def start(self):
        print("Engine started")


class Car:

    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()


engine = Engine()

car = Car(engine)
```

The `Car` receives its dependency from outside.

This is called **dependency injection**.

It makes the code easier to test and allows different implementations to be supplied.

---

# 11. Composition and Dependency Injection

Composition can also use dependency injection.

```python
class PetrolEngine:

    def start(self):
        print("Petrol engine")


class ElectricEngine:

    def start(self):
        print("Electric engine")


class Car:

    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()


car1 = Car(PetrolEngine())
car2 = Car(ElectricEngine())

car1.start()
car2.start()
```

Output:

```text
Petrol engine
Electric engine
```

The `Car` doesn't need to know which engine implementation it received.

---

# 12. Inheritance vs Composition

A common design principle is:

> **Prefer composition over inheritance when there is no genuine IS-A relationship.**

For example, don't write:

```python
class Engine:
    pass


class Car(Engine):
    pass
```

This says:

```text
Car IS-A Engine
```

which is logically incorrect.

Instead:

```python
class Engine:
    pass


class Car:

    def __init__(self):
        self.engine = Engine()
```

This correctly represents:

```text
Car HAS-A Engine
```

---

# 13. Detailed Comparison

| Feature | Inheritance | Composition | Aggregation |
|---|---|---|---|
| Relationship | IS-A | HAS-A | HAS-A |
| Main idea | Child derives from parent | Object owns/contains another object | Object references another independent object |
| Ownership | Not applicable | Strong | Weak |
| Object containment | No | Yes | Yes |
| Independent lifetime | Parent/child relationship | Component is strongly tied conceptually | Component can exist independently |
| Inheritance required | Yes | No | No |
| Coupling | Generally tighter | Generally looser | Generally looser |
| Flexibility | Lower | High | High |
| Code reuse | Through inheritance | Through delegation/composition | Through delegation/reference |
| Typical example | Dog → Animal | Car → Engine | Department → Teacher |
| Python keyword | `class Child(Parent)` | No special keyword | No special keyword |
| Method overriding | Common | Not required | Not required |
| Dependency injection | Possible | Common | Common |

---

# 14. Visual Comparison

```text
INHERITANCE
-----------

Animal
  ↑
  │ inherits
  │
 Dog

Dog IS-A Animal
```

```text
COMPOSITION
-----------

Car
 │
 └── Engine

Car HAS-A Engine
Strong ownership
```

```text
AGGREGATION
-----------

Department
     │
     └──── references ────→ Teacher

Department HAS-A Teacher
Teacher can exist independently
```

---

# 15. Simple Real-World Examples

## Inheritance

```text
Animal
 ├── Dog
 ├── Cat
 └── Bird
```

```text
Dog IS-A Animal
```

---

## Composition

```text
Car
 ├── Engine
 ├── Wheel
 └── Battery
```

```text
Car HAS-A Engine
Car HAS-A Wheel
Car HAS-A Battery
```

---

## Aggregation

```text
University
 ├── Department
 │      └── Teacher
```

A teacher can exist independently of a particular department.

```text
Department HAS-A Teacher
```

---

# 16. How to Decide Which One to Use

Ask these questions:

### Question 1

> Is the child actually a type of the parent?

```text
Dog IS-A Animal
```

If yes:

```text
Use Inheritance
```

---

### Question 2

> Is one object made up of another object and strongly owns it?

```text
Car HAS-A Engine
```

If yes:

```text
Use Composition
```

---

### Question 3

> Does one object use/reference another object that can exist independently?

```text
Department HAS-A Teacher
```

If yes:

```text
Use Aggregation
```

---

# 17. Quick Decision Tree

```text
Does A have a relationship with B?
          │
          ├── A IS-A B
          │      ↓
          │  Inheritance
          │
          └── A HAS-A B
                 │
                 ├── A strongly owns B
                 │      ↓
                 │  Composition
                 │
                 └── B can exist independently
                        ↓
                    Aggregation
```

---

# 18. Final Cheat Sheet

```text
INHERITANCE
-----------
IS-A
Parent → Child
Example:
Dog IS-A Animal
```

```text
COMPOSITION
-----------
HAS-A
Strong ownership
Example:
Car HAS-A Engine
```

```text
AGGREGATION
-----------
HAS-A
Weak/independent ownership
Example:
Department HAS-A Teacher
```

## One-Line Memory Trick

> **Inheritance = IS-A**

> **Composition = HAS-A + strong ownership**

> **Aggregation = HAS-A + independent object**

## Most Important Difference

```text
Inheritance:
Dog IS-A Animal

Composition:
Car HAS-A Engine
Car strongly owns Engine

Aggregation:
Department HAS-A Teacher
Teacher can exist independently
```

### Practical Design Rule

> Use **inheritance** for genuine "IS-A" relationships. Use **composition** when building an object from components. Use **aggregation** when an object needs to reference/use another object whose lifetime and ownership remain independent.
