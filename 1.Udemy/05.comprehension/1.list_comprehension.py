Chai_menu = [
    "ICED MASALA TEA",
    "ICED LEMON TEA",
    "GREEN TEA",
    "GINGER TEA",
    "MASALA TEA",
    "COLD COFFIE",
    "HOT COFFIE",
]
# [expression for item in iterable if condition] 
#  Q1 -create a list for all iced tea from menu
iced_tea = [tea for tea in Chai_menu if "ICED" in tea]
print(iced_tea)


# Question 2 — Find Tea Items 
# tea_item= [tea for tea in Chai_menu if "tea" in tea.lower()]
# print(tea_item)

            # or 
tea_item2 = [t for t in Chai_menu if t.lower().endswith("tea")]
print("Tea item :",tea_item2)




# Question 3 — Find Coffee Items

coffie_item = [t for t in Chai_menu if t.lower().endswith("coffie")]
print("coffie item :", coffie_item)




# Question 4 — Find Non-Iced Drinks

non_iced_drink = [ x for x in Chai_menu if not  x.lower().startswith(("iced" , "cold")) ]
print(non_iced_drink)

                #  or
# non_iced_drink = [
#     x for x in Chai_menu
#     if "iced" not in x.lower() and "cold" not in x.lower()
# ]                


# Question 5 — Convert only  Tea Names to Lowercase inside the tea menu list

lowerCase_name = [x.replace("TEA","tea") for x in Chai_menu if "tea" in x.lower()]
print("tea lower case ", lowerCase_name)