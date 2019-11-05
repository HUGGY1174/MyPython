import turtle
t=turtle.Turtle()

def f():
    t.forward(100)
    t.left(90)

def h():
    f(),f(),f(),f()
    t.right(90)

h(),h(),h(),h()
