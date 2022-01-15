import Problem3

#To generate a list of prime numbers, we can reuse the function from Problem Three
#If that function is too slow to compute 10,001 primes, we can try to write a faster prime function

primes = []
n = 2
while len(primes) < 10001:
    if Problem3.primeChecker(n):
        primes.append(n)
    n+=1
print(primes[-1])
