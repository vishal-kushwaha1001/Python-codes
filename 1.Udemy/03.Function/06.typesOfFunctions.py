#  types of functions
# 
# 1. Pure Function - 
# A pure function always gives the same output for the same input and does not change anything outside the function.

def add(a, b):
    return a + b

print(add(10, 20))  # 30
print(add(10, 20))  # 30

# 2. Impure Function -
# An impure function can produce different outputs for the same input or change something outside the function.

total = 0

def add_to_total(x):
    global total
    total += x
    return total

print(add_to_total(10))  # 10
print(add_to_total(10))  # 20


# 3. Lambda Function in Python -
# A lambda function is a small anonymous function (a function without a name). 
# It is mainly used when you need a simple function for a short operation.
#  lambda arguments: expression


#  note ------   lambda input: output

# example
# 1
square = lambda x: x * x

print(square(5))


# 2
students = [
    ("Aman", 80),
    ("Vishal", 95),
    ("Rahul", 70)
]

result = sorted(students, key=lambda x: x[1])

print(result)


# [('Rahul', 70), ('Aman', 80), ('Vishal', 95)]