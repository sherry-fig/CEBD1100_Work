#一次性显示
with open('my_input_file') as file_object:
    contents = file_object.read()

print(contents.rstrip())

#一行行显示（用于显示容量大的file)
#方法1
with open('my_input_file') as file_object:
    for u in file_object:
        print(u.rstrip())

#方法2
with open('my_input_file') as file_object:
    e=file_object.readlines() #return 的是list
    print(e)
for line in e:
    print(line.rstrip())
