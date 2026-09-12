# Python Thread Methods

These are the main `threading.Thread` methods to know.

## 1. `start()`

Starts the thread and causes its `run()` method to execute.

```python
t.start()
```

> Normally use `start()` instead of calling `run()` directly.

---

## 2. `run()`

Contains the code that the thread executes.

```python
import threading

def task():
    print("Task running")

t = threading.Thread(target=task)
t.start()
```

`start()` internally causes `run()` to execute.

You normally **do not call `run()` directly**.

---

## 3. `join()`

Waits for the thread to finish before continuing.

```python
t.start()
t.join()

print("Thread finished")
```

Without `join()`, the main thread can continue while the other thread is still running.

### With timeout

```python
t.join(2)
```

Waits for a maximum of 2 seconds.

---

## 4. `is_alive()`

Checks whether the thread is currently running.

```python
print(t.is_alive())
```

Returns:

```text
True
```

or

```text
False
```

Example:

```python
t = threading.Thread(target=task)

print(t.is_alive())  # False

t.start()

print(t.is_alive())  # True (while running)

t.join()

print(t.is_alive())  # False
```

---

## 5. `isDaemon()`

Checks whether the thread is a daemon thread.

```python
t.isDaemon()
```

> This is an older/deprecated style. Prefer the `daemon` attribute.

Use:

```python
t.daemon
```

---

## 6. `setDaemon()`

Sets whether the thread is a daemon thread.

```python
t.setDaemon(True)
```

> Older/deprecated style. Prefer:

```python
t.daemon = True
```

---

## 7. `getName()`

Gets the thread's name.

```python
t.getName()
```

> Older/deprecated style. Prefer:

```python
t.name
```

---

## 8. `setName()`

Sets the thread's name.

```python
t.setName("Worker")
```

> Older/deprecated style. Prefer:

```python
t.name = "Worker"
```

---

# Quick Summary

| Method | Purpose |
|---|---|
| `start()` | Starts the thread |
| `run()` | Executes the thread's target code |
| `join()` | Waits for the thread to finish |
| `is_alive()` | Checks whether the thread is running |
| `isDaemon()` | Checks daemon status *(older style)* |
| `setDaemon()` | Sets daemon status *(older style)* |
| `getName()` | Gets thread name *(older style)* |
| `setName()` | Sets thread name *(older style)* |

## Most Important

```python
t.start()       # Start thread
t.run()         # Run thread code (normally called by start())
t.join()        # Wait for thread
t.is_alive()    # Check thread status
```

### Modern Alternatives

```python
t.daemon = True     # Instead of setDaemon()
t.name = "Worker"   # Instead of setName()
```
