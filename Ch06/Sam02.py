fig = int(input("몇각형을 그릴까요?"))

import turtle

t = turtle.Turtle()

for i in range(fig):
    t.forward(30)
    t.left(360/fig)
    
