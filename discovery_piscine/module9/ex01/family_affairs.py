#!/usr/bin/env python3

#def find_the_redheads(dupont_family):
#    array_for_red = []
#    for name, color in dupont_family.items():
#        if color == "red":
#            array_for_red.append(name)
#    return list(array_for_red)

def value_is_red(key_value):
    return key_value[1] == "red"
    
def find_the_redheads(dupont_family):
    list_for_red = []
    for name, color in filter(value_is_red, dupont_family.items()):
        list_for_red.append(name)
    list(list_for_red)
    return list_for_red

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))