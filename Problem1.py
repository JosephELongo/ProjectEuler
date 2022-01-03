#To find all multiples of 3 or 5, iterate over the range from 1 to 1000
#If i % 3 == 0 or i % 5 == 0, add i to a count variable

count = 0
upperLimit = 1000
lowerLimit = 1

for i in range(lowerLimit, upperLimit):
    if i % 3 == 0 or i % 5 == 0:
        count += i
print(count)