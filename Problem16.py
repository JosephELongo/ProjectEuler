#Can Python calculate 2**1000?
#Thankfully, it easily can!
#Therefore, we simply have to calculate 2**1000, convert it into a string, and then sum the string, converting each character to an int as we go

num = str(2**1000)
sum = 0
for i in num:
    sum+= int(i)
print(sum)