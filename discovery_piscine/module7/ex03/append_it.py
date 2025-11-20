#!/usr/bin/env python3

#import sys
#
#if len(sys.argv) == 1:
#    print("none")
#    exit(1)
#
#for arg in sys.argv[1:]:
#    if arg.endswith("ism"):
#        continue
#    else:
#        print(arg + "ism")

import sys

if len(sys.argv) == 1:
    print("none")
    exit(1)

for arg in sys.argv[1:]:
    start = len(arg) - 3
    if len(arg) < 3:
        print(arg + "ism")
    elif arg.find("ism", start) == len(arg) - 3:
        continue
    else:
        print(arg + "ism")
