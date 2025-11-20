#!/usr/bin/env python3
arg = input()

try:
    number = float(arg)
except:
    print("Invalid input.")
    exit(1)

if number < 0:
    print("This number is negative.")
elif number > 0:
    print("This number is positive.")
else:
    print("This number is both positive and negative.")