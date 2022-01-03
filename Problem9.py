#First, a function is needed to determine whether or not a number n is a perfect square
#Then, you can increment a and b and then sum their squares
#If a**2 + b**2 is a perfect square, then a, b, and (a**2 + b**2)**0.5 (which is equal to c) is a Pythagorean triplet
#Then, we can add a, b, and c to check if they sum to 1000
#If so, we calculate a * b * c and that number is the answer
#This code is definitey not efficient; it has the same issue as problem 4 with double checking a bunch of numbers
#Also, there is the possibility of the ranges not being large enough
#However, for now, this works but can definitely be improved upon

def isSquare(n):
    """
    Takes a number and returns true if it is a perfect square, false otherwise
    By converting n**0.5 to an integer, we can truncate the decimal if there is one
    If there is no decimal to truncate, the truncated int squared will be exactly equal to n
    And we do not need to worry about comparing an int vs a float because of how Python runs type comparison
    """
    return int(n**0.5)**2 == n

for a in range(1, 1000):
    for b in range(1, 1000):
        sumOfSquares = a**2 + b**2
        if isSquare(sumOfSquares):
            c = sumOfSquares**0.5
            if a + b + c == 1000:
                print(a * b * c)

