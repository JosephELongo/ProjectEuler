#First prime problem!
#Since this is an early problem, I am guessing a brute force method will work
#To start, generate a list of primes from 2 to our target number: 600851475143 
#However, we likely do not have to actually check all the primes up to 600851475143 and that is computationally expensive
#So, we can get all primes up to some arbitrarily large value and then see if 600851475143 can be factored completely by those primes
#If so, we have our solution! Try to divide 600851475143 by each prime and take note of the largest number that it can be evenly divided by
#However, if 600851475143 cannot be evenly divided, we need to generate a larger primeList

def primeChecker(n):
    """
    Takes a number n and returns true if n is prime, else returns false
    Determines primeness by checking remainder of every number from 2 to the square root of n + 1
    Only works for n >= 2
    """
    if n == 2:
        return True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    primeList = []
    target = 600851475143
    max = 0

    for i in range(2, 10000):
        if primeChecker(i):
            primeList.append(i)
    
    for i in primeList:
        #Check if target can be factored by i
        #If so, our new max factor is i
        #Then, to make sure we have factored the number fully, we divide target by i until target % i is not 0
        #ie if the target is 4, we divide it by 2 and our new target is 2
        #2 % 2 is still 0 so we divide it by 2 and our new target is 1 (note that our max factor does not change at this step, this is only meant to ensure full factorization)
        #Then, since our target is 1, we know that we have full factorization
        #After iterating over primeList, if target is still not 1, we know primeList was not long enough

        if target % i == 0:
            max = i
            while target % i == 0:
                target /= i
            #Note: compare to 1.0 because python converts ints to floats when dividing
            if target == 1.0:
                print(max)
                break
    if target != 1.0:
        print("primeList is not long enough")
