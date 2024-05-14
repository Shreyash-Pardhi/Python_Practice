def generate():
    a,b=0,1
    while(a<100):
        yield a
        a,b=b,a+b
    
gen = generate()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))