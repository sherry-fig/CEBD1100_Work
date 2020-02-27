mylist=["red", "green","blue"]

mylist1=mylist+["black","white"]
print(mylist1)

mylist.append('black')
print(mylist)

mylist[2]="yellow"
print(mylist)

mylist2=mylist.copy()
del mylist2[1]
print(mylist2)

mylist.remove("red")
print(mylist)

num=1
for a in mylist:
    print("%i %s"%(num,a.upper()))
    num+=1

random_list=[random.randrange(1,100) for i in range(20)]