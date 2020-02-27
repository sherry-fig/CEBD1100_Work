
limit=input("how many times?")
num=int(limit)+1

for a in range(num):

    for b in range(int(limit)):
        print("*", end="")
    print()



for a in range(num):
    print("#"*int(limit))

for a in range(int(limit)):
    print("*"*(a+1))
