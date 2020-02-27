

#loop03-03
a=""
while a.upper()!="N":
    num = input("please enter a number>")
    if a.upper()=="N":
        break
    if int(num)%2==0:
        print("the number is even")
    else:
        print("the number is odd")
    a=input("if you want to continue or not?")


