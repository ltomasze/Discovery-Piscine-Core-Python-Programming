#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("none")
    exit(1)

try:
    first_num = int(sys.argv[1])
    second_num = int(sys.argv[2])
except:
    print("Invalid input.")
    exit(1)

if first_num >= second_num:
    print("Error: the first parameter is equal to or greater than the second")
    exit(1)

array_i = []
for i in range(first_num, (second_num + 1)):
    array_i.append(i)
print(array_i)
    