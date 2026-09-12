# Generator
 ```
 ⇒ A generator is a special type of function/iterator
 that produces values one at a time, instead of creating and 
 storing all values in memory at once.

 ```

__⇒ The main keyword used is <code>*yield.</code>*__


## Why its needed: 
     ➔ you save memory
     ➔ you don't want the result immedietely
     ➔ lazy evaluation
     ➔ memory efficiency

``` python
# using generator
def chai_routine():
    yield "Cup 1: masala chai"
    yield "Cup 2: lemon Tea"
    yield "Cup 3: Green Tea" 

stall = chai_routine()

print(next(stall))
print(next(stall))
print(next(stall))

# Normal Way
def chai_routine_nor():
      return ["Cup 1: masala chai","Cup 2: lemon Tea","Cup 3: Green Tea"]

print(chai_routine_nor())

```
⇒ Its return all values at once but generator return once at a time .The output of Normal way and using generator is same but generator save memory 

### output :
      Cup 1: masala chai
      Cup 2: lemon Tea
      Cup 3: Green Tea
      ['Cup 1: masala chai', 'Cup 2: lemon Tea', 'Cup 3: Green Tea']


#### When you call:

``` python

stall = chai_routine()

```

>*Python does not execute the function completely.*

## Inifinite Generator

``` python

def infinite_chai():
    count = 1
    while True :
        yield f"Refill chai : # {count}"
        count += 1
        
user1 = infinite_chai()

print("Serve for user1 : \n " )
for _ in range(5):
    print(next(user1))
    
    
user2 = infinite_chai()

print("\n Serve for user2 :\n" )
for _ in range(5):
    print(next(user2))

```

### In this code :

``` python

for _ in range(5):
    print(next(user1))


```
> __It can handle the iteration of Generator. It decide the how may itmes it iterate through .__



# `yield from` and `close()`

## `yield from`

`yield from` gets values from another generator.

```python
def chai_menu():
    yield from local_chai()
    yield from imported_chai()
```

It produces:

```text
Masala Chai
Lemon Tea
Matcha
Oolong
```

**Remember:**
- `yield` → produces a value
- `yield from` → produces values from another generator

---

## `close()`

`close()` permanently stops a generator.

```python
stall = chai_stall()

next(stall)
stall.send("Masala Chai")
stall.close()
```

Output:

```text
preparing .....Masala Chai
stall closed
```

**Flow:**

```text
next()       → start generator
send(value)  → send value into generator
yield        → pause generator
close()      → terminate generator
```

**Summary:** `yield from` delegates to another generator; `close()` terminates the current generator.

