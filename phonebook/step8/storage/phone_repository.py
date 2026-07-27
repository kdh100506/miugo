import csv
import os
from models.phone_info import PhoneInfo, PhoneUnivInfo, PhoneCompanyInfo

class PhoneBookRepository:
    def __init__(self, file_name=None):
        if file_name is None:
            # 현재 파일(phone_repository.py)이 있는 위치 기준으로 프로젝트 루트(step07)의 data 폴더 경로를 자동으로 찾습니다.
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.file_name = os.path.join(base_dir, "data", "phone_book.csv")
        else:
            self.file_name = file_name

    # 💾 1. 데이터 저장 (Save)
    def save(self, data_list):
        # data 폴더가 존재하지 않을 경우 자동으로 생성합니다.
        os.makedirs(os.path.dirname(self.file_name), exist_ok=True)

        with open(self.file_name, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "phone", "birth", "region", "group", "memo"])
            
            for info in data_list:
                if isinstance(info, PhoneUnivInfo):
                    group = "대학"
                    memo = info.major
                elif isinstance(info, PhoneCompanyInfo):
                    group = "회사"
                    memo = info.company
                else:
                    group = "일반"
                    memo = ""
                
                writer.writerow([info.name, info.phone_number, info.birth, info.region, group, memo])
        print(f"💾 [{self.file_name}] 파일에 데이터가 안전하게 백업되었습니다.")

    # 📂 2. 데이터 불러오기 및 복원 (Load)
    def load(self):
        loaded_data = set()
        if not os.path.exists(self.file_name):
            return loaded_data
            
        with open(self.file_name, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            
            for row in reader:
                name, num, birth, region, group, memo = row
                
                birth = birth if birth != "" else None
                region = region if region != "" else None
                
                if group == "대학":
                    info = PhoneUnivInfo(name, num, major=memo, birth=birth, region=region)
                elif group == "회사":
                    info = PhoneCompanyInfo(name, num, company=memo, birth=birth, region=region)
                else:
                    info = PhoneInfo(name, num, birth=birth, region=region)
                    
                loaded_data.add(info)
        return loaded_data