# def fun(func):
#     return ''.join(reversed(func))

# def val(str):
#     return str
    
# if __name__ == "__main__":
#     print(fun(val('shreyash')))
    
##Class As a Decorator
# class A:
#     def __init__(self, func):
#         self.func = func
    
#     def __call__(self,*args):
#         self.func(*args)     
# @A
# def fun(a,b):
#     print('add: ', a+b)

# fun(10,20)

def decorater(func):
    def fun(*args, **kwargs):
        func(*args, **kwargs)
        print(f"Thank You for using {func.__name__} functionality")
    return fun

@decorater
def Addition(a, b):
    print(f"Addition of {a} and {b} is {a+b}")

@decorater
def shutdown(x:bool):
    print("\nShutting down operations" if x else "\nShutdown processes cancelled")

Addition(10,20)
shutdown(False)