from phone_info import PhoneInfo

def main():
  person1 = PhoneInfo('kim', '010-1234-1234', '2000-01-01', 'seoul')
  person2 = PhoneInfo('kim', '010-1234-1234', '2000-01-01')
  person3 = PhoneInfo('kim', '010-1234-1234')

  person1.print_info()
  person2.print_info()
  person3.print_info()

if __name__ == '__main__':
  main()