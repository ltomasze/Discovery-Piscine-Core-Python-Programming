#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []

print("Original array: " + str(original_array))

for element in original_array:
    new_array.append(element + 2)

print("New array: " + str(new_array))