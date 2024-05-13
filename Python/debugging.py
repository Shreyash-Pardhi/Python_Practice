#using print statement
def div1(x,y):
    print(f'Dividing {x} by {y}:')
    return f'Result: {x/y}'

print(div1(4,2))
print('\n')

#using assert statement
def div2(x,y):
    print(f'Dividing {x} by {y}:')
    assert y!=0, "can't be divided by zero" 
    return f'Result: {x/y}'

print(div2(4,2))

#using logging
import logging as log
def div3(x,y):
    log.debug('Dividing {} by {}:'.format(x,y))
    d = x/y
    return log.debug('Result: {}'.format(d))

print(div3(4,2))

#using Python Debugger PDB
import pdb
def div4(x,y):
    pdb.set_trace()
    print(f'Dividing {x} by {y}:')
    return f'Result: {x/y}'

print(div4(4,2))