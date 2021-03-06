'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''


def check(num):
    if (num%2 == 0):
        return num
    else:
        return 0

def fib(num1,num2):

    END_POINT=4000000

    num3=num1+num2

    print "Checking " + str(num3)
    if (num3 < END_POINT):
        add = check(num3)

        print "Adding "+str(add)+" to sum, recursing into ("+str(num2)+","+str(num3)+")"
        return add + fib(num2,num3)
    else:
        print "over"
        return 0


def main():

    START_NUM1=0
    START_NUM2=1

    sum=0
    sum = sum + fib(START_NUM1,START_NUM2)

    print sum

if __name__ == "__main__":
    main()
