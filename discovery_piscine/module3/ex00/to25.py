#!/usr/bin/env python3

arg = input("Enter a number less than 25\n")

try:
    number = int(arg)
except:
    print("Invalid input")
    exit(1)

if(number < 25):
    while number <= 25:
        print("Inside the loop, my variable is " + str(number))
        number += 1
        
else:
    print("Error")
