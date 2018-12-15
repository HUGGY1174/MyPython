num = int(input("네자리 숫자를 입력하시오:"))

num1000 = num // 1000
num100 = (num % 1000) // 100
num10 = num // 10
num1 = num % 10

print("자리수의 합:", num1 + num10 + num100 + num1000)
