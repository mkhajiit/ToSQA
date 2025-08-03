class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def say_hello(self):
    print(f"안녕하세요, 저는 {self.name}입니다. 저는 {self.age}살 입니다.")

class Dog:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  
  def say_hello(self):
    print(f"안녕 내 이름은 {self.name}입니다. 저는 {self.age}살 입니다.")

p1 = Person("지훈",25)
p2 = Person("주호",30)
d1 = Dog("백구",3)
d2 = Dog("하니", 6)

p1.say_hello()
p2.say_hello()
d1.say_hello()
d2.say_hello()