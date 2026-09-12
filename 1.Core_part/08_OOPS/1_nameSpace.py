class chai():
    origin = "India"
    flavour = []
    
# Accessing property
# print(chai.origin)

# Adding value in  property
chai.flavour = ["masala", "ginger", "plane"]
chai.prices = [15,20,30,50]

# 
# print(chai.flavour)
print(chai.prices )


# creating object

person1 = chai()
print(person1.prices[1])

# 
person2 = chai()
person2.name = "vishal kumar"
print(person2.name)
print(person2.flavour)

