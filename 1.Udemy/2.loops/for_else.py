scorecard = [("vishal", 90), ("nitesh", 80), ("abhi", 40 ), ("Vipul", 80)]

for name , marks in scorecard :
    if marks <= 40 :
        print(f"{name } is fail")
        break
else : print("all are pass")