import pandas as pd
import os
from info import Login

class Repository:
    def __init__(self, file_name="user_repository.csv"):
        self.file_name = file_name
        self.headers = [
            "my_id", "my_name", "daughter_name", "password",
            "Stamina", "MuscularStrength", "Intellect", "Dignity", "Tenacity", "Attractiveness", "Morality",
            "current_scene"
        ]

    def save_all_users(self, user_list):
        """Pandas DataFrame을 사용하여 전체 유저 데이터 저장"""
        data = []
        for user in user_list:
            data.append({
                "my_id": user.my_id,
                "my_name": user.my_name,
                "daughter_name": user.daughter_name,
                "password": user.password,
                "Stamina": user.stats.get('Stamina', 0),
                "MuscularStrength": user.stats.get('MuscularStrength', 0),
                "Intellect": user.stats.get('Intellect', 0),
                "Dignity": user.stats.get('Dignity', 0),
                "Tenacity": user.stats.get('Tenacity', 0),
                "Attractiveness": user.stats.get('Attractiveness', 0),
                "Morality": user.stats.get('Morality', 0),
                "current_scene": user.current_scene
            })
        
        # Pandas DataFrame 생성 및 CSV 저장
        df = pd.DataFrame(data, columns=self.headers)
        df.to_csv(self.file_name, index=False, encoding="utf-8")

    def write_repo(self, user):
        user_list = self.load_repo()
        user_list.append(user)
        self.save_all_users(user_list)

    def update_user_stats(self, target_user):
        self.update_user(target_user)

    def update_user(self, target_user):
        """유저 정보(이름, 비밀번호, 스탯 등) 수정 반영"""
        user_list = self.load_repo()
        for i, user in enumerate(user_list):
            if user.my_id == target_user.my_id:
                user_list[i] = target_user
                break
        self.save_all_users(user_list)

    def delete_user(self, target_id):
        """Pandas의 불리언 인덱싱을 활용한 계정 삭제 처리"""
        if os.path.exists(self.file_name):
            df = pd.read_csv(self.file_name, encoding="utf-8")
            # Pandas 필터링: 해당 ID가 아닌 행만 남김
            df_filtered = df[df['my_id'].astype(str) != str(target_id)]
            df_filtered.to_csv(self.file_name, index=False, encoding="utf-8")

    def load_repo(self):
        """Pandas pd.read_csv를 통한 유저 목록 로드"""
        user_list = []
        if not os.path.exists(self.file_name):
            df = pd.DataFrame(columns=self.headers)
            df.to_csv(self.file_name, index=False, encoding="utf-8")
            return user_list

        try:
            df = pd.read_csv(self.file_name, encoding="utf-8")
            if df.empty:
                return user_list

            for _, row in df.iterrows():
                stats = {
                    'Stamina': int(row['Stamina']),
                    'MuscularStrength': int(row['MuscularStrength']),
                    'Intellect': int(row['Intellect']),
                    'Dignity': int(row['Dignity']),
                    'Tenacity': int(row['Tenacity']),
                    'Attractiveness': int(row['Attractiveness']),
                    'Morality': int(row['Morality'])
                }
                current_scene = int(row['current_scene']) if 'current_scene' in row and not pd.isna(row['current_scene']) else 1
                user = Login(
                    str(row['my_id']),
                    str(row['my_name']),
                    str(row['daughter_name']),
                    str(row['password']),
                    stats,
                    current_scene
                )
                user_list.append(user)
            return user_list
        except Exception:
            df = pd.DataFrame(columns=self.headers)
            df.to_csv(self.file_name, index=False, encoding="utf-8")
            return user_list

repo = Repository()