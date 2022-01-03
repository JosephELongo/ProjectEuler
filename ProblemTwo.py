#While a Fibonacci recursive function could be used, it should be possible to create a list of all the terms less than or equal to 4 million
#by adding previous terms: n = n-1 + n-2
#Then, iterate over that list and count up all values where i % 2 == 0

fibMax = 4000000
fibFirst = 1
fibSecond = 2
fibList = [fibFirst, fibSecond]
count = 0

fibNext = fibList[len(fibList)-1] + fibList[len(fibList)-2]

while fibNext < fibMax:
    fibList.append(fibNext)
    fibNext = fibList[len(fibList)-1] + fibList[len(fibList)-2]

for i in fibList:
    if i % 2 == 0:
        count+=i

print(count)