import turtle, random
t=turtle.Turtle()
s=t.getscreen()
s.setup(400,400)

color=["orange","purple","red","yellow","skyblue","green","pink","black","blue","hotpink"]

def 원그리기(x,y):
    i=random.randint(0,9)
    size=random.randint(10,80)
    t.penup()
    t.goto(x,y)
    t.dot(size,color[i])

s.onclick(원그리기)
