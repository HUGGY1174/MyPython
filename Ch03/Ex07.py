in_money = int(input("투입한 돈:"))           
price = int(input("물건 값:"))

change = in_money - price

print("거스름돈:", change)
coin500 = change // 500
coin100 = (change % 500) // 100
remain = change - coin500 * 500 - coin100 * 100

print("500원 동전의 개수:", coin500)
print("100원 동전의 개수:", coin100)
print("완전 잔돈:", remain, "원")
