class buy_item:
  def __init__(self,fruit, balance):
    self.fruit = fruit
    self.balance = balance
  
  def print_input(self):
    print(f"입력한 과일명은 {self.fruit}입니다.")
    print(f"입력한 보유금액은 {self.balance}입니다.")

while True:
  fruit = input("과일 이름을 입력하세요(포도,사과,키위,딸기): ")
  balance = int(input("보유할 금액을 입력하세요: "))
  status = buy_item(fruit,balance)

  if fruit in ["포도","사과","키위","딸기"] and balance > 0:
    status.print_input()
  else:
    print("잘못된 입력 입니다!")
    break