from functools import wraps

def log_activity(func):
    
    @wraps(func)
    def wrapper(*args ,**kwargs):
        print(f"starting : {func.__name__}")
        result = func(*args, **kwargs)
        print(f"finishing : {func.__name__}")
        
        return result
        
    
    
    return wrapper


@log_activity
def brew_chai(type , milk = "no"):
    print(f"brewing chai :{type} chai with Milk {milk}")
    
    
brew_chai("masala", milk=" yes")