mynumber=[2,89,53,46]
for a in mynumber:
    print(a,end="")




num=""
mylist=[]

while True:
    num=input("please enter a number>")
    if num.upper()=="Q":
        break
    mylist.append(int(num))

    sum=0
    for a in mylist:
        sum+=a
    print(sum)




