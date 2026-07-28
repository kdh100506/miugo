from system import LoginSystem
from repository import repo as repo

user_list = repo.load_repo()

while 1 :
    user_list = repo.load_repo()
    print(f"""\n{"="*30}뭐하실꺼임{"="*30}
1. 바로그냥회원가입
2. 바로그냥로그인
3. 내 정보
0. 껒@여""")
    try :
        choice = int(input("\n선택하기: "))

        if choice == 1 :
            LoginSystem.make_user(user_list)
        elif choice == 2 :
            user = LoginSystem.login(user_list)
        elif choice == 3 :
            try :
                LoginSystem.check_user(user)
            except NameError:
                print("\n유저 데이터가 없어용~")
        elif choice == 0 :
            print("\n어 종료할게 ㅇㅇ")
            break
    except ValueError:
        print("\n문자나 빈값 넣지마세용~")