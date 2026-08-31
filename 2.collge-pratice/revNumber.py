num = 1234
revNum = 0 
while num > 0:
     lastDigit = int(num%10) 
     revNum = revNum * 10 + lastDigit
     num = num // 10

print(revNum)     
    