fruits = ["apple","grape","kiwi","strawberry"]
number = [1,2,3,4,5]

def print_list(list):
  for element in list:
    print(element)
  
print_list(fruits)
print_list(number)

fruits.append("melon")
fruits.remove("apple")

print_list(fruits)