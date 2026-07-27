import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

class PhoneBookAnalyzer:
    def __init__(self, file_name="step08/data/phone_book.csv"):
        self.file_name = file_name
        
        # matplotlib 한글 깨짐 방지 설정 (Windows: Malgun Gothic, Mac: AppleGothic)
        plt.rcParams['font.family'] = 'AppleGothic' 
        plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지

    def load_dataframe(self):
        """데이터 load"""
        if not os.path.exists(self.file_name):
            print("분석할 데이터 파일이 존재하지 않습니다.")
            return None
        return pd.read_csv(self.file_name, encoding="utf-8")

    def visualize_group_ratio(self):
        """1. 그룹별(일반/대학/회사) 인맥 비율 시각화 (Pie Chart)"""
        df = self.load_dataframe()
        if df is None or df.empty: return       # 정상로드 X, 내용이 없으면 함수종료

        # 그룹별 데이터 개수 집계
        
        group_counts = df['group'].value_counts()

        plt.figure(figsize=(6, 6))  # 도화지 준비
        # 파이 차트 그리기
        plt.pie(group_counts, labels=group_counts.index, autopct='%1.1f%%', 
                startangle=140, colors=sns.color_palette('pastel'))
        plt.title('내 인맥 그룹별 비율', fontsize=14, fontweight='bold')
        plt.tight_layout()          # 여백조절 
        plt.show()                  # 파이 차트 창을 띄워줌

    def visualize_region_distribution(self):
        """2. 지역별 인원 분포 시각화 (Bar Chart)"""
        df = self.load_dataframe()
        if df is None or df.empty: return

        # 결측치(None) 제거 및 빈 문자열 제외 후 집계
        region_data = df['region'].dropna()
        region_data = region_data[region_data != ""]
        
        if region_data.empty:
            print("등록된 지역 데이터가 없습니다.")
            return

        region_counts = region_data.value_counts()

        plt.figure(figsize=(10, 5))
        # 막대 그래프 그리기
        sns.barplot(x=region_counts.index, y=region_counts.values, palette='viridis')
        plt.title('지역별 인원 분포', fontsize=14, fontweight='bold')
        plt.xlabel('지역')
        plt.ylabel('인원 수 (명)')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()