import basic_export
try:
  number = int(input("숫자 입력:"))
  acc = 1
  if 100 >= number >= 10:
    print(f"결과 값: {number - 10}")
  elif number < 10:
    for i in range(3):
      acc *= number
    print(f"결과 값: {acc}")
  elif number > 100:
    basic_export.error_message()
except ValueError:
  print("숫자를 입력해주세요!!!")