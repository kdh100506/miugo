import csv
from info import Login

class Repository :
    def __init__(self,file_name="data/princess_repository.csv"):
        self.file_name = file_name

    def write_repo(self,user) :
        with open(self.file_name,"a",encoding="utf-8",newline="") as file :
            writer = csv.writer(file)

            row = [user.my_id,user.my_name,user.daughter_name,user.password]
            writer.writerow(row)

    def load_repo(self) :
        user_list = []

        try :
            with open(self.file_name, "r", encoding="utf-8") as file:
                reader = csv.reader(file)

                next(reader)

                for user in reader :
                    user = Login(user[0],user[1],user[2],user[3])

                    user_list.append(user)
                return user_list
        except :
            with open(self.file_name,"w",encoding="utf-8",newline="") as file :
                writer = csv.writer(file)
    
                writer.writerow(["내 아이디","내 이름","딸의 이름","비밀번호"])
            return user_list

repo = Repository()