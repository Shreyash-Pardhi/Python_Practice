ans = 0
 
def add():
    val = int(input("Enter the value: "))
    global ans
    ans = ans+val
    return f"Total: {ans}"
        
def sub():
    val = int(input("Enter the value: "))
    global ans
    ans = ans - val
    return f"Total: {ans}"
        
def mul():
    val = int(input("Enter the value: "))
    global ans
    ans = ans * val
    return f"Total: {ans}"
        
def div ():
    global ans
    val = int(input("Enter the value: "))
    if val==0:
        print("Can't divide by zero...")
        return f"Total: {ans}"
    ans = ans/val
    return f"Total: {ans}"
        
def power ():
    val = int(input("Enter the value: "))
    global ans
    ans = ans**val
    return f"Total: {ans}"