def gugudan(dan):
  for i in range(1,10):
    print(f"{dan} x {i} = {dan * i}")


try:
  dan = int(input("구구단을 출력할 숫자를 입력하세요: "))
  if dan < 1 or dan > 9:
    raise ValueError("1부터 9 사이의 정수를 입력해야 합니다.") # 명시적으로 ValueError 를 발생시킵니다.
  gugudan(dan)

except ValueError as e:
  print("입력 오류:",e)