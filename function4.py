def print_list(mylist,title=""):
    if len(title)>0:# 是有title的
        print("title: "+title)
    for a in mylist:
        print(a)

colour_list=["red","green","blue"]

print_list(colour_list,"list of colours")