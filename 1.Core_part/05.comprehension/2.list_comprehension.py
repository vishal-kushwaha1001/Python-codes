employees = [
    ("Aman", 25000),
    ("Vishal", 45000),
    ("Rahul", 30000),
    ("Ankit", 60000)
]

#  find the employee whose salary is > 30000

result = [ name for name, salary in employees if salary > 30000]
print(" Employee whose salary is grater than 30k :", result)
