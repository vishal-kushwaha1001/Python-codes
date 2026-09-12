from functools import wraps


def auth_Admin(func):
    
    @wraps(func)
    def wrapper(role):
        if role != "admin":
            print("Access Denied : Admins only")
            return None
        else :
            return func(role)
    return wrapper


@auth_Admin
def teaching(role):
    print("Access Granted to head Master Admin")
    
teaching("admin")
teaching("user")
    
        

        