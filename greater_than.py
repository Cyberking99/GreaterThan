#  Title: Number Comparison (LTC Hackathon)
#  Description: A program that outputs the maximum of two numbers.
#  Author: Kefas Kingsley (KC)
#  Date: 13/05/2020
  
#Take the first number from the user
num1 = int(input("First number:\n>>"))

#Take the second number from the user
num2 = int(input("Second number:\n>>"))

#Compare the two numbers
if num1 < num2:
  print(num2)
elif num1 > num2:
  print(num1)
elif num1 == num2:
  print("The numbers are the same")
else:
  print("There is an error!")