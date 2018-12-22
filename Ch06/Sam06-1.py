age = int(input("나이를 입력하세요."))
height = int(input("키를 입력하세요."))

if age >= 13 and height >= 140:
    print("놀이기구를 즐겨주세요.")

elif age < 13 and height >= 140:
    print("나이가 안되시네요..놀이기구를 탈 수 없습니다.")

elif age >= 13 and height < 140:
    print("키가 안되시네요..놀이기구를 탈 수 없습니다.")

else :
    print("나이와 키가 안되서 놀이기구를 탈 수 없습니다.")

