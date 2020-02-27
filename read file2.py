with open('my_input_file') as file_object:
    n=file_object.read(6)
print(n)

# seek\ tell问题？
with open('my_input_file') as file_object:
    print(file_object.seek(7))
    print(file_object.tell())

with open('my_input_file') as file_object:
    print(file_object.readable())