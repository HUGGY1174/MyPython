americano = 2000
cafelatte = 3000
capucino = 3500

ame_no = int(input("아메리카노  판매 개수:"))
latte_no = int(input("카페라떼 판매 개수:"))
capu_no = int(input("카푸치노 판매 개수:"))

ame_sum = americano * ame_no
latte_sum = cafelatte * latte_no
capu_sum = capucino * capu_no

all_sum = str(ame_sum + latte_sum + capu_sum)

print("총 매출은", all_sum + "원 입니다.")
