import random
score=0

def cal():
    global score
    a=random.randint(1,10)
    b=random.randint(1,10)
    c=random.randint(1,3)
    if c==1:
        op="+"
    elif c==2:
        op="-"
    else:
        op="x"

    print(a,op,b)
    res=int(input("="))

    if op=="=+":
        if (a+b)==res:
            score+=20
            print("정답")

    elif op=="-":
        if (a-b)==res:
            score +=20
            print("정답")

    else:
        if (a*b)==res:
            score +=20
            print("정답")


for i in range(5):
    cal()

print("획득한 점수:",score)
