    # closed generator

def chai_stall():
    try:
        while True:
            order = yield "waiting for order"
            print(f"preparing .....{order}")
    except:
        print("stall closed ") 
        
stall = chai_stall()
next(stall)

stall.send(input("choose :"))
stall.close()