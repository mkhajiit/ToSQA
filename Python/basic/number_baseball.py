import random

number = random.randint(1,10) # 1이상 10이하의 정수

try:
  while True:
    answer = int(input("정답을 입력하세요(1이상 10이하): "))
    if answer > 10 or answer < 1:
      raise ValueError("1부터 10이하의 정수를 입력해야 합니다.")
    
    if answer == number:
      print("정답입니다!")
      break
    elif answer > number:
      print("더 작은 숫자입니다.")
    elif answer < number:
      print("더 큰 숫자 입니다")

except ValueError as e:
  print("입력 오류:",e)