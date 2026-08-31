# zip() is a built-in Python function used to combine two or more iterables element-by-element.

# Syntax
# zip(iterable1, iterable2, iterable3, ...)


#  example 1 -looping over two lists
names = ["vishal", "vipul", "nitesh", "abhi"]

bills = [20 , 40, 60 , 80]

for name , amount in zip(names, bills):
    print(f"{name} paid {amount}")
 
    
    
    
# example 2- create a dictionary
keys = ["name", "age", "city"]
values = ["Vishal", 25, "Delhi"]

data = dict(zip(keys, values))

print(data)





# example 3 - zip() can combine more than two iterables.
names = ["Aman", "Vishal", "Rahul"]
marks = [80, 90, 75]
subjects = ["Math", "Python", "Java"]

for name, mark, subject in zip(names, marks, subjects):
    print(name, mark, subject)