#First, get all of the numbers from a txt file
#Then, convert them to an int and add them together
#Finally, convert the sum back to a string to get the first ten digits
nums = open('Problem13.txt', 'r').readlines()
sum = 0 
for num in nums:
    sum += int(num)
print(str(sum)[0:10])