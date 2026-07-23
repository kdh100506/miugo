import csv
import os
from phonebook_service import PhoneInfo, PhoneUnivInfo, PhoneCompanyInfo

class PhoneRepository:
  def __init__(self, file_name):
    self.file_name = file_name

  def save(self, data_list):
    with open(self.file_name, 'w', encoding='utf-8', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(['name','phone','birth','region','group','memo'])
    
      for info in data_list:
        if isinstance(info, PhoneUnivInfo):
          group = '대학'
          memo = info.major
        elif isinstance(info, PhoneCompanyInfo):
          group = '회사'
          memo = info.company
        else:
          group = '일반'
          memo = ''
        
        writer.writerow([info.name, info.phone_number, info.birth, info.region, group, memo])
    print('[시스템] 파일 저장 완료')

  def load(self):
    loaded_data = []
    if not os.path.exists(self.file_name):
      return loaded_data
    
    with open(self.file_name, 'r', encoding='utf-8') as file:
      reader = csv.reader(file)
      next(reader)
      for row in reader:
        name, num, birth, region, group, memo = row
        birth = birth if birth != '' else None
        region = region if region != '' else None
        if group == '대학':
          info = PhoneUnivInfo(name, num, major=memo, birth=birth, region=region)
        elif group == '회사':
          info = PhoneCompanyInfo(name, num, company=memo, birth=birth, region=region)
        else:
          info = PhoneInfo(name, num, birth=birth, region=region)
        
        loaded_data.append(info)
    print('[시스템] 파일 로드 완료')
    