def list_while_func(data):
    index = 0
    while index < len(data):
        print(data[index])
        index += 1

def list_for_func(data):
    for index in data:
        print(index)

mylist = [1,2,3,4,5]
list_while_func(mylist)
list_for_func(mylist)