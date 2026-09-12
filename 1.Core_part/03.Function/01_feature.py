#  feature - 
#           1- Hiding Implementation details
#           2- improve readeability 
#           3- improving traceability

# ------------------------------------------------------------
#        1- Hiding Implementation details

def get_input():
    print(" getting user input ")

def validate_input():
    print("Validating the user info")
    
def save_to_db():
    print("saving to the databases")
    
    
def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("user registeration complete")
    
    

register_user()
# ---------------------------------------------
#         2- improve readeability 





def calulate_bill(cup ,price_per_cup):
    return cup * price_per_cup


my_bill = calulate_bill(3,30)
print(my_bill)




# ---------------------------------------------
#           3- improving traceability


def add_vat(price , vat_rate):
    return price *(100 +vat_rate)/100

orders = [100 ,150 , 200]

for price in orders :
    final_amount = add_vat(price , 10)
    print(f"Original : {price} , final with Vat : {final_amount}")