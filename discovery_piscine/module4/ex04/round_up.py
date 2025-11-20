#!/usr/bin/env python3
import math

arg = input("Give me a number: ")
try:
    number = float(arg)
except:
    print("Invalid input")
    exit(1)

number_rounded_up = math.ceil(number)
print(str(number_rounded_up))

