sumAll = 0
answer = "yes"

while answer == "yes":
    n = int(input("수를 입력하세요."))
    sumAll = sumAll + n
    answer = input("계속할까요.(yes/non)")
print("합계는", sumAll, "입니다.")
