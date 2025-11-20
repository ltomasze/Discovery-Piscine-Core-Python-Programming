#!/usr/bin/env python3

def array_of_names(persons):
    array_for_names = []
    for first_name, last_name in persons.items():
        array_for_names.append(first_name.capitalize() + " " + last_name.capitalize())
    return array_for_names

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))