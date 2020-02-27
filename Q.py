num=""
while num.upper()!="Q":
    num=input("enter your number")

    if num.upper() == "Q":
        print("this is the end")
        break

    if int(num) % 10 == 0:
        print("the number is a multiple of 10")
    else:
        print("the number is not a multiple of 10")





