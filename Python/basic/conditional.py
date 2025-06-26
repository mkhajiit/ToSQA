def calculation_box(number, refer):
  if number > refer:
    print(f"출력값: {number + refer}")
  elif number <= refer:
    print(f"출력값: {refer - number}")


calculation_box(20,10)
calculation_box(9,10)