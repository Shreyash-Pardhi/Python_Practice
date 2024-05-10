#list
l1 = [1,2.5,'a','shr'] #list -Mutable
l2 = ['a','b','c']
print(l1,'\n', l2)

#List operations
print(len(l1)) #no. of elements on an list
print(l1[-1]) # used to print elements at specific index
l1.append([1,2,3,4]) #enters an element to a list at the end
print(l1)
l1.extend([1,2,3,4]) #enters multiple elements(iterable) in a list 
print(l1)
l1.remove('shr') #removes 1st occurence of value
print(l1)
#print(l1.sort()) sorts elements in a list
l2.insert(2,'inserted1') # inserts element at specific position
print(l2)
l2.pop() #removes last element by default and if given a index, deletes that index
print(l2)
l2.reverse() #reverses the order of elements
print(l2)
l2.clear() #removes all elements from list
print(l2)
print('\n')

#touple
t1 = (1,2.5,'a','shr',True) #touple -Immutable
t2 = ('a','b','c')
print(t1,'\n', t2)
#touple is immutable so we can't add, delete or update the content of it.

#touple operations
print(len(t1)) #length of touple
print(t1.count('a')) #counts given element occorences in a touple
print(t1.index('shr')) #provides the index of given element in a touple
print(t1[-1]) #used to print elements at specific index