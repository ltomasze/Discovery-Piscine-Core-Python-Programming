#!/usr/bin/env python3
j = 0
while j < 11:
    print("Table of " + str(j) + ":", end=" ")
    i = 0
    while i < 11:
        print(str(j * i), end=" ")
        i += 1
    j += 1
    print()