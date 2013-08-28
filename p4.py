'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

largest=0
largestI=0
largestJ=0

iterationCount=0

for i in reversed(range(100,1000)):

    j = 990

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

        j = j - 11

print largest
print str(largestI) + " X " + str(largestJ)
print iterationCount
