class ChaiOrder :
    
    def __init__(self ,Chai_type , sweetness , size  ):
        self.chai_type = Chai_type
        self.sweetness = sweetness
        self.size = size
        
    @classmethod
    def from_dict(cls, order_details):
        return cls(
            order_details["chai_type"],
            order_details["sweetness"],
            order_details["size"]   
        )
    

    @classmethod
    def from_string(cls, order_details):
        chai_type , sweetness , size = order_details.split("-")
        return cls(chai_type, sweetness , size )
    
    
    def prepare(self):
        print(f"we are preparing your - {self.chai_type} with - {self.size} size along with - {self.sweetness} sweetness")
    
dict_Data = {
    "chai_type": "green Tea",
    "sweetness": "low",
    "size": "medium"
}

string_data = "Masala chai - medium - large"

order1 = ChaiOrder.from_dict(dict_Data)
order2 = ChaiOrder.from_string(string_data)

print(order1.__dict__)
print(order2.__dict__)

order1.prepare()
order2.prepare()