def infinite_chai():
    count = 1
    while True :
        yield f"Refill chai : # {count}"
        count += 1
        
user1 = infinite_chai()

print("Serve for user1 : \n " )
for _ in range(5):
    print(next(user1))
    
    
user2 = infinite_chai()

print("\n Serve for user2 :\n" )
for _ in range(5):
    print(next(user2))