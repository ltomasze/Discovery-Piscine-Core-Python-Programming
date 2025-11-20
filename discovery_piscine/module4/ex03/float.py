#!/usr/bin/env python3

#arg = input("Give me a number: ")

#try:
#    number = float(arg)
#except:
#    print("This is not a number")
#    exit(1)
#
#try:
#    number = int(arg)
#    print("This number is an integer.")
#except:
#    print("This number is an decimal.")


arg = input("Give me a number: ")

try:
    number = float(arg)
except ValueError:
    print("This is not a number")
    exit(1)

if number.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")