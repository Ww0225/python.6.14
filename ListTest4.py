num_list = [1,2,3,4,5,6,7,8,9,10]
index = 0
new_num_list = []
while index < len(num_list):
    if num_list[index] % 2 == 0:
        new_num_list.append(num_list[index])
    index += 1
print(new_num_list)

new_num_list = []
for index in num_list:
    if index % 2 == 0:
        new_num_list.append(index)
print(new_num_list)