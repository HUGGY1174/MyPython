import turtle
t=turtle.Turtle()
def f():
    t.forward(100)
    t.left(60)

def h():
    f(),f(),f(),f(),f(),f()

def g():
    h()
    t.forward(100)
    t.right(60)

g(),g(),g(),g(),g(),g()
