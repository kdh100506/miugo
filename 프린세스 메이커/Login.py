from Repository import repo as repo
from Login_System import LoginSystem

def Start_Menu(current_user=None):
    # 매개변수로 전달받은 current_user 상태 유지
    while True:
        user_list = repo.load_repo()
        
        # 동기화 및 삭제된 유저 처리
        if current_user:
            found = False
            for u in user_list:
                if u.my_id == current_user.my_id:
                    current_user = u
                    found = True
                    break
            if not found:
                current_user = None

        user_status = f" ({current_user.my_name} 로그인 됨 | Scene {current_user.current_scene})" if current_user else " (로그인 필요)"

        print(f"""\n{"="*20}시작 메뉴{user_status}{"="*20}
    1. 회원가입
    2. 로그인
    3. 내 정보 및 계정 관리
    4. 게임 시작
    0. 종료""")
        try:
            choice = int(input("\n선택하기: "))

            if choice == 1:
                LoginSystem.make_user(user_list)
            elif choice == 2:
                user = LoginSystem.login(user_list)
                if user:
                    current_user = user
            elif choice == 3:
                if current_user is None:
                    print("\n로그인된 유저 정보가 없습니다. 먼저 로그인 해주세요.")
                else:
                    print(f"""\n{"="*20} 계정 및 정보 관리 {"="*20}
    1. 내 정보 조회
    2. 딸 스탯 그래프 보기 (Seaborn)
    3. 내 정보 수정
    4. 계정 삭제
    5. 로그아웃
    0. 메인 메뉴로 돌아가기""")
                    sub_choice = input("\n선택하기: ")
                    if sub_choice == '1':
                        LoginSystem.check_user(current_user)
                    elif sub_choice == '2':
                        LoginSystem.show_stat_chart(current_user)
                    elif sub_choice == '3':
                        LoginSystem.edit_user(current_user)
                    elif sub_choice == '4':
                        if LoginSystem.delete_user(current_user):
                            current_user = None
                    elif sub_choice == '5':
                        print(f"\n[{current_user.my_name}]님, 성공적으로 로그아웃되었습니다.")
                        current_user = None
                    elif sub_choice == '0':
                        pass
                    else:
                        print("\n올바른 번호를 선택해 주세요.")
            elif choice == 4:
                if current_user is None:
                    print("\n게임을 시작하려면 먼저 로그인 해주세요.")
                else:
                    if 1 < current_user.current_scene <= 14:
                        print(f"\n기존 저장 데이터가 있습니다. (현재 위치: Scene {current_user.current_scene})")
                        print("1. 이어서 시작하기")
                        print("2. 처음부터 다시하기")
                        sub_choice = input("선택: ")
                        if sub_choice == '2':
                            current_user.current_scene = 1
                            current_user.stats = {
                                'Stamina': 0, 'MuscularStrength': 0, 'Intellect': 0,
                                'Dignity': 0, 'Tenacity': 0, 'Attractiveness': 0, 'Morality': 0
                            }
                            repo.update_user_stats(current_user)
                    elif current_user.current_scene > 14:
                        print("\n이전 회차를 완료한 상태입니다. 처음부터 새로 시작합니다.")
                        current_user.current_scene = 1
                        current_user.stats = {
                            'Stamina': 0, 'MuscularStrength': 0, 'Intellect': 0,
                            'Dignity': 0, 'Tenacity': 0, 'Attractiveness': 0, 'Morality': 0
                        }
                        repo.update_user_stats(current_user)

                    print(f"\n[{current_user.daughter_name}] 키우기 게임을 시작합니다!")
                    return current_user
            elif choice == 0:
                print("\n시스템을 종료 합니다.")
                return None
            else:
                print("\n올바른 번호를 선택해 주세요.")
        except ValueError:
            print("\n입력값이 잘못 되었습니다.")