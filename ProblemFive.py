#To determine the smallest possible number that is evenly divisible by all the numbers from 1 to 20,
#we need to be able to divide it by all the prime factors of 1 through 20
#For example, to make a number evenly divisible by all the numbers from 1 to 5, it would be equal to 1 * 2 * 3 * 2 * 5
#Where the 1 accounts for 1, the first 2 accounts for 2, and the 3 accounts for 3
#The second 2 accounts for 4 which is equal to 2 * 2 and the 5 accounts for 5
#Because we are only going up to 20, it is easy enough to write out all the prime factors by hand
#1: 1
#2: 2
#3: 3
#4: 2 * 2
#5: 5
#6: 2 * 3
#7: 7
#8: 2 * 2 * 2
#9: 3 * 3
#10: 2 * 5
#11: 11
#12: 2 * 2 * 3 * 3
#13: 13
#14: 2 * 7
#15: 3 * 5
#16: 2 * 2 * 2 * 2
#17: 17
#18: 2 * 3 * 3
#19: 19
#20: 2 * 2 * 5
#Finally, we simply multiply by all the prime factors: 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19
#If a larger number was asked for, it would likely require implementing a prime factor function which could be done easily enough for small numbers using
#the code from ProblemThree.py
print(2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19)