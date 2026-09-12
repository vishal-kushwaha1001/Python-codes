# Concurrency and Parallelism

## 1. Concurrency

**Concurrency = dealing with multiple tasks by switching/interleaving between them.**

Tasks do not necessarily execute at the exact same time.

### Example

```text
Task A: ███     ███
Task B:    ███     ███
Task C:       ███
        ──────────────> Time
```

Think of **one chef** preparing multiple dishes by switching between them.

### Best for

- API requests
- Database queries
- File I/O
- Network requests
- User input

### Common Python approaches

```text
asyncio
threading
```

---

## 2. Parallelism

**Parallelism = executing multiple tasks at the same time.**

Usually, multiple CPU cores execute tasks simultaneously.

### Example

```text
Task A: █████████
Task B: █████████
Task C: █████████
        ──────────────> Time
```

Think of **multiple chefs** preparing multiple dishes simultaneously.

### Best for

- Image processing
- Video processing
- Mathematical calculations
- Machine learning
- Large data processing

### Common Python approach

```python
from multiprocessing import Process
```

---

## 3. Key Difference

| Concurrency | Parallelism |
|---|---|
| Multiple tasks are in progress | Multiple tasks execute simultaneously |
| Can work with one CPU core | Usually uses multiple CPU cores |
| Tasks switch/interleave | Tasks run at the same time |
| Best for I/O-bound work | Best for CPU-bound work |
| `asyncio`, `threading` | `multiprocessing` |
| Focus: managing tasks | Focus: simultaneous execution |

---

## 4. Easy Way to Remember

> **Concurrency:** "I can handle multiple things."

> **Parallelism:** "I can do multiple things at the same time."

---

## 5. Real-World Example

Suppose you need to download 10 files.

### Concurrency

```text
Download A → waiting
Download B → waiting
Download C → waiting
Download A → data received
Download D → waiting
...
```

While one download waits for the network, another task can make progress.

### Parallelism

```text
CPU 1 → Process file A
CPU 2 → Process file B
CPU 3 → Process file C
CPU 4 → Process file D
```

Multiple CPU cores execute work simultaneously.

---

## 6. Concurrency and Parallelism Together

Concurrency and parallelism can exist together.

```text
             Concurrency
                  ↓
       ┌──────────┼──────────┐
       ↓          ↓          ↓
     Task A     Task B      Task C
       ↓          ↓          ↓
     CPU 1      CPU 2      CPU 3
       └──────────┼──────────┘
                  ↓
             Parallelism
```

### Remember

```text
Concurrency ≠ Parallelism

Concurrency → Multiple tasks in progress
Parallelism  → Multiple tasks executing simultaneously
```
