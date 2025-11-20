#!/usr/bin/env python3

def greetings(name=None):
    if name is None:
        print("Hello, noble stranger.")
    elif not isinstance(name, str ):
        print("Error! It was not a name.")
    else:
        print("Hello, " + name + ".")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)