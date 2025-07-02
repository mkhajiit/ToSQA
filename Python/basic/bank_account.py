class BankAccount:
  def __init__(self,owner):
    self.owner = owner
    self.balance = 0

  def deposit(self, amount):
    print(f"어서 오십시오 {self.owner}님")
    self.balance += amount
    print(f"{amount}원이 입금되어 잔고는{self.balance}원이 되었습니다.")

  def withdraw(self, amount):
    print(f"어서 오십시오 {self.owner}님")
    if amount > self.balance:
      print("잔액이 부족합니다!")
    else:
      self.balance -= amount
      print(f"{amount}원이 출금되어 잔고는{self.balance}원이 되었습니다.")

name = input("예금주 이름을 입력하십시오: ")
account = BankAccount(name)

while True:
  action = input("무엇을 하시겠습니까? (입금, 출금, 종료):")

  if action == "입금":
    amount = int(input("입금할 금액을 입력하세요: "))
    account.deposit(amount)

  elif action == "출금":
    amount = int(input("출금할 금액을 입력하세요: "))
    account.withdraw(amount)
  
  elif action == "종료":
    print("거래를 종료합니다")
    break

  else:
    print("잘못된 입력입니다. 다시 시도해주세요.")