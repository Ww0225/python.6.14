fr = open("D:\pybill.txt","r",encoding="UTF-8")
fw = open("D:\pybill.txt.bak","w",encoding="UTF-8")

for line in fr:
    line = line.strip()
    words = line.split(",")
    for word in words:
        if word == "正式":
            fw.write(line)
            fw.write("\n")
        else:
            continue
fr.close()
fw.close()


