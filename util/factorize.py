#!/usr/bin/python

import sys

print sys.argv[1]

num = int(sys.argv[1])

for i in range(2,num/2):
    if (num%i == 0):
        print i
