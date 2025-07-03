# map 주어진 리스트의 요소를 두배곱한 리스트 제곱한 리스트 만들기
r = range(5) # 0 ~ 4
print(list(r))

numbers = [1,2,3,4,5,6]

doubles = list(map(lambda x: x*2,numbers)) # lambda x: x*2 == def doubles x return x*2
squares = list(map(lambda x: x**2,numbers))

print(doubles)
print(squares)

# filter 주어진 문자열에서 대문자만 필터링 해보기
text = "Python Filter Test"

upper_cases = list(filter(str.isupper,text))

print(upper_cases)

# enumerate()는 반복 가능한 객체(iterable)를 순회할 때,
# 값 뿐 아니라 인덱스도 같이 얻을 수 있게 해주는 내장 함수
# enumerate(iterable, start=0) start의 기본값은 0

fruits = ["grape","banana","apple","strawberry","kiwi"]
for i, fruit in enumerate(fruits, start=1):
  print(f"인덱스 {i}번째 과일 {fruit}")

# 보너스 zip
# 여러 리스트를 병렬로 묶기
# 인덱스가 같은 요소끼리 튜플로 묶인다
names = ["철수", "영희", "민수"]
scores = [90, 85, 78]

home_lists = list(zip(names,scores))

print(home_lists)