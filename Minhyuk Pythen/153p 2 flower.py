import turtle
t=turtle.Turtle()
t.pensize(3)

c=["blue","red","green","yellow","orange"]
for i in range(5):
    t.color(c[i])
    for j in range(5):
        t.forward(50)
        t.right(72)
    t.left(72)
