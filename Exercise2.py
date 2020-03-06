import random
def random_number():
    num1 = input("Enter number from 1 to 10 ")
    if num1 in range(10):
     print(num1)
    else:
      print("Number should be between 0 to 10 ")
      print(input("Enter number from 1 to 10 "))

random_number()



