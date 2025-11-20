#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []
new_set = set()

print(str(original_array))

for element in original_array:
    if element > 5:
        new_set.add(element + 2)

#new_array.extend(new_set)
#new_array.sort()
#print(new_array)
#print("{" + ", ".join(str(x) for x in new_array) + "}")
print(new_set)
#list1 =list(new_set)
#list1.sort()
#print(list1)

