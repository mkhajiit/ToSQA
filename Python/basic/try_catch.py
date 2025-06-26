try:
  for i in range(3):
    a = int(input("숫자 입력:"))
    print (10 / a)
# 숫자를 0으로 나눌경우 예외처리
except ZeroDivisionError:
  print("0으로 나눌 수 없습니다.")

try:
  for i in range(2):
    a = int(input("숫자 입력:"))
    print (10 / a)
except ValueError:
  print("숫자만 입력해야 합니다.")