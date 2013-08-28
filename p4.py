'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

largest=0
largestI=0
largestJ=0

iterationCount=0

i = 999
while i >= 100:

    if i%11 == 0:
        j=999
        dj=1
        di=11
    else:
        j=990
        dj=11
        di=1

    if i < j:
        break;

    while j >= 100:

        iterationCount = iterationCount + 1

        num = i*j

        if str(num) == str(num)[::-1]:
            if num > largest:
                largest = num
                largestI = i
                largestJ = j

        j = j - dj

    i = i - di

print largest
print str(largestI) + " X " + str(largestJ)
print iterationCount
