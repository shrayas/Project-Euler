'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
'''

import math
import sys

def isPrime(num,previousPrimes):

    isPrimeFlag = True

    if len(previousPrimes) == 0:
        return isPrimeFlag

    for previousPrime in previousPrimes:
        if num % previousPrime == 0:
            isPrimeFlag = False
            break

    return isPrimeFlag

primeToFind = int(sys.argv[1])
primesTillNow = []

i = 2
while True:
    isPrimeFlag = isPrime(i,primesTillNow)

    if isPrimeFlag == True:
        primesTillNow.append(i)

    if len(primesTillNow) != primeToFind:
        i = i+1
    else:
        break

print primesTillNow[-1]
print len(primesTillNow)
