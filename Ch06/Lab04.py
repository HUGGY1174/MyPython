import random
x = random.randint(1, 100)
y = random.randint(1, 100)
while True:
    #x = random.randint(1, 100)
    #y = random.randint(1, 100)
    print(x, "+", y, "의 값은?")
    userNo = int(input())
    if userNo == (x + y):
        print("정답입니다.")
        break
    else :
        print("오답입니다.")
        print("다른 문제를 풀어보세요.")
