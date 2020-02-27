a=1
while a<10:
    print(a,end="")
    a+=1
print()

message=""
while message!="quit":
    message=input("please write down a message")

    if message=="quit":
        print("this is the end")
        break

    print(message)


i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)





