#Again, first try a brute force approach
#Loop over all the numbers from 1 to 100 (inclusive) and sum them and their squares
#Then, square the sum and subtract the sum of the squares

sum = 0
sumOfSquares = 0
for i in range(1,101):
    sum += i
    sumOfSquares += i**2
print(sum**2 - sumOfSquares)