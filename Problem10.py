#Another prime problem
#To start, assume that the original prime checker from problem 3 will still work
#Then, use that prime checker function on every number up to 2,000,000 and store the primes in a list
#Then, sum up the numbers in that list
#While the code takes a while to run, it still seems reasonable
#If there is another prime problem, a more efficient method will be necessary, potentially the sieve of Eratosthenes 

import Problem3

primes = []
for n in range(2, 2000000):
    if Problem3.primeChecker(n):
        primes.append(n)
print(sum(primes))