#!/usr/bin/python

import sys
import random
import fractions

def factorize(num):
    for i in range(2,num/2):
        if (num%i == 0):
            print i

def pollandsRho(num):
    if num%2 == 0:
        return 2

    x = random.randint(1, num-1)
    y = x

    c = random.randint(1, num-1)

    g = 1

    while g == 1:
        x = ((x*x)%num + c) % num
        y = ((y*y)%num + c) % num
        y = ((y*y)%num + c) % num
        g = fractions.gcd(abs(x-y),num)
    return g
