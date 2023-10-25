#For Loop with Range
#for number in range(a,b,c)
#range(a,b) for the range eg. 1 to 10 but not including 10
#range( , ,c) for the number of steps to take 
for number in range(1,10,2):
    print (number)

total = 0
for number in range(1,101):
    total+=number
print(total)