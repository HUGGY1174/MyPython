import turtle
t=turtle.Turtle()
t.shape("turtle")
pen=["blue","red","orange","green","purple"]
c=["공부","친구","이성","외모","기타"]
s=["50","26","32","25","17"]
t.pensize(2)

def bubble(category,score):
    t.begin_fill()
    t.circle(score)
    t.end_fill()
    t.color("black")
    t.write(category+" "+str(score)+"점")
    t.penup()
    t.forward(100)
    t.right(70)
    t.pendown()

for i in range(0,5):
    t.color(pen[i])
    category=c[i]
    score=int(s[i])
    bubble(category,score)
