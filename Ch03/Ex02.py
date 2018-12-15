import turtle
t = turtle.Turtle()
t.shape("turtle")

n = int(input("몇각형을 그리시겠어요?"))

angle = 360//n
side = 10

for i in range(n):
    t.forward(side)
    t.left(angle)
