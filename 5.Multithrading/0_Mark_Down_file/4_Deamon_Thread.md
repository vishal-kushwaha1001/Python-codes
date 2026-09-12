# Daemon Thread in Python

## What is a Daemon Thread?

A **daemon thread** is a background thread that **does not keep the Python program alive**.

When all non-daemon threads finish, Python can exit even if daemon threads are still running.



---

```
A daemon thread is a background thread that runs alongside the main program but does not prevent the Python program from terminating when all non-daemon threads have finished.

In simple words

A daemon thread performs background work and is automatically stopped when the program exits. 
```

## Normal Thread vs Daemon Thread

### Normal Thread

A normal thread must finish before Python exits.

```python
import threading
import time

def task():
    time.sleep(5)
    print("Task finished")

t = threading.Thread(target=task)
t.start()

print("Main finished")
```

Even though the main thread finishes, Python waits for the normal thread.

```text
Main thread   → Finished
                  ↓
              WAITING
                  ↓
Worker thread → Finished
                  ↓
              Program exits
```

### Daemon Thread

A daemon thread runs in the background.

```python
import threading
import time

def background_task():
    while True:
        print("Background working...")
        time.sleep(1)

t = threading.Thread(target=background_task)

t.daemon = True
t.start()

time.sleep(3)

print("Main finished")
```

When the main thread finishes, Python can exit and the daemon thread is stopped.

```text
Main thread
    ↓
Finished
    ↓
Python exits
    ↓
Daemon thread stops
```

---

## How to Create a Daemon Thread

### Method 1: Using `daemon` attribute

```python
t = threading.Thread(target=task)

t.daemon = True
t.start()
```

### Method 2: Using the constructor

```python
t = threading.Thread(
    target=task,
    daemon=True
)

t.start()
```

> Set the daemon status **before** calling `start()`.

---

## Common Uses

Daemon threads are useful for background tasks such as:

- Logging
- Monitoring
- Background cleanup
- Periodic status checking
- Heartbeat tasks

---

## Important Warning

Do **not** use daemon threads for important work that must finish.

For example:

```text
❌ Saving critical data
❌ Completing an important transaction
❌ Writing essential files
```

A daemon thread may be stopped when the program exits.

---

## Easy Analogy

Imagine a shop:

```text
Main work → Shop is open
                ↓
           Shop closes
                ↓
      Background worker can stop
```

The background worker should not keep the entire shop open.

---

## Quick Comparison

| Normal Thread | Daemon Thread |
|---|---|
| Keeps program alive | Does not keep program alive |
| Python waits for it | Python does not wait for it at shutdown |
| Must finish before exit | May be stopped when program exits |
| Good for important work | Good for background work |

## Remember

```text
Normal Thread
    ↓
Keeps program alive until it finishes

Daemon Thread
    ↓
Runs in background
    ↓
Does NOT keep program alive
    ↓
Can stop when the program exits
```
