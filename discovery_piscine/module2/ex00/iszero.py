#!/usr/bin/env python3
arg = input()

try:
    number = float(arg)
except:
    print("Invalid input.")
    exit(1)

if number == 0:
    print("This number is equal to zero.")
else:
    print("This number is different from zero.")