#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []

print(str(original_array))

for element in original_array:
    if element > 5:
        new_array.append(element + 2)

print(str(new_array))