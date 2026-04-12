
# Day 11: Binary Numbers
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
    binary = bin(n)[2:]
    ones=binary.split('0') # only group of 1 
    max_count=0# find max length
    for i in ones:
        if len(i)> max_count:
            max_count=len(i)
    print(max_count)