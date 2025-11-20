#!/usr/bin/env python3

arg = input("Please tell me your age: ")

try:
    number = int(arg)
except:
    print("Invalid input")
    exit(1)

print("You are currently " + arg + " years old.")
print("In 10 years, you'll be " + str(number + 10) + " years old.")
print("In 20 years, you'll be " + str(number + 20) + " years old.")
print("In 30 years, you'll be " + str(number + 30) + " years old.")