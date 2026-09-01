# enumerate() is a built-in function used when you 
# want to loop over a sequence and get both the index and the value at the same time.

# Syntax
# enumerate(iterable, start=0)
# iterable → list, tuple, string, etc.
# start → starting index (default is 0)


# use case : enumerate() is useful whenever you need both the position (index) and the value while looping.
# -------------------------------------------------------------------------------------------------------------------


menu = ["green", "Lemon", 'Spiced', "mint"]
 
for i, item in enumerate(menu , start= 1):
    print(f"{i} : {item} tea") 






# output-
# 1 : green tea
# 2 : Lemon tea
# 3 : Spiced tea
# 4 : mint tea