from functools import wraps


def my_decorators(func):
    @wraps(func)
    def wrapper():
        print("before function execution ")
        func()
        print("After Function executed")
        
    return wrapper
    
    
@my_decorators
def greet():
    print("hello , this is decorators")

greet()    
print(greet.__name__)