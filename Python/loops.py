#for loop
for i in range(1,11):
    print(2*i)


list=[1,2,3,'a','b','c']

for i in list:
    print(i)
#or
print('\n')
for i in range(len(list)):
    print(list[i])

dict = {1:'a', 2:'b', 3:'c'}
for i in dict:
    print(f'{i}:{dict[i]}')




#while
tuple = ('t1','t2',3,6)
i=0
while(i<len(tuple)):
    print(tuple[i])
    i+=1

dict = {1:'a', 2:'b', 3:'c'}
i=1
while(i<=len(dict)):
    print(dict[i])
    i+=1