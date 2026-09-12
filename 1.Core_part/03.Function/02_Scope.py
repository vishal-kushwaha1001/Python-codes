# Scope and Name Resolution
#     -: Local -inside the function
#     -: Enclosing from outer function if nested
#     -: Global - top level script
#     -: bulit in
    
    
    
    #-----------local vs globel
# nonlocal is used inside a nested function when you want to modify a variable belonging to the outer function.
#   useful for counter 
def update_order():
    chai_type = "elaichi"
    def kitchen():
        nonlocal chai_type
        chai_type = "kesar"
    kitchen()
    print("After kitchen update " , chai_type)

update_order()





# global = modify a global variable.
chai_type01 ="plain"

def front_desk ():
    
    def kitchen():
        global chai_type01
        chai_type01 = "kesar"
    kitchen()
    print("After kitchen update " , chai_type01)

front_desk()