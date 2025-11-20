#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print("none")
    exit(1)

print("parameters: " + str(len(sys.argv) - 1))
for arg in sys.argv[1:]:
    print (arg + ": " + str(len(arg)))
