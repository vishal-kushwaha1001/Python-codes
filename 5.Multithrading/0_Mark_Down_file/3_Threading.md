# Threading in Python

## 1. Definition

> **Threading is a technique for running multiple threads concurrently within a single process, allowing a program to make progress on multiple tasks without waiting for one task to completely finish before starting another.**

In Python, threading is mainly useful for **I/O-bound tasks** such as network requests, file operations, API calls, and database operations.

---

# 2. What is a Thread?

A **thread** is a lightweight unit of execution inside a process.

```text
Process
│
├── Main Thread
├── Thread 1 → Task A
├── Thread 2 → Task B
└── Thread 3 → Task C
```

Threads belonging to the same process share the process's memory.

---

# 3. Concurrency vs Parallelism

### Concurrency

> **Concurrency means multiple tasks are in progress during overlapping periods of time.**

The CPU may switch between tasks.

```text
Task A: ███     ███
Task B:    ███     ███
Task C:       ███
        ──────────────→ Time
```

### Parallelism

> **Parallelism means multiple tasks are actually executing at the same time, typically on different CPU cores.**

```text
CPU 1 → Task A █████████
CPU 2 → Task B █████████
CPU 3 → Task C █████████
```

### Important

```text
Threading → mainly provides concurrency
Parallelism → simultaneous execution
```

In standard CPython, the **GIL (Global Interpreter Lock)** limits simultaneous execution of Python bytecode by multiple threads, so threading is generally not the best choice for CPU-bound Python code.

---

# 4. Creating a Thread

Python provides the `threading` module.

```python
import threading

def task():
    print("Task is running")

t = threading.Thread(target=task)

t.start()
t.join()
```

### Explanation

```python
threading.Thread(target=task)
```

Creates a thread object.

```python
t.start()
```

Starts the thread.

```python
t.join()
```

Waits for the thread to finish.

---

# 5. `start()`

`start()` starts a new thread and causes its `run()` method to execute.

```python
t.start()
```

> A thread can normally be started only once.

Do not normally call `run()` directly when you want a new thread.

---

# 6. `run()`

`run()` contains the code executed by the thread.

```python
import threading

def task():
    print("Task running")

t = threading.Thread(target=task)

t.start()
```

Conceptually:

```text
start()
   ↓
creates/starts thread
   ↓
run()
   ↓
target function executes
```

Calling `t.run()` directly does **not** create a separate thread; it executes in the current thread.

---

# 7. `join()`

`join()` makes the calling thread wait until another thread finishes.

```python
t.start()
t.join()

print("Thread completed")
```

### With timeout

```python
t.join(2)
```

The calling thread waits for a maximum of 2 seconds.

---

# 8. `is_alive()`

Checks whether a thread is currently alive/running.

```python
print(t.is_alive())
```

Returns:

```text
True
```

or:

```text
False
```

Example:

```python
t = threading.Thread(target=task)

print(t.is_alive())  # False

t.start()

print(t.is_alive())  # True while the task is running

t.join()

print(t.is_alive())  # False
```

---

# 9. Passing Arguments to a Thread

Use `args`.

```python
import threading

def greet(name):
    print(f"Hello {name}")

t = threading.Thread(
    target=greet,
    args=("Vishal",)
)

t.start()
t.join()
```

For multiple arguments:

```python
def add(a, b):
    print(a + b)

t = threading.Thread(
    target=add,
    args=(10, 20)
)

t.start()
t.join()
```

For keyword arguments, use `kwargs`:

```python
def user(name, age):
    print(name, age)

t = threading.Thread(
    target=user,
    kwargs={"name": "Vishal", "age": 25}
)

t.start()
t.join()
```

---

# 10. Multiple Threads

```python
import threading

def task(name):
    print(f"{name} is running")

t1 = threading.Thread(target=task, args=("Task 1",))
t2 = threading.Thread(target=task, args=("Task 2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("All tasks completed")
```

The order in which threads execute is controlled by the operating system/runtime, so output order can vary.

---

# 11. Threading with a Loop

```python
import threading

def download(file):
    print(f"Downloading {file}")

files = ["A.pdf", "B.pdf", "C.pdf"]

threads = []

for file in files:
    t = threading.Thread(
        target=download,
        args=(file,)
    )

    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All downloads completed")
```

