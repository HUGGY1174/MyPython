login_id = input("아이디를 입력하세요.")
pwd = input("비밀번호를 입력하세요.")

com_id = "min"
com_pwd = "1174"

if login_id == com_id:
    if pwd == com_pwd:
        print("-로그인-.")
    else :
        print("암호가 잘못 되었습니다.")
else :
    print("존재하지 않는 아이디입니다.")
