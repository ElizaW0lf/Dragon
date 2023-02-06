import turtle
t = turtle.Turtle()
s=turtle.Screen()
#Body
for c in ['blue', 'blue', 'blue', 'blue']:
    t.color(c)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
t.right(90)
#Leg 1
for c in ['green', 'green', 'green', 'green']:
    t.color(c)
    t.forward(100)
    t.left(90)
    t.forward(55)
    t.left(90)
t.left(90)
t.forward(145)
t.right(90)
#Leg 2
for c in ['green', 'green', 'green', 'green']:
    t.color(c)
    t.forward(100)
    t.left(90)
    t.forward(55)
    t.left(90)
t.left(90)
t.forward(55)
t.left(90)
t.forward(65)
t.right(50)
#Neck
for c in ['black', 'black', 'black', 'black']:
    t.color(c)
    t.forward(100)
    t.left(90)
    t.forward(45)
    t.left(90)
t.forward(100)
t.left(90)
t.right(140)
t.right(10)
t.backward(38)
#Head
for c in ['red', 'red', 'red', 'red']:
    t.color(c)
    t.forward(100)
    t.left(90)
    t.forward(45)
    t.left(90)
#Wings
t.left(90)
t.forward(23)
t.left(150)
t.forward(100)
t.right(100)
t.forward(150)
t.left(90)
#Tail
for c in ['blue', 'blue', 'blue', 'blue']:
    t.forward(97)
    t.left(120)
    t.forward(90)
t.forward(71)
t.right(150)
t.forward(157)
t.left(50)
t.forward(150)
t.left(165)
t.forward(126)

s.exitonclick()