This pattern is useful when several independent tasks need to be performed.

---

# 12. I/O-Bound Tasks

Threading is particularly useful for tasks that spend significant time **waiting for external resources**.

Examples:

```text
API requests
Network requests
File I/O
Database operations
Downloading files
Web scraping
```

Example concept:

```text
Thread 1 → API request → WAITING
Thread 2 → API request → WAITING
Thread 3 → File operation → WORKING
Thread 1 → Response received
```

While one thread is waiting, another thread can make progress.

---

# 13. CPU-Bound Tasks

CPU-bound tasks require substantial CPU computation.

Examples:

```text
Large mathematical calculations
Image processing
Video processing
CPU-heavy data processing
```

For CPU-bound Python code, normal threading is generally not the preferred way to achieve CPU parallelism in CPython because of the GIL.

Common alternative:

```python
multiprocessing
```

Simple rule:

```text
I/O-bound  → threading / asyncio
CPU-bound  → multiprocessing
```

---

# 14. Daemon Thread

A **daemon thread is a background thread that does not prevent the Python program from terminating when all non-daemon threads have finished.**

Create one using:

```python
import threading

def background_task():
    print("Background work")

t = threading.Thread(
    target=background_task,
    daemon=True
)

t.start()
```

Or:

```python
t = threading.Thread(target=background_task)
t.daemon = True
t.start()
```

### Common uses

- Background monitoring
- Logging
- Cleanup
- Periodic checking
- Heartbeat/background tasks

### Important

Do not use daemon threads for critical work that must finish, because Python does not wait for daemon threads during shutdown.

---

# 15. Normal Thread vs Daemon Thread

| Normal Thread | Daemon Thread |
|---|---|
| Keeps the program alive | Does not keep the program alive |
| Python waits for it | Python does not wait for it at shutdown |
| Intended to complete its work | Intended for background work |
| Suitable for important work | Suitable for non-critical background work |

---

# 16. Thread Safety

Because threads share memory, multiple threads can access the same data.

This can create a **race condition**.

Example:

```python
counter = 0

# Multiple threads modify counter
counter += 1
```

If multiple threads access shared data without proper synchronization, the result may not be what you expect.

---

# 17. Lock

A `Lock` allows only one thread at a time to enter a protected section of code.

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter

    with lock:
        counter += 1
```

The `with lock:` block is protected.

```text
Thread 1 → 🔒 Critical Section → Unlock
Thread 2 → Wait
Thread 3 → Wait
Thread 2 → 🔒 Critical Section → Unlock
```

---

# 18. Other Synchronization Tools

The `threading` module provides several synchronization mechanisms.

```text
Lock
RLock
Semaphore
Event
Condition
Barrier
```

### `Lock`

Basic mutual exclusion.

### `RLock`

A reentrant lock that can be acquired multiple times by the same thread.

### `Semaphore`

Limits the number of threads that can access a resource at the same time.

### `Event`

Allows threads to communicate using a shared event flag.

### `Condition`

Allows threads to wait for and signal specific conditions.

### `Barrier`

Allows a group of threads to wait until all of them reach a certain point.

---

# 19. Thread Name

Threads can have names.

```python
import threading

def task():
    print(threading.current_thread().name)

t = threading.Thread(
    target=task,
    name="Worker-1"
)

t.start()
t.join()
```

You can also use:

```python
t.name = "Worker-1"
```

---

# 20. Thread Identity

A thread has identifiers such as:

```python
t.ident
t.native_id
```

`ident` is the thread's Python-level identifier.

`native_id` is the operating-system thread ID when available.

---

# 21. Current Thread

Use:

```python
threading.current_thread()
```

Example:

```python
import threading

def task():
    current = threading.current_thread()
    print(current.name)

t = threading.Thread(
    target=task,
    name="Worker"
)

t.start()
t.join()
```

---

# 22. Main Thread

You can access the main thread using:

```python
threading.main_thread()
```

Example:

```python
import threading

print(threading.main_thread().name)
```

Usually the name is:

```text
MainThread
```

---

# 23. Thread Pool

Instead of manually creating and managing many threads, use `ThreadPoolExecutor`.

```python
from concurrent.futures import ThreadPoolExecutor

