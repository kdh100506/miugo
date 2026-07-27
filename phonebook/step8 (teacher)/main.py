#from phonebook_service import PhoneBookService
from services.phonebook_service import instance as service
#from services.phonebook_service import instance as service2
from services.phone_book_analyzer import PhoneBookAnalyzer

def show_menu():
    print("선택하세요...")
    print("1. 데이터 입력")
    print("2. 데이터 검색")
    print("3. 데이터 수정")
    print("4. 데이터 삭제")
    print("5. 전체 출력")
    print("6. 데이터 저장")
    print("7. 데이터 분석")
    print("0. 프로그램 종료")

def main():
    
    analyzer = PhoneBookAnalyzer("/Users/dgsw12/Desktop/미유고/PhoneBook/step08/data/phone_book.csv") 

    while True:
        show_menu()
        try:
            choice = int(input("선택: "))       

            print() # 가독성을 위한 빈 줄
            
            if choice == 1:
                service.input_data()
            elif choice == 2:
                #service2.search_data()
                service.search_data()
            elif choice == 3:
                service.update_data()
            elif choice == 4:
                service.delete_data()
            elif choice == 5:
                service.show_all_data()
            elif choice == 6:
                service.backup_data()
            elif choice == 7:  # 👈 3. 7번 데이터 분석 메뉴 분기 추가
                print("--- 📊 데이터 분석 메뉴 ---")
                print("1) 인맥 그룹 비율 (원형 차트)")
                print("2) 거주 지역 분포 (막대 차트)")
                sub_choice = int(input("원하는 분석을 선택하세요: "))
                
                if sub_choice == 1:
                    analyzer.visualize_group_ratio()
                elif sub_choice == 2:
                    analyzer.visualize_region_distribution()
                else:
                    print("잘못된 선택입니다. 메인 메뉴로 돌아갑니다.\n")
                               
            elif choice == 0:
                print("프로그램을 종료합니다.")
                service.backup_data()  
                break
            else:
                print("잘못된 입력입니다. 다시 선택해주세요.\n")
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.\n")
            continue

if __name__ == "__main__":   
    main()
