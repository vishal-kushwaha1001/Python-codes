n = int(input("Number :"))

def prime(n):
    isPrime = True
    for i in range(2,n):
        if n%i == 0:
           isPrime = False
           break
       
       
    if isPrime == False:
        print(f"{n} is not prime" )
    else  :
         print(f"{n} is  prime" )       
            
prime(n)           