def task(number):
    return number * 2

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, [1, 2, 3, 4, 5])

    for result in results:
        print(result)
```

### Why use a thread pool?

```text
Without pool:
Create → Start → Manage → Destroy many threads

With pool:
Create worker threads → Reuse them for multiple tasks
```

This makes concurrent code easier to manage.

---

# 24. Thread Methods

Important `Thread` methods:

| Method | Purpose |
|---|---|
| `start()` | Starts a new thread |
| `run()` | Executes the thread's target code |
| `join()` | Waits for the thread to finish |
| `is_alive()` | Checks whether the thread is alive |
| `isDaemon()` | Checks daemon status; older style |
| `setDaemon()` | Sets daemon status; older style |
| `getName()` | Gets the name; older style |
| `setName()` | Sets the name; older style |

### Modern approach

Instead of:

```python
t.setDaemon(True)
t.setName("Worker")
```

Prefer:

```python
t.daemon = True
t.name = "Worker"
```

---

# 25. Thread Lifecycle

A simplified thread lifecycle:

```text
             Thread Created
                    ↓
                start()
                    ↓
                 Running
                    ↓
             ┌──────┴──────┐
             ↓             ↓
          Waiting       Executing
             ↓             ↓
             └──────┬──────┘
                    ↓
                 Finished
```

A thread cannot be restarted after it has finished.

```python
t.start()
t.join()

# t.start() again → RuntimeError
```

---

# 26. Threading vs Multiprocessing

| Threading | Multiprocessing |
|---|---|
| Multiple threads | Multiple processes |
| Shared memory | Separate memory |
| Lightweight | More resource-intensive |
| Good for I/O-bound work | Good for CPU-bound work |
| Limited by CPython GIL for Python bytecode | Can use multiple CPU cores |
| `threading` | `multiprocessing` |

---

# 27. Threading vs Asyncio

| Threading | Asyncio |
|---|---|
| Uses threads | Uses asynchronous tasks |
| OS/runtime schedules threads | Event loop schedules tasks |
| Can run blocking I/O in threads | Best with non-blocking async I/O |
| Easier for some blocking libraries | Excellent for high-volume async I/O |
| `threading.Thread` | `asyncio` |

---

# 28. Common Mistakes

### Mistake 1: Calling `run()` instead of `start()`

```python
t.run()
```

This does not start a separate thread.

Use:

```python
t.start()
```

---

### Mistake 2: Forgetting `join()`

If the main thread needs to wait for worker threads:

```python
t.start()
t.join()
```

---

### Mistake 3: Sharing mutable data without synchronization

```python
counter += 1
```

Use appropriate synchronization when multiple threads access shared mutable state.

---

### Mistake 4: Using threading for CPU-heavy Python code

For CPU-bound work in CPython, consider:

```python
multiprocessing
```

---

# 29. Complete Basic Example

```python
import threading
import time

def task(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} finished")

t1 = threading.Thread(
    target=task,
    args=("Task 1",)
)

t2 = threading.Thread(
    target=task,
    args=("Task 2",)
)

t1.start()
t2.start()

t1.join()
t2.join()

print("All tasks completed")
```

Conceptually:

```text
Main Thread
     │
     ├──→ Thread 1 → Task 1
     │
     └──→ Thread 2 → Task 2
                  ↓
              Both finish
                  ↓
          Main continues
```

---

# 30. Quick Summary

```text
Threading
│
├── Multiple threads inside a process
│
├── Threads share process memory
│
├── Provides concurrency
│
├── Best suited to I/O-bound work
│
├── threading.Thread
│   ├── start()
│   ├── run()
│   ├── join()
│   └── is_alive()
│
├── Synchronization
│   ├── Lock
│   ├── RLock
│   ├── Semaphore
│   ├── Event
│   ├── Condition
│   └── Barrier
│
├── Background work
│   └── Daemon Thread
│
└── Thread pool
    └── ThreadPoolExecutor
```

## Most Important Things to Remember

```text
start()      → Start a new thread
run()        → Thread's execution method
join()       → Wait for thread completion
is_alive()   → Check thread status
daemon=True  → Background thread
Lock         → Protect shared data
```

> **Threading is mainly used to achieve concurrency and improve responsiveness/performance for I/O-bound tasks.**
