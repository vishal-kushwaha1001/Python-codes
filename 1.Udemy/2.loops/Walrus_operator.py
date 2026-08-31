# The Walrus Operator (:=), introduced in Python 3.8, allows you to assign a value to a variable 
# as part of an expression. It helps avoid redundant code when a value needs to be both used and
# tested in the same expression — especially in loops or conditional statements.

# Syntax ----
#            variable := expression 

# ------------------------------------------------------------------------------------------------------------



# Example 1 -
value = 19 

# without walrus operator
remainder = value % 4
if remainder:
    print("not devisible by 4")
    
    # with walrus operator
if remainder := value % 4:
    print(f"not devisible by 4 and remainder is {remainder}")    
    
    
    
    
    
    
    
    
    # Example 2
available_sizes = [ "small" , "medium", "large"]

if (requested_size := input("choose your cup size : ").lower()) in available_sizes:
    print(f"we are serving {requested_size} cup size tea")
else :
    print(f"not available - {requested_size} size cup tea")
    





# Example 3

flavours = ["masala" , "ginger", "lemon", "mint"]
print(f"available flavours : {flavours}")
while (flavour := input("choose your flavour : ")).lower() not in flavours: 
    print(f"Sorry {flavour} is not available ")
print(f"you are ordering - {flavour} tea")
    