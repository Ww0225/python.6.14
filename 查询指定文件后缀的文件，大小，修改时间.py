# 查询指定路径（目录，如：G:\）下的某种类型的文件（txt文件）并返回其文件大小、修改时间
import os,time
def searchfile(filepath):
    if not os.path.isdir(filepath):
        return
    for i in os.listdir(filepath):
        cur = os.path.join(filepath,i)
        if os.path.isdir(cur):
            searchfile(cur)
        if os.path.isfile(cur) and os.path.splitext(cur)[1] == '.txt':
            print(f"文件名为：{cur}，大小为：{os.path.getsize(cur)}，修改时间为：{os.path.getmtime(cur)}")

if __name__ == '__main__':
    searchfile("C:\\")