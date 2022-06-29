from math import *

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter the operator: ")

if(operation == "+"):
    print(num1 + num2)
elif(operation == "-"):
    print(num1 - num2)
elif(operation == "*"):
    print(num1 * num2)
elif(operation == "/"):
    print(num1/num2)
else:
    print("error")
