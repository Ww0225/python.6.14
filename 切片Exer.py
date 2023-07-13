my_str = "万过薪月，员序程马黑来，nohtyP学"
result1 = my_str[9:4:-1]
print(result1)

new_str = my_str.split("，")
print(new_str[1])
new_str = new_str[1].replace("来","")
print(new_str[::-1])