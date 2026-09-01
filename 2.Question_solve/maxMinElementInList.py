print("input no of element :")
s = int(input())
list1 = []
for i in range(s):
    element = int(input())
    list1.append(element)
print(list1)
maxElement = list1[0]
minElement = list1[0]
for i in range(1,len(list1)):
    if list1[i] > maxElement:
        maxElement = list1[i]
    if list1[i] < minElement :
        minElement = list1[i]
print("max element :",maxElement)
print("min element :",minElement)


