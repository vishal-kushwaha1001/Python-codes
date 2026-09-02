def chai_customer():
    print("Welcome to My Stall . What would you like to prefere : ")
    order = yield
    while True :
        print(f" Please wait, we are preparing.....   your {order} ")
        order = yield
        
        
stall = chai_customer()


next(stall)

stall.send(input("choose order :"))

# stall.send("Masala chai")

stall.send(input("choose order Again :"))
# stall.send("Lemaon Tea")