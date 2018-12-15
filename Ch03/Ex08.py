money = 1000000 #저금한 금액
year = 5 #저축기간
rate = 0.05 #이자율을 나타냄

sum_money = money*(1 + rate)**year #복리계산법

print("원금이", money, "원이고, 이자율이", rate * 100,"%이며", year,
      "년동안 저축하였을경우 합계는" ,sum_money, "원입니다.")
