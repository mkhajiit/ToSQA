dan = int(input("구구단을 출력할 숫자를 입력하세요: "))

def gugudan(dan):
  for i in range(1,10):
    print(f"{dan} x {i} = {dan * i}")

gugudan(dan)