class BankAccount :
    
    def __init__(self , user_account, Password ="abcdefgh" ):
        self.__user_account = user_account
        self.__Password = Password
        
    
    @property
    def user_account(self):
        return self.__user_account
    
    @property
    def Password(self):
        return self.__Password
    
    @Password.setter
    def Password(self , password):
        try:
            if len(password) >= 6 and len(password) <= 12:
                self.__Password = password
                print("Password set successfully")
            else:
                raise ValueError("password must be atleast more than 5 and less 13 character ")
        except ValueError as e :
            print(e)
            
    
user1 = BankAccount("vishal1001")
# print(user1.user_account)            
# print(user1.Password)

user1.Password = "kashyap2003"

print(f"userId : {user1.user_account} and password : {user1.Password} ")   
  
    

        