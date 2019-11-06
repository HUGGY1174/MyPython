import turtle
t=turtle.Turtle()
t.shape("turtle")
pen=["blue","red","orange","green","purple"]
c=["공부","친구","이성","외모","기타"]
s=["50","26","32","25","17"]
t.pensize(2)

def bar(category,score):
    t.begin_fill()
    t.left(90)
    t.forward(score)
    t.write(category+" "+str(score)+"점")
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(score)
    t.left(90)
    t.end_fill()
    t.forward(10)

for i in range(0,5):
    t.color(pen[i])
    category=c[i]
    score=int(s[i])
    bar(category,score)
