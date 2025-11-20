#!/usr/bin/env python3

arg1 = input("Give me the first number: ")
try:
    number1 = int(arg1)
except:
    print("Invalid first input")
    exit(1)

arg2 = input("Give me the second number: ")
try:
    number2 = int(arg2)
except:
    print("Invalid second input")
    exit(1)

print("Thank you!")
print(arg1 + " + " + arg2 + " = " + str(number1 + number2))
print(arg1 + " - " + arg2 + " = " + str(number1 - number2))
try:
    print(arg1 + " / " + arg2 + " = " + str(int(number1 / number2)))
except ZeroDivisionError:
    print("cannot be divided by 0")
print(arg1 + " * " + arg2 + " = " + str(number1 * number2))


