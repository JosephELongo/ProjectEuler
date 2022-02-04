#First, define a function that generates the collatz sequence and stores the values reached
#Then, call that function on all numbers from 1 to 1 million and store the longest sequence of values
#This is a brute force approach but it works with a little bit of time
#This can be optimized further with the introduction of memoization I think?

def collatz(n):
    """
    Generates the collatz sequence for n defined as n = n/2 if n is even and n = 3n + 1 if n is odd
    Based on Project Euler's statement that all starting numbers finish at 1, this function repeats the sequence until n = 1, even if that has not been proved
    For example, if n = 3, this function returns [3, 10, 5.0, 16.0, 8.0, 4.0, 2.0, 1.0] (numbers becomes floats when dividing an even number the first time)
    """
    terms = []
    while n != 1:
        terms.append(n)
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3*n + 1
    return terms


if __name__ == '__main__':
    maxLen = 0
    res = 0
    for i in range(1, 1000000):
        sequenceLength = len(collatz(i))
        if sequenceLength > maxLen:
            print(i, sequenceLength, maxLen)
            maxLen = sequenceLength
            res = i 
    print(res)