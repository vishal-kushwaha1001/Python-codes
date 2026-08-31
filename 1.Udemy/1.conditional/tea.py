cup_size = input("input cup Size :").lower().strip()

if cup_size == "small":
    print(f'your prize of {cup_size} is : 10 rs')
elif cup_size == "medium":
     print(f'your prize of {cup_size} is : 15 rs')
elif cup_size == "large":
     print(f'your prize of {cup_size} is : 20 rs') 
else:
    print("Unknow cup size")   