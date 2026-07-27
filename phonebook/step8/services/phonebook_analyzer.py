import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

class PhoneBookAnalyzer:
    def __init__(self, file_name="/Users/dgsw12/Desktop/미유고/PhoneBook/step8/data/phone_book.csv"):
        self.file_name = file_name
        plt.rcParams['font.family'] = 'AppleGothic'
        plt.rcParams['axes.unicode_minus'] = False

    def load_dataframe(self):
        if not os.path.exists(self.file_name):
            print('분석할 데이터 파일이 존재하지 않습니다.')
            return None
        return pd.read_csv(self.file_name, encoding='utf-8')

    def visualize_group_ratio(self):
        df = self.load_dataframe()
        if df is None or df.empty: 
            return
        
        group_counts = df['group'].value_counts()
        plt.figure(figsize=(6, 6))
        plt.pie(group_counts, labels=group_counts.index, autopct='%1.1f%%')
        plt.title('내 인맥 그룹별 비율', fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()

    def visualize_region_distribution(self):
        df = self.load_dataframe()
        if df is None or df.empty: 
            return
            
        region_data = df['region'].dropna()
        region_data = region_data[region_data != ""]
        if region_data.empty:
            print('등록된 지역 데이터가 없습니다.')
            return
            
        region_counts = region_data.value_counts()
        
        plt.figure(figsize=(10, 5))
        sns.barplot(x=region_counts.index, y=region_counts.values, palette='viridis')
        # sns.barplot(x=region_counts.index, y=region_counts.values, palette='viridis', hue=region_counts.index, legend=False)
        plt.title('지역별 인맥 분포', fontsize=14, fontweight='bold')
        plt.xlabel('지역', fontsize=12)
        plt.ylabel('인원수', fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()