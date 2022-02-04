#To calculate the first triangle number with 500 hundred or more divisors, we first need a function to calculate triangle numbers
#Then, a function to determine all the divisors of a number is needed
#To determine all the divisors of a number n, we can check by brute force whether or not each integer i up to the square root of the number divides evenly
#If the number divides evenly by i, we know that i and n / i are divisors 
#Then, we generate triangular numbers and check each one's divisor until there are over 500 hundred divisors
#This code can definitely be optimized but it works for this problem

import Problem3

def triangleNumber(n):
    """
    Generates the nth triangular number
    For example, with n = 3, this will return 6 (= 1 + 2 + 3)
    """
    res = 0
    for i in range(1, n+1):
        res += i
    return res

def generateDivisors(n):
    """
    Takes a number n and returns all of the divisors of n
    Determines the divisors by brute force division from 1 to n**0.5+1, taking advantage of the fact that divisors come in pairs
    For example, with n = 6, this will return 1, 2, 3, 6 as a list"""
    res = []
    for i in range(1, int(n**0.5+1)):
        if n % i == 0:
            res.append(i)
            #While not necessary to convert n/i to an int, it seems like a good decision if this function is needed in the future
            res.append(int(n/i))
    return res

if __name__ == '__main__':
    counter = 1
    factors = []
    while len(factors) < 500:
        counter+=1
        factors = generateDivisors(triangleNumber(counter))
    print(triangleNumber(counter))