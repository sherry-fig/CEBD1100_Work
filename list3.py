mylist = [4,5,10,20,10,54,22,1,20,20]

# get the lowest value
# get the highest value
# print a list of duplicate number

min = mylist[0]
for x in mylist:
    if min >x:
        min = x
print(min)

max = mylist[0]
for y in mylist:
    if max < y:
        max = y
print(max)

