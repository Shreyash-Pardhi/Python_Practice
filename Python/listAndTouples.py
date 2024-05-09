#list
l1 = [1,2.5,'a','shr'] #list -Mutable
l2 = ['a','b','c']
print(l1,'\n', l2)

#List operations
print(len(l1)) #no. of elements on an list
l1.append([1,2,3,4]) #enters an element to a list at the end
print(l1)
l1.extend([1,2,3,4]) #enters multiple elements(iterable) in a list 
print(l1)
l1.remove('shr') #removes 1st occurence of value
print(l1)
#print(l1.sort()) sorts elements in a list
