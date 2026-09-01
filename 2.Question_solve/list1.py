# create an empty list & insert element by append & insert element in the list 

a = int(input())
list1 = []
for i in range(a):
    element = int(input())
    list1.append(element)
print(list1)
list1.insert(5 ,int(input()) )
print(list1)

