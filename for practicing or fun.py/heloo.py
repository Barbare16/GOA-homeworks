import turtle
t=turtle.Turtle()
#cloding.com
s = turtle.Screen()
colors=['orange','red','magenta','blue','magenta','yellow','green','cyan','purple']
s.bgcolor('black')
t.pensize('2')
t.speed(0)
for x in range (360):
    t.pencolor(colors[x%6])
    t.width(x//100+1)
    t.forward(x)
    t.right(59)
    turtle.hideturtle()























    