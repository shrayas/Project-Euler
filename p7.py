'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
'''

import math
import sys

def isPrime(num):
    if num == 1:
        return False
    elif num < 4:
        return True
    elif num % 2 == 0:
        return False
    elif num < 9:
        return True
    elif num % 3 == 0:
        return False
    else:
        
        r = math.floor(math.sqrt(num))
        f = 5

        while f <= r:
            if num % f == 0:
                return False
            if num % (f+2) == 0:
                return False
            f = f+6

        return True

limit=10001
count=1
candidate=1

while count != limit:
    candidate = candidate + 2
    if isPrime(candidate):
        count = count+1

print candidate
