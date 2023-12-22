from collections import defaultdict

'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

#What does it mean to have a Sunday fall on the first of the month?
#DOW = Day of Month = 1
#Three variables:
#Day, month, and year
#Iterate over day, until day hits a certain value based on month + year
#Month is going to be a key that points to a number of days
#Feb is going to have two values -> 28 or 29
#1/1/1900: 1,1,0

months_no = {
4:30,
6: 30,
9: 30,
11: 30,
2: 28
}
for i in range(12):
    if i+1 not in months_no.keys():
        months_no[i+1] = 31


dow = 1

day = 1
year = 1901
month = 1
counter = 0

for i in range(36524):
    

    if month == 12 and day == 31:
        month = 1
        day = 1
        year += 1

    elif day == months_no[month] and month != 2:
        day = 1
        month += 1

    elif (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)) and day == 28 and month == 2:
        day = 1
        month += 1

    elif year % 4 == 0 and day == 29 and month == 2:
        day = 1
        month += 1

    else:
        day += 1
    
    dow += 1
    if dow >= 8:
        dow = 1
    print(day, month, year, dow)

    if dow == 6 and day == 1:
        counter+=1
print(counter)    



