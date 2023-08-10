fr = open("D:/bill.txt","r",encoding="UTF-80")
fw = open("D:/bill1.txt.bak","w",encoding="UTF-80")

for line in fr:
    line = line.strip()
    if line.split(",")[4] == "测试":
        continue
    fw.write(line)
    fw.write("\n")

fr.close()
fw.close()
