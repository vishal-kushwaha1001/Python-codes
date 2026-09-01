num = int(input("inter Number : "))
isPrime = False 
for i in range(2 ,num//2):
    if num % i== 0 :
        print("No is non prime Number")
        isPrime = True
        break
    
if isPrime == False:
    print("Number is  Prime No ") 
