class PhoneInfo:
  def __init__(self, name, phone_number, birth = None, region = None):
    self.name = name
    self.phone_number = phone_number
    self.birth = birth
    self.region = region

  def print_info(self):
    if bool(self.birth) == True and bool(self.region) == True:
      print(f'이름 : {self.name}, 전화번호 : {self.phone_number}, 생일 : {self.birth}, 지역 : {self.region}')
    elif bool(self.birth) == True and bool(self.region) == False:
      print(f'이름 : {self.name}, 전화번호 : {self.phone_number}, 생일 : {self.birth}')
    elif bool(self.birth) == False and bool(self.region) == True:
      print(f'이름 : {self.name}, 전화번호 : {self.phone_number}, 지역 : {self.region}')
    else:
      print(f'이름 : {self.name}, 전화번호 : {self.phone_number}')

class PhoneUnivInfo(PhoneInfo):
  def __init__(self, name, phone_number, major, birth=None, region=None):
    super().__init__(name, phone_number, birth, region)
    self.major = major
  
  def print_info(self):
    if bool(self.birth) == True and bool(self.region) == True:
      print(f'이름 : {self.name}, 전화번호 : {self.phone_number}, 학과 : {self.major}, 생일 : {self.birth}, 지역 : {self.region}')
    elif bool(self.birth) == True and bool(self.region) == False:
      print(f'이름 : {self.name}, 전화번호 : {self.phone_number}, 학과 : {self.major}, 생일 : {self.birth}')
    elif bool(self.birth) == False and bool(self.region) == True:
      print(f'이름 : {self.name}, 전화번호 : {self.phone_number}, 학과 : {self.major}, 지역 : {self.region}')
    else:
      print(f'이름 : {self.name}, 전화번호 : {self.phone_number}, 학과 : {self.major}')

class PhoneCompanyInfo(PhoneInfo):
  def __init__(self, name, phone_number, company, birth=None, region=None):
    super().__init__(name, phone_number, birth, region)
    self.company = company
  
  def print_info(self):
    if bool(self.birth) == True and bool(self.region) == True:
      print(f'이름 : {self.name}, 전화번호 : {self.phone_number}, 회사 : {self.company}, 생일 : {self.birth}, 지역 : {self.region}')
    elif bool(self.birth) == True and bool(self.region) == False:
      print(f'이름 : {self.name}, 전화번호 : {self.phone_number}, 회사 : {self.company}, 생일 : {self.birth}')
    elif bool(self.birth) == False and bool(self.region) == True:
      print(f'이름 : {self.name}, 전화번호 : {self.phone_number}, 회사 : {self.company}, 지역 : {self.region}')
    else:
      print(f'이름 : {self.name}, 전화번호 : {self.phone_number}, 회사 : {self.company}')