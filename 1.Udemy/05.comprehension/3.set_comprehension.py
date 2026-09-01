employees = [
    ("Aman", "IT"),
    ("Vishal", "HR"),
    ("Rahul", "IT"),
    ("Ankit", "Sales"),
    ("Ravi", "HR")
]

# find all unique departments.

# normal way
# departments = set()

# for name, department in employees:
#     departments.add(department)

# print(departments)

# using comprehension
u_departments= {department for name , department in employees}
print(u_departments)