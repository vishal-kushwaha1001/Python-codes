class BaseChai :
    
    def __init__(self, type_):
        self.type_ = type_
        
    
    def prepare(self):
        print(f"Preparing {self.type_} chai.......")
        
        
# Inheritance  
class MasalaChai(BaseChai):
    
    def add_spices(self):
        print("Adding cardamom , ginger , cloves .")
        


# composition

class  ChaiShop:
    chai_cls = BaseChai
    
    def __init__(self):
        self.chai = self.chai_cls("Regular")  # self.chai = BaseChai("Regular")
        
        
    def server(self):
        print(f"Serving {self.chai.type_} chai in the shop")
        self.chai.prepare()


# Inheritance and Decomposition 
class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai
    
    # the inherited __init__() runs:
    #  when we  call chai_cls then  it call---
    #   self.chai = MasalaChai('Regular')
    



shop = ChaiShop()
fancy = FancyChaiShop()

shop.server()
fancy.server()
fancy.chai.add_spices()  #self.chai = MasalaChai('Regular')
print(fancy.chai.type_)
fancy.chai.prepare()


# fancy.chai_cls.add_spices()    #-- It gives error because add_spices() is a
# instance method it didn't provide an object for self.

