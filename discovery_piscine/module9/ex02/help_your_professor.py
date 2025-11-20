#!/usr/bin/env python3

def average(class_3):
    array_for_scores = []
    for element in class_3.values():
        array_for_scores.append(element)
    count_elements = len(array_for_scores)
    total = sum(array_for_scores)
    result = total / count_elements
    return result


class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}
class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")