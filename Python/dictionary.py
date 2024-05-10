dict1 = {1:'a', 2:'b', 3:'c'} #dictionaty initialization #dict{key:value}
#dictionary is mutable
print(dict1)
print(len(dict1))
print(dict1.get(3))# takes a key and give value that is assosiated with the key
print(dict1.values())#printing all the values in a dict
print(dict1.setdefault(5, 'modified')) #if key exists returns a value of that key, if key doesn't exsist the creates the key with given value.
print(dict1)
dict1.update({1:'updated'}) #updates the key's value if exist else creates a new key with value
print(dict1)
dict2=dict1.copy() #copies one dict content to other
print(dict2)
print(dict2.items()) #provides a set like view at dict elements
dict2.pop(2) #takes key and deletes key:value pair
print(dict2)
dict2.popitem()# removes last key:value pair
print(dict2)
dict2.clear()
print(dict2)

k=(1,2,3,4,5)
v= "values"
print(dict2.fromkeys(k,v)) #created a dict with specific keys and values