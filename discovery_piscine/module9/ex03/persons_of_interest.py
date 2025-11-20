#!/usr/bin/env python3

def get_birth_date(item):
     return item[1]['date_of_birth']

def famous_births(persons):
    for big_key, big_value in sorted(persons.items(), key=get_birth_date):
        name = big_value['name']
        date = big_value['date_of_birth']
        print(str(name) + " is a great scientist born in " + str(date) + ".")

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)