num= [2,3,4,5,6,7,8]

print("slicing reverse")
print(num[-1:0 :-1])

print("slicing with len function")
print(num[0:len(num)])

print("indexing")
print(num[5])

print("slicing with indexing")
print(num[0:num[-1]])

print("slicing with index function")
print(num[0:num.index(5)])


