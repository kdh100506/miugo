from phone_info import PhoneInfo
from phone_info import PhoneUnivInfo
from phone_info import PhoneCompanyInfo

class PhoneBookService:
  def __init__(self):
    self.phonebook = []

  def read_data(self):
    print('1.일반, 2.대학, 3.회사')
    choice = int(input())
    if choice == 1:
      name = input('이름 : ')
      phone_number = input('전화번호 : ')
      birth = input('생일 : ')
      region = input('지역 : ')
      ins = PhoneInfo(name, phone_number, birth, region)
      info = {'이름':name, '전화번호':phone_number, '생일':birth, '지역':region}
    
    elif choice == 2:
      name = input('이름 : ')
      phone_number = input('전화번호 : ')
      major = input('학과 : ')
      birth = input('생일 : ')
      region = input('지역 : ')
      ins = PhoneUnivInfo(name, phone_number, major, birth, region)
      info = {'이름':name, '전화번호':phone_number, '학과':major, '생일':birth, '지역':region}
    
    elif choice == 3:
      name = input('이름 : ')
      phone_number = input('전화번호 : ')
      company = input('회사 : ')
      birth = input('생일 : ')
      region = input('지역 : ')
      ins = PhoneCompanyInfo(name, phone_number, company, birth, region)
      info = {'이름':name, '전화번호':phone_number, '회사':company, '생일':birth, '지역':region}
    
    else:
      print('잘못 입력하셨습니다.')
      return
    ins.print_info()
    self.phonebook.append(info)
    print('저장완료')

  def search(self):
    search_input = input('이름을 검색하세요 : ')
    for i in self.phonebook:
      if search_input in i.values():
        print(i)
        return
    print('검색결과가 없습니다.')

  def remove(self):
    remove_input = input('삭제할 대상을 입력하세요 : ')
    for i in self.phonebook:
      if remove_input in i.values():
        self.phonebook.remove(i)
        print('삭제 되었습니다.')
        return
    print('삭제할 대상이 없습니다.')

  def edit(self):
    edit_input = input('수정할 대상을 입력하세요 : ')
    for i in self.phonebook:
      if edit_input in i.values():
        for j in i.keys():
          if j == '이름':
            continue
          edit_ing = input(f'{j} 수정하기 : ')
          i[j] = edit_ing
        print('수정이 완료 되었습니다.')
        return
    print('수정할 대상이 없습니다.')

  def show(self):
    print(self.phonebook)