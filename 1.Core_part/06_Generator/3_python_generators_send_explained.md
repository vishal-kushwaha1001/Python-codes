# Python Generator with `send()`

## Code

```python
def chai_customer():

    print("Welcome to My Stall. What would you like to prefer:")

    order = yield

    while True:

        print(f"Please wait, we are preparing..... your {order}")

        order = yield


stall = chai_customer()

next(stall)

stall.send("Masala chai")

stall.send("Lemon Tea")
```

---

# 1. What is happening here?

This is a **generator function**, because it contains the `yield` keyword.

But this example demonstrates something more specific:

> **Using `yield` to receive values from outside with `generator.send(value)`.**

Normally, we use a generator to produce values.

Here, the generator is also being used to **receive values**.

---

# 2. Creating the generator

```python
stall = chai_customer()
```

At this point, Python does **not execute the function body**.

Instead, it creates a generator object:

```text
chai_customer()
      ↓
 generator object
      ↓
    stall
```

So:

```python
stall
```

represents the paused generator.

---

# 3. Why do we need `next(stall)` first?

The first important line is:

```python
next(stall)
```

This starts/resumes the generator.

Python executes:

```python
print("Welcome to My Stall. What would you like to prefer:")
```

So it prints:

```text
Welcome to My Stall. What would you like to prefer:
```

Then Python reaches:

```python
order = yield
```

At this point, the generator **pauses**.

Think of it as:

```text
order = yield
         ↑
      PAUSED
```

The generator is now waiting for a value.

---

# 4. What does `order = yield` mean?

This line is very important:

```python
order = yield
```

It means:

> Pause the generator here and wait for a value to be sent into it.

When we later execute:

```python
stall.send("Masala chai")
```

the value:

```text
"Masala chai"
```

is sent to the paused `yield`.

Then the assignment becomes conceptually:

```python
order = "Masala chai"
```

So now:

```text
order
  ↓
"Masala chai"
```

---

# 5. First `send()`

We execute:

```python
stall.send("Masala chai")
```

The generator was paused at:

```python
order = yield
```

The value `"Masala chai"` is sent into the generator.

So:

```python
order = "Masala chai"
```

Then Python continues to:

```python
while True:
```

and executes:

```python
print(f"Please wait, we are preparing..... your {order}")
```

Output:

```text
Please wait, we are preparing..... your Masala chai
```

Then it reaches:

```python
order = yield
```

again.

The generator pauses here again.

---

# 6. Second `send()`

Now we execute:

```python
stall.send("Lemon Tea")
```

The generator is currently paused at:

```python
order = yield
```

So `"Lemon Tea"` is sent into that `yield`.

Now:

```python
order = "Lemon Tea"
```

Then the loop continues:

```python
print(f"Please wait, we are preparing..... your {order}")
```

Output:

```text
Please wait, we are preparing..... your Lemon Tea
```

Then:

```python
order = yield
```

pauses the generator again.

---

# 7. Complete execution flow

The execution can be visualized like this:

```text
stall = chai_customer()
        │
        ▼
Generator created
        │
        ▼
next(stall)
        │
        ▼
Print welcome message
        │
        ▼
order = yield
        │
        │ PAUSED
        ▼
stall.send("Masala chai")
        │
        ▼
order = "Masala chai"
        │
        ▼
Print:
Please wait, we are preparing..... your Masala chai
        │
        ▼
order = yield
        │
        │ PAUSED
        ▼
stall.send("Lemon Tea")
        │
        ▼
order = "Lemon Tea"
        │
        ▼
Print:
Please wait, we are preparing..... your Lemon Tea
        │
        ▼
order = yield
        │
        │ PAUSED
```

---

# 8. Why can't we directly use `send()`?

This would be incorrect:

```python
stall = chai_customer()

stall.send("Masala chai")
```

because the generator has not started yet.

You should first start it with:

```python
next(stall)
```

Then you can send a value:

```python
stall.send("Masala chai")
```

A common pattern is:

