from phone_info import PhoneInfo
from phonebook_service import PhoneBookService

# 싱글톤
# from phonebook_service import PhoneBookService as ins
# from phonebook_service import PhoneBookService as ins2

def menu():
  print('1. 데이터 입력')
  print('2. 검색')
  print('3. 삭제')
  print('4. 수정')
  print('5. 전체 출력')
  print('0. 프로그램 종료')

def main():
  ins = PhoneBookService()
  # service2 = PhoneBookService()
  while True:
    menu()
    try:
      menu_info = int(input('메뉴 선택 : '))
      if menu_info == 0:
        print('프로그램 종료')
        break
      elif menu_info == 1:
        ins.read_data()
      elif menu_info == 2:
        ins.search()
      elif menu_info == 3:
        ins.remove()
      elif menu_info == 4:
        ins.edit()
      elif menu_info == 5:
        ins.show()
    except ValueError:
          print('입력값이 올바르지 않습니다.')
          continue

if __name__ == '__main__':
  main()