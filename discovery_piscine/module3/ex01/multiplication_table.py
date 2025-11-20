#!/usr/bin/env python3

arg = input("Enter a number\n")

try:
    number = int(arg)
except:
    print("Invalid input")
    exit(1)

i = 0
while i < 10:
    print(str(i) + " x " + str(number) + " = " + str(number * i))
    i += 1