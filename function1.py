def my_max(n1,n2,n3):
    num=[n1,n2,n3]
    max=num[0]
    for a in num:
       if a>max:
          max=a
    return max

print(my_max(5,6,7))

def print_name(first="unknownfirst", last="unknownlast"):
    print(first+" "+last)

print_name()

print_name("one")

print_name("one","two")