count = 0

import random
compNo = random.randint(1, 100)
userNO = 0

while compNo != userNO:
    userNO = int(input("1~100까지의 수를 입력하세요"))
    if compNo > userNO:
        print("입력한 숫자보다 큽니다.")
    elif compNo < userNO:
        print("입력한 숫자보다 작습니다.")
    else:
        print("맞습니다! 축하합니다!")
    count = count + 1
print(count, "번만에 맞혔습니다.")


