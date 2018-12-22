import random

num1 = random.randint(1,100)
num2 = random.randint(1,100)

a = str(num1) + "-" + str(num2) + "의 값은얼마인가요."
answer = int(input(a))

com_answer = num1 - num2

if com_answer == answer:
    print("정답입니다.")
else:
    print("오답입니다.")
