# break: terminates the loop/flow
a=20
for i in range(50):
    if(i==a):
        print(f'found a at i:{i}')
        break
    else:
        print(f'Not found a at i:{i}')

print('\n')
# Continue: terminates the current iteration of loop and continues with remaining iterations
a=20
for i in range(50):
    if(i==a):
        print(f'found a at i:{i}')
        continue
    else:
        print(f'Not found a at i:{i}')