num = int(input("please inter number :"))

def sumOfN(n):
    sum =int(n*(n+1)/2)
    return sum 
# print(sumOfN(num))


def factorial(n):
    fact = 1
    while n>1:
        fact = fact * n 
        n -= 1
    return fact

print(factorial(num))  


def factorial1(n):
    fact = 1 
    for i in range(1,n+1,1):
        fact = fact * i 
    return fact 
          
          
# print(factorial1(num))          