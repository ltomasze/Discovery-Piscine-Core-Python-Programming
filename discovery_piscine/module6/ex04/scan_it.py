#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    result = re.findall(sys.argv[1], sys.argv[2])
    count_word = len(result)
    if count_word == 0:
        print("none")
    else:
        print(count_word)

    
    