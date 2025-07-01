class BankAccount:
  def __init__(self,owner):
    self.owner = owner
    self.balance = 0

  def deposit(self, amount):
    self.balance += amount
    print(f"{amount}원이 입금되어 잔고는{self.balance}원이 되었습니다.")

  def withdraw(self, amount):
    if amount > self.balance:
      print("잔액이 부족합니다!")
    else:
      self.balance -= amount
      print(f"{amount}원이 출금되어 잔고는{self.balance}원이 되었습니다.")

account = BankAccount("홍길동")
account.deposit(40000)
account.withdraw(40010)
account.withdraw(30000)