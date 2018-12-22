scoreKor = int(input("국어 점수를 입력하세요"))
scoreMath = int(input("수학 점수를 입력하세요"))
scoreEng = int(input("영어 점수를 입력하세요"))

avg = (scoreKor + scoreMath + scoreEng) / 3

print("평균은", str(avg)
      + "이고,")

if avg >= 90:
    print("A학점입니다.")

elif avg >= 80:
    print("B학점입니다.")

elif avg >= 70:
    print("c학점입니다.")

elif avg >= 60:
    print("D학점입니다.")

else :
    print("F학점입니다.")

