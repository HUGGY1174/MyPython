import random
x = random.randint(2, 10)
y = random.randint(1, 10)

while True:
    print(x, "x", y, "=", end=" ")
    userNo = int(input())

    if userNo == (x*y):
        print("맞았습니다.")
        break
