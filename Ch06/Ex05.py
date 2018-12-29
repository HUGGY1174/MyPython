sumAll = 0

while True:
    print("정수를 입력하세요.", end="")
    userNo = int(input())
    sumAll = sumAll + userNo
    if userNo == 0:
        break
print("합은", sumAll, "입니다.")

