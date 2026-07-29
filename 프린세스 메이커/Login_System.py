import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from Info import Login
from Repository import repo as repo

class LoginSystem:
    def check_space(ordinal_number):
        text_list = ["내 이름을 입력하세요: ", "딸의 이름을 입력하세요: ", "비밀번호를 입력하세요: "]
        while True:
            value = input(text_list[ordinal_number])
            if value.replace(" ", "") == "":
                print("\n빈 값이거나 공백입니다. 다시 입력해주세요.\n")
                continue
            return value

    def make_user(user_list):
        while True:
            my_id = input("아이디를 입력하세요: ")

            for user in user_list:
                if my_id == user.my_id:
                    print("\n같은 id가 있습니다. 메인 메뉴로 돌아갑니다.")
                    return None

            if my_id.replace(" ", "") == "":
                print("\n빈 값이거나 공백입니다. 다시 입력해주세요.\n")
                continue
            break

        my_name = LoginSystem.check_space(0)
        daughter_name = LoginSystem.check_space(1)
        password = LoginSystem.check_space(2)

        user = Login(my_id, my_name, daughter_name, password)
        repo.write_repo(user)
        print("\n회원가입 성공!")
        return user

    def login(user_list):
        login_id = input("\n로그인 할 아이디: ")

        for user in user_list:
            if login_id == user.my_id:
                login_password = input("패스워드: ")
                if login_password != user.password:
                    print("\n비밀번호가 일치하지 않습니다. 메뉴로 돌아갑니다.")
                    return None
                else:
                    print(f"\n[로그인 성공]\n당신의 이름: {user.my_name}\n당신 딸의 이름: {user.daughter_name}")
                    return user

        print("\n존재하지 않는 아이디입니다.")
        return None

    def check_user(user):
        if user is None:
            print("\n로그인된 유저 정보가 없습니다. 먼저 로그인 해주세요.")
            return

        # NumPy를 사용한 평균 능력치 계산
        stat_values = list(user.stats.values())
        avg_stat = np.mean(stat_values)

        print(f"""\n{"="*20} 내 정보 {"="*20}
내 아이디: {user.my_id}
내 이름: {user.my_name}
내 딸 이름: {user.daughter_name}
현재 진행 위치: Scene {user.current_scene}
[딸의 현재 스탯] (평균: {avg_stat:.1f})
 - 체력: {user.stats['Stamina']} | 근력: {user.stats['MuscularStrength']} | 지력: {user.stats['Intellect']}
 - 기품: {user.stats['Dignity']} | 근성: {user.stats['Tenacity']} | 매력: {user.stats['Attractiveness']} | 도덕성: {user.stats['Morality']}
{"="*38}""")

    def show_stat_chart(user):
        """Seaborn 및 Pandas를 활용한 딸의 스탯 시각화"""
        if user is None:
            print("\n로그인된 유저 정보가 없습니다.")
            return

        # Pandas DataFrame 변환
        df = pd.DataFrame(list(user.stats.items()), columns=['Stat', 'Value'])

        # Seaborn 바차트 생성
        plt.figure(figsize=(8, 5))
        sns.barplot(x='Stat', y='Value', data=df, hue='Stat', legend=False, palette='viridis')
        plt.title(f"[{user.daughter_name}] Stat Graph (Scene {user.current_scene})")
        plt.xlabel("Stat Type")
        plt.ylabel("Value")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

    def edit_user(user):
        """계정 수정 기능"""
        if user is None:
            print("\n로그인된 유저 정보가 없습니다. 먼저 로그인 해주세요.")
            return

        print(f"""\n{"="*20} 계정 정보 수정 {"="*20}
1. 내 이름 변경
2. 딸 이름 변경
3. 비밀번호 변경
0. 취소""")
        choice = input("\n선택하기: ")

        if choice == '1':
            new_name = LoginSystem.check_space(0)
            user.my_name = new_name
            repo.update_user(user)
            print("\n[내 이름이 성공적으로 변경되었습니다.]")
        elif choice == '2':
            new_daughter_name = LoginSystem.check_space(1)
            user.daughter_name = new_daughter_name
            repo.update_user(user)
            print("\n[딸 이름이 성공적으로 변경되었습니다.]")
        elif choice == '3':
            current_pw = input("현재 비밀번호를 입력하세요: ")
            if current_pw != user.password:
                print("\n비밀번호가 일치하지 않습니다.")
                return
            new_pw = LoginSystem.check_space(2)
            user.password = new_pw
            repo.update_user(user)
            print("\n[비밀번호가 성공적으로 변경되었습니다.]")
        elif choice == '0':
            print("\n수정을 취소합니다.")
        else:
            print("\n올바른 번호를 선택해 주세요.")

    def delete_user(user):
        """계정 삭제 기능"""
        if user is None:
            print("\n로그인된 유저 정보가 없습니다. 먼저 로그인 해주세요.")
            return False

        print(f"""\n{"="*20} 계정 삭제 {"="*20}""")
        confirm_pw = input("계정을 삭제하려면 현재 비밀번호를 입력하세요: ")

        if confirm_pw != user.password:
            print("\n비밀번호가 일치하지 않습니다. 삭제가 취소됩니다.")
            return False

        answer = input("정말로 계정을 삭제하시겠습니까? (Y/N): ")
        if answer.upper() == 'Y':
            repo.delete_user(user.my_id)
            print(f"\n[{user.my_id}] 계정이 성공적으로 삭제되었습니다.")
            return True
        else:
            print("\n계정 삭제가 취소되었습니다.")
            return False