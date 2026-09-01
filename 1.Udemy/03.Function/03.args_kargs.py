

#  *args allows a function to accept any number of positional arguments.
#                        while
# **kwargs allows a function to accept any number of keyword arguments.

# note -- *args type : <class 'tuple'> and **kwargs type : <class 'dict'>




def special_chai(*normal, **special):
    print("normal :", normal)
    print("special :", special)
    print(f"*args type : {type(normal)} and **kwargs type : {type(special)}")

special_chai("plain","with sugar","without sugar", lauxary1 = "green tea", lauxary2 = 'masala tea'  )



# **kwargs example
# def student(**kwargs):
#     print(kwargs)

# student(name="Vishal", age=25, course="MCA")