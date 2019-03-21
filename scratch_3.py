import turtle
wn = turtle.Screen()
a = turtle.Turtle()
a.pensize(5)
a.speed(300)
for i in range(300):
    a.pencolor("red")
    a.circle(5)
    a.left(50)
    a.fd(i)
turtle.done()
