import turtle 
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
t = turtle.Pen()
p = turtle.Pen()
t.speed(10)
p.speed(0)
turtle.bgcolor('black') 
for x in range(1,360): 
    t.pencolor(colors[x%6])
    p.pencolor(colors[x%6])
    t.width(x//100 + 1) 
    # p.width(360//x + 1)
    p.forward(x)
    t.forward(x)
    p.right(60) 
    t.left(50) 
