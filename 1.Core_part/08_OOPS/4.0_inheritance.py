class car :
    
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model
        
    
    def fullName(self):
        return f"{self.brand} {self.model}"
    
    def display(self):
        
        print(f"Car Model : {self.model} and Car brand : {self.brand}")
        
        
        
class ElectricCar(car):
    
    # Explicit call
    # def __init__(self, brand, model , battery_size):                
    #     car.__init__(self , brand, model)
    #     self.battery = battery_size
        
        
        
 # super() is used to access behavior from a parent class according to Python's method resolution order.
    def __init__(self, brand, model , battery_size):        
        super().__init__(brand, model)
        self.battery = battery_size
        
    def display(self) :
        print(f" Name and Model :{self.fullName()} and battery size : {self.battery}")   
        
        
c1 = ElectricCar("Toyota", "Urban Cruiser Ebella", "61kWh")
c1.display() 
        
c2 = car("tesla", "model s")
c2.display()        


# display() method show overriding because both class has a same method with same parameter and one class inherit from other