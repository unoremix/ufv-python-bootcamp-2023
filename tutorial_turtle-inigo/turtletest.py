simport turtle
s = turtle.getscreen()
t = turtle.Turtle()
turtle.bgcolor("darkgreen")

t.right(90)
t.forward(100)
t.left(90)
t.backward(100)

t.goto(100,100)

t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)

t.circle(60)

t.dot(20)

t.shapesize(1,5,10)
t.shapesize(10,5,1)
t.shapesize(1,10,5)
t.shapesize(10,1,5)

t.shapesize(3,3,5)
t.fillcolor("orange")

t.begin_fill()
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.end_fill()

t.shape("turtle")
t.shape("arrow")
t.shape("circle")

t.speed(3)
t.forward(100)
t.speed(10)
t.forward(100)

t.pencolor("purple")
t.fillcolor("orange")
t.pensize(10)
t.speed(9)
t.begin_fill()
t.circle(70)
t.end_fill()

t.pen(pencolor="purple", fillcolor="orange", pensize=10, speed=9)
t.begin_fill()
t.circle(80)
t.end_fill()
t.fd(65)
t.rt(70)
t.penup()
t.fd(55)
t.rt(60)
t.pendown()
t.fd(90)
t.rt(90)
t.penup()
t.fd(90)
t.pendown()

t.stamp()
8
t.fd(100)
t.stamp()
9
t.fd(100)

c = t.clone()
t.color("magenta")
c.color("silver")
t.circle(25)
c.circle(75)

t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)

n=10
while n <= 40:
   t.circle(n)
   n = n+10

