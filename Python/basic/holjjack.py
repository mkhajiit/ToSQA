input = int(input("정수를 입력하세요: "))

def holjjack_reader(input):
  if(input % 2 == 0):
    print(f"{input} 은 짝수입니다")
  elif(input % 2 == 1):
    print(f"{input} 은 홀수입니다")

holjjack_reader(input)