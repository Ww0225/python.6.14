# 1、现从开发的代码库中得到以下一组数据，数据表示每个文件的代码变更情况。
# {'login.py': 'add 8 del 2 upd 3',
#  'order.py': ' add 15 del 0 upd 34',
#  'info.py': ' add 1 del 20 upd 5',
# 'register.py': ' add 9 del 23 upd 7',
# 'exit.py': ' add 16 del 6 upd 19'
# }
# 其中 add表示新增行数，del表示删除行数，upd表示修改行数。
# 要求，使用带异常处理实现以下问题求解：
# （1）统计出每个文件的变更行数。比如：统计出login.py的变更行数为13。
# （2）从键盘上输入一个文件名，查找该文件的变更行数，文件名不存在，显示“查找的文件不存在”。
# 操作方法与步骤：
# 第（1）题：
# 第一步：创建Test1_1.py程序，根据题目要求，先创建一个字典存储文件代码变更情况。
# 第二步：遍历字典，在循环体内设置一个变量sum用于每个文件的变更行数，然后对字典中的value进行切割并遍历，判断如果是类型转换后的对象是数字，则加入sum，不是数字则跳过。此过程涉及类型转换，需要使用try.....except进行处理。

# 第（2）题：
# 第一步：创建Test1_2.py程序，根据题目要求，先创建一个字典存储文件代码变更情况。
# 第二步：输入要查询的文件名filename，并使用列表推导式对字典中的所有k进行遍历，查看filename是否存在字典中。
# 第三步：判断列表推导式中是否为空，根据判断的结果结合第（1）小题的方法输出结果即可。


# (1)
from collections import defaultdict
filecount = defaultdict(int)
data = {'login.py': 'add 8 del 2 upd 3',
        'order.py': ' add 15 del 0 upd 34',
        'info.py': ' add 1 del 20 upd 5',
        'register.py': ' add 9 del 23 upd 7',
        'exit.py': ' add 16 del 6 upd 19'
        }
for k in data.keys():
    values = data[k].split()
    sum = 0
    for v in values:
        try:
            sum += int(v)
        except:
            pass
    filecount[k]=sum
    print(f"统计出{k}的变更行数为:{sum}")
# (2)
import re
filename = input("请输入你要查找的文件名:")
pattern = re.compile(filename, re.IGNORECASE)
found_files = [key for key in filecount.keys() if re.search(pattern,key)]
for file in found_files:
    print(f"你要查找的文件名为：{file}，其变更行数为：{filecount[file]}")