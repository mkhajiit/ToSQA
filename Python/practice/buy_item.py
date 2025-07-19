class buy_item:
  def __init__(self,fruit, balance):
    self.fruit = fruit
    self.balance = balance
  
  def print_input(self):
    print(f"입력한 과일명은 {self.fruit}입니다.")
    print(f"입력한 보유금액은 {self.balance}입니다.")


fruit = input("과일 이름을 입력하세요(포도,사과,키위): ")
balance = input("보유할 금액을 입력하세요: ")

status = buy_item(fruit,balance)

status.print_input()