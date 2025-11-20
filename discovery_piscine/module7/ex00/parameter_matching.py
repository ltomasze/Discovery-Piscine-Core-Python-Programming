#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
    exit(1)
parameter = input("What was the parameter? ")
if (sys.argv[1] == parameter):
    print("Good job!")
else:
    print("Nope, sorry...")


