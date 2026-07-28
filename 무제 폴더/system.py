from info import Login
from repository import repo as repo

class LoginSystem:
    def check_space(ordinal_number) :
        text_list = ["내 이름을 입력하세요: ","딸의 이름을 입력하세요: ","비밀번호를 입력하세요: "]
        while True:
            value = input(text_list[ordinal_number])
            if value.replace(" ","") == "" :
                print("\n빈 값이거나 공백입니다. 다시 입력해주세요.\n")
                continue
            return value

    def make_user(user_list) :
        ordinal_number = 0
        while True :
            my_id = input("아이디를 입력하세요: ")

            for user in user_list :
                if my_id == user.my_id :
                    print("\n같은 id가 있습니다. 바탕화면으로 돌아갑니다.")
                    return

            if my_id.replace(" ","") == "" :
                print("\n빈 값이거나 공백입니다. 다시 입력해주세요.\n")
                continue
            break

        while True :
            my_name = LoginSystem.check_space(ordinal_number)
            ordinal_number = 1
            daughter_name = LoginSystem.check_space(ordinal_number)
            ordinal_number = 2
            password = LoginSystem.check_space(ordinal_number)
            break

        user = Login(my_id,my_name,daughter_name,password)
        repo.write_repo(user)
        print("\n성공")
        return

    def login(user_list) :
        for user in user_list :
            print(user.my_name)
        login_name = input("\n로그인 할 내 이름: ")

        for user in user_list :
            if login_name == user.my_name :
                login_password = input("패스워드: ")
                if login_password != user.password :
                    print("\n비밀번호가 일치하지 않습니다. 바탕화면으로 돌아갑니다.")
                    return
                else :
                    print(f"""\n당신의 이름: {user.my_name}
당신 딸의 이름: {user.daughter_name}
로그인 성공. 바탕화면으로 돌아갑니다.""")
                    return user

    def check_user(user) :
            print(f"""\n내 이름:{user.my_name}
내 딸 이름:{user.daughter_name}""")