```python
generator = some_generator()

next(generator)          # Start the generator

generator.send(value)    # Send a value
```

---

# 9. `yield` as input and output

Usually, people learn:

```python
value = yield
```

and think only about generating values.

But `yield` has two sides.

### It can produce a value

```python
yield 10
```

The generator gives `10` to the caller.

### It can receive a value

```python
value = yield
```

The caller can send a value:

```python
generator.send(100)
```

So `yield` can act as a **communication point** between the generator and the caller.

---

# 10. Why `while True`?

Your code contains:

```python
while True:
```

This creates an infinite loop.

That means the chai stall can continuously receive orders:

```text
Order 1 → Masala chai
             ↓
         Prepare
             ↓
Order 2 → Lemon Tea
             ↓
         Prepare
             ↓
Order 3 → Ginger Tea
             ↓
         Prepare
             ↓
Order 4 → Elaichi Chai
             ↓
         Prepare
             ↓
           ...
```

For example:

```python
stall.send("Masala chai")
stall.send("Lemon Tea")
stall.send("Ginger Tea")
stall.send("Elaichi Chai")
```

The generator can keep accepting orders.

---

# 11. Why is `order = yield` repeated?

Notice that you have:

```python
order = yield
```

twice:

```python
order = yield

while True:

    print(f"Please wait, we are preparing..... your {order}")

    order = yield
```

The first one waits for the **first order**.

The second one waits for the **next order**.

Without the second `yield`, the generator would not have a point where it could pause and receive another order.

---

# 12. A cleaner version

Your code can be written as:

```python
def chai_customer():

    print("Welcome to My Stall. What would you like to prefer?")

    order = yield

    while True:
        print(f"Please wait, we are preparing..... your {order}")
        order = yield


stall = chai_customer()

next(stall)

stall.send("Masala chai")
stall.send("Lemon Tea")
stall.send("Ginger Tea")
```

Output:

```text
Welcome to My Stall. What would you like to prefer?
Please wait, we are preparing..... your Masala chai
Please wait, we are preparing..... your Lemon Tea
Please wait, we are preparing..... your Ginger Tea
```

---

# 13. Important concept: `send()` returns the value yielded

There is another interesting point.

Consider:

```python
def test():
    value = yield
    yield value * 2
```

Now:

```python
g = test()

next(g)

result = g.send(10)

print(result)
```

Output:

```text
20
```

Why?

The first:

```python
value = yield
```

receives `10`.

Then:

```python
yield value * 2
```

produces `20`.

So:

```text
send() → sends value INTO generator
yield  → sends value OUT of generator
```

This is the key concept.

---

# 14. `next()` vs `send()`

| Operation | Purpose |
|---|---|
| `next(g)` | Start/resume the generator |
| `g.send(value)` | Send a value into the generator |
| `yield` | Pause generator and optionally produce a value |
| `while True` | Keep accepting values continuously |

---

# 15. Real-world idea

Your example is similar to a **customer/order processing system**:

```text
Customer
   │
   │ "Masala chai"
   ▼
Generator
   │
   ▼
Process order
   │
   │ "Lemon Tea"
   ▼
Generator
   │
   ▼
Process order
```

The generator acts like a small **stateful receiver** that stays alive between orders.

This pattern can be useful for:

- Event processing
- Data pipelines
- Log processing
- Request handling
- Message processing
- Producer/consumer patterns
- Coroutine-style programming

---

# Final takeaway

The most important part of this example is:

```python
order = yield
```

and:

```python
stall.send("Masala chai")
```

They work together:

```text
              GENERATOR
                 │
                 │ yield
                 ▼
            ┌──────────┐
            │  PAUSED  │
            └──────────┘
                 ▲
                 │ send("Masala chai")
                 │
              CALLER
```

In simple words:

> **`yield` pauses the generator, and `send()` allows the caller to put a value into that paused generator.**

So your chai-stall generator is essentially a **continuously running order receiver** that pauses whenever it is waiting for the next order.
