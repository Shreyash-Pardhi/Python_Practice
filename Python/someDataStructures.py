# Frozen set
import collections


s={1,2,23,4,45,6}
print(s,'\n',type(s))
f = frozenset(s)
print(f,'\n',type(f))
print('\n')

#byte array: can efficiently store large binary data
arr = bytearray('shreyash','utf-16','failed for some reason')
print(arr)

#ordered dictionary
d={1:'a',2:'b',3:'c'}
od=collections.OrderedDict({1:'a',2:'b',3:'c'})
print(d,'\n',od)

d.pop(2)
od.pop(2)
print(d,'\n',od)

d[2]='b'
for k,v in d.items():
    print(k,v)

od[2]='b'
for k,v in od.items():
    print(k,v)


#Deque (Doubly Ended Queue)
de=collections.deque((1,2,3,4))
de.appendleft(5)
print(de)
de.popleft()
print(de)

#named tuple
st = collections.namedtuple('stu',['n','a','dob'])
s = st('shreyash','22','121313')
print(s.a)

