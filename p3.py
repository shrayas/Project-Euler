'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
'''

import sys
from util import factorize

def findLargestPrime(num):

    factor = factorize.pollandroh(num)

    if (factor == num):
        return num
    else:
        return findLargestPrime(num/factor)

if __name__ == "__main__":
    num = int(sys.argv[1])

    print findLargestPrime(num)
