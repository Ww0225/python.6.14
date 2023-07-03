import pandas as pd
import matplotlib.pyplot as plt
from pandas import Index
from pylab import mpl

# 设置中文显示字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 读取附件二数据文件
data = pd.read_excel('附件二.xlsx')

# 缺失值处理
data = data.dropna() # 删除含有缺失值的行
print(data.head(30))
print(data.info())
print(data.duplicated())
print(data.isnull())
# 数据预处理和清洗
# 假设我们只关注部分特征，可以选择需要的列进行分析
# 强烈建议自行修改表头(例如去掉序号),这里我们因为是示例展示便不再修改
selected_columns = ['1、您的性别(1-22题为单选题)','2、您的专业','3、您所在的年级','4、您的性格','5、您最常通过哪种方式上网？','6、您每周的上网时长大约是多少？','7、您是否使用过学习软件工具？']
data = data[selected_columns]



# 数值化处理
# 例如，可以使用独热编码对分类变量进行数值化
# 在独热编码过程中，创建的新列名的命名方式是在原始列名的基础上添加各个类别的名称
# 例如 对于列名为"您的性别(1-22为单选题)",如果该列有两个类别，即“男”和“女”,
# 那么独热编码后将创建两个新的列,分别命名为"您的性别(1-22题为单选题_女)"
# 和"您的性别(1-22题为单选题_男)"
categorical_columns = ['1、您的性别(1-22题为单选题)','2、您的专业','3、您所在的年级','4、您的性格','5、您最常通过哪种方式上网？']
for column in categorical_columns:
    encoded_columns = pd.get_dummies(data[column],prefix=column)
    data = pd.concat([data,encoded_columns],axis=1)
print(data.columns)

# 数据分析和可视化
# 示例：计算每个性别的人数并绘制柱状图
gender_counts = data['1、您的性别(1-22题为单选题)_女'].sum(),data['1、您的性别(1-22题为单选题)_男'].sum()
gender_labels = ['女性','男性']

plt.bar(gender_labels,gender_counts)
plt.xlabel('性别')
plt.ylabel('人数')
plt.title('性别分布')
plt.show()

# 示例：计算各专业的人数并绘制饼图
major_counts = data['2、您的专业'].value_counts()

plt.pie(major_counts,labels=major_counts.index,autopct='%1.1f%%')
plt.axis('equal')
plt.title('专业分布')
plt.show()

# 示例：计算使用学习软件工具的人数并绘制条形图
tool_users = data['7、您是否使用过学习软件工具？'].value_counts()

plt.bar(tool_users.index,tool_users)
plt.xlabel('使用工具情况')
plt.ylabel('人数')
plt.title('学习软件工具使用情况')
plt.show()