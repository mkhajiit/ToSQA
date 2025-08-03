phone_book = {}

while True:
  menu = input("1. 저장 | 2. 검색 | 3. 삭제 | 4. 종료\n메뉴를 선택하세요: ")

  if menu == "1":
    name = input("이름을 입력하세요: ") # 키
    number = input("전화번호를 입력하세요: ") # 값
    phone_book[name] = number
    print(f"{name}의 번호가 저장되었습니다.")
  
  elif menu == "2":
    name = input("검색할 이름을 입력하세요: ")
    if name in phone_book:
      print(f"{name}의 번호는 {phone_book[name]}입니다.")
    else:
      print(f"{name}은 전화번호부에 저장되어 있지 않습니다.")
  
  elif menu == "3":
    name = input("삭제할 이름을 입력하세요: ")
    if name in phone_book:
      del phone_book[name] # del 키-값 쌍 전체가 삭제됨
      print(f"{name}의 번호가 삭제 되었습니다.")
    else:
      print(f"{name}은 전화번호부에 저장되어 있지 않습니다.")
  
  elif menu == "4":
    print("프로그램을 종료합니다!")
    break

  else:
    print("잘못된 입력입니다 다시 선택해주세요")