# write a file
with open("my_input_file","w") as file_object:
    file_object.write("my name is ")
    file_object.write("hello")
    print(file_object.writable())

with open("my_input_file") as file_object:
    print(file_object.read())

# append to a file
with open("my_input_file","a") as file_object:
    file_object.write("\nwhat is you name?")
    print(file_object.writable())

with open("my_input_file") as file_object:
    for s in file_object.readlines():
        print(s.rstrip())
    print(file_object.writable())
    print(file_object.seekable())
    print(file_object.seek(5))

with open("my_input_file","r+") as file_object:
    for s in file_object.readlines():
        print(s.rstrip())

with open("epiphany","x") as file_object:
    file_object.write("kim sook jin "\
                      +", kim nam jun"\
                      +", park ji min")





