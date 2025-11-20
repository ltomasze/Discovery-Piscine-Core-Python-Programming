#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print("none")
    exit(1)

def shrink(parameter):
    print(parameter[0:8])

def enlarge(parameter):
    difference = 8 - len(parameter)
    print(parameter, end="")
    print("Z" * difference)

for arg in sys.argv[1: ]:
    if len(arg) > 8:
        shrink(arg)
    elif len(arg) < 8:
        enlarge(arg)
    else:
        print(arg)