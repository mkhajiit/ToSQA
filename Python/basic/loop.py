import random

def random_star():
  random_count = random.randint(1,10) # 1~10 사이의 정수 난수생성
  stars = ""
  for i in range(random_count):
    stars += "*"

  print(stars)

random_star()