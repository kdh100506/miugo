from phone_info import PhoneInfo

def menu():
  print('1. 데이터 입력')
  print('0. 프로그램 종료')

def read_data():
  name = input('이름 : ')
  phone_number = input('전화번호 : ')
  birth = input('생일 : ')
  region = input('지역 : ')
  ins = PhoneInfo(name, phone_number, birth, region)
  ins.print_info()


def main():
  while True:
    menu()
    menu_info = int(input('메뉴 선택 : '))
    if menu_info == 0:
      print('프로그램 종료')
      break
    read_data()

if __name__ == '__main__':
  main()