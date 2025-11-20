#!/usr/bin/env python3
arg1 = input("Enter the first number:\n")
arg2 = input("Enter the second number:\n")

try:
    number1 = int(arg1)
except:
    print("Invalid first argument")
    exit(1)

try:
    number2 = int(arg2)
except:
    print("Invalid second argument")
    exit(1)

result = number1 * number2
print(str(number1) + " x " + str(number2) + " = " + str(result))
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")

