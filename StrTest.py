str1 = "ww and python"
s1 = str1[1]
s2 = str1[-1]
print(s1)
print(s2)

index = str1.index("and")
print(index)

str2 = str1.replace("python","java")
print(str2)

str3 = "hello ww python"
new_str3 = str3.split(" ")
print(new_str3)

str4 = "8 hello ww python 8"
str4_1 = " hello ww python "
new1_str4 = str4_1.strip()
new2_str4 = str4.strip("8")
print(new1_str4)
print(new2_str4)

str5 = "it ww it python"
count = str5.count("it")
print(count)
length = len(str5)
print(length)
