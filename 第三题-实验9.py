# 使用递归调用实现：遍历指定目录（如F:\test）下所有目录（包含子目录）下. txt文件改为.py文件。
import os
def seacher_file(filename):
    if not os.path.isdir(filename):
        return
    for i in os.listdir(filename):
        cur = os.path.join(filename,i)
        if os.path.isdir(cur):
            seacher_file(cur)
        if os.path.isfile(cur) and cur.endswith('.txt'):
            new_name = os.path.splitext(cur)[0] + '.py'
            new_path = os.path.join(filename,new_name)
            os.rename(cur,new_path)