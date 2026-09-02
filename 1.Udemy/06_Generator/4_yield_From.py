def local_chai():
    yield "Masala Chai"
    yield "Lemon Tea"
    
def imported_chai():
    yield "Matcha"
    yield "Oolong"
    
def chai_menu():
    yield from local_chai()
    yield from imported_chai()
    
full_menu = chai_menu()

for chai in full_menu:
    print(chai)
    
