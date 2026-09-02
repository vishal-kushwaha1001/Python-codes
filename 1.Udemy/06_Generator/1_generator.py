def chai_routine():
    yield "Cup 1: masala chai"
    yield "Cup 2: lemon Tea"
    yield "Cup 3: Green Tea" 
    
    
    
stall = chai_routine()

# for cup in stall:
#    print(cup) 
 

#  Another way by using Next
print(next(stall))
print(next(stall))
print(next(stall))

# normal way
def chai_routine_nor():
      return ["Cup 1: masala chai","Cup 2: lemon Tea","Cup 3: Green Tea"]

print(chai_routine_nor())

