#!/usr/bin/env python3

def add_one(parameter):
    plus_one = parameter + 1
    return plus_one

number = 0
print("before use add one: number = " + str(number))
print("when we use method add_one for number: number =", end=" ")
print(add_one(number))
print("number is the same as before: number = " + str(number))
