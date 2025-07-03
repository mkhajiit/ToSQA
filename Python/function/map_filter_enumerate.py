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

# enumerate 주어진