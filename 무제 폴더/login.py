from system import LoginSystem
from repository import repo as repo

def Start_Menu():
    user_list = repo.load_repo()

    while 1 :
        user_list = repo.load_repo()
        print(f"""\n{"="*30}시작 메뉴{"="*30}
    1. 회원가입
    2. 로그인
    3. 내 정보
    0. 종료""")
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
                    print("\n유저 데이터가 없습니다")
            elif choice == 0 :
                print("\n시스템을 종료 합니다.")
                break
        except ValueError:
            print("\n입력값이 잘못 되었습니다.")