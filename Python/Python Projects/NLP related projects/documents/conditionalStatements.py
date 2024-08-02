#if statement
a=10
if(a==10):
    print(f'if: a is {a}')

#if-else
a=20
if(a==10):
    print(f'if: a is {a}')
else:
    print(f'else: a is {a}')

#if-elif-else
a=30
if(a==10):
    print(f'if: a is {a}')
elif(a==30):
    print(f'elif: a is {a}')
else:
    print(f'else: a is {a}')
    
    
#nested if-else
age=30
if(age!=0):
    if(age>50):
        print('senior')
    else:
        if(age>20 and age<50):
            print('young')
        else:
            if(age>10 and age<21):
                print('Teen')
            else:
                print('child')
else:
    print('invalid input')