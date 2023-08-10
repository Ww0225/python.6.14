file1 = open("D:\word.txt","r",encoding="UTF-8")
# count = file1.read().count("love")
# print(count)
count = 0
for line in file1:
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word == "love":
            count += 1
print(count)
file1.close()