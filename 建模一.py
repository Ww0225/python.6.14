# coding: UTF-8
import pandas as pd
import numpy as np
from matplotlib.font_manager import FontProperties
from scipy import stats

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号#有中文出现的情况，需要u'内容'

from scipy.stats import ttest_ind

font = FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc", size=12)  # 指定本地中文字体文件路径，根据系统环境可能需要修改路径
font.set_family('Times New Roman')  # 设置字体为英文

# 假设df_sales是销售流水表的数据框架，df_members是会员消费明细表的数据框架
# 计算整体消费特征的平均水平
df_sales = pd.read_excel('附件2-销售流水表.xlsx', engine='openpyxl')
df_members = pd.read_excel('附件3-会员消费明细表.xlsx', engine='openpyxl')
product_data = pd.read_excel('附件4-商品信息表.xlsx', engine='openpyxl')


acv = df_sales['je'].mean()  # 平均消费金额
apf = df_sales['sl'].mean()  # 平均购买频次

# 计算会员消费特征的平均水平
macv = df_members['je'].mean()  # 会员平均消费金额
mapf = df_members['sl'].mean()  # 会员平均购买频次

# 比较会员与非会员群体的差异
delta_acv = acv - macv  # 平均消费金额差异
delta_apf = apf - mapf  # 平均购买频次差异

t_value, p_value = ttest_ind(df_sales['je'], df_members['je'])

# 如果p值小于显著性水平（例如0.05），我们可以拒绝零假设，认为差异是显著的
alpha = 0.05
if p_value < alpha:
    print(f"差异显著: t值 = {t_value}, p值 = {p_value}")
else:
    print("差异不显著")

# 绘制柱状图比较平均消费金额
plt.figure(figsize=(10, 6))
plt.bar(['整体', '会员'], [acv, macv], color=['blue', 'green'])
plt.xlabel('群体', fontproperties=font)
plt.ylabel('平均消费金额', fontproperties=font)
plt.title('整体和会员平均消费金额比较', fontproperties=font)
plt.show()

# 绘制柱状图比较平均购买频次
plt.figure(figsize=(10, 6))
plt.bar(['整体', '会员'], [apf, mapf], color=['blue', 'green'])
plt.xlabel('群体', fontproperties=font)
plt.ylabel('平均购买频次', fontproperties=font)
plt.title('整体和会员平均购买频次比较', fontproperties=font)
plt.show()

# 说明会员群体给商场带来的价值
sales_contribution = (df_members['je'].sum() / df_sales['je'].sum())
# 计算销售额
sales_total = (df_members['sj'] * df_members['sl']).sum()
# 计算进货成本
cost = (product_data['wsjj'] * df_members['sl']).sum()
# 计算销售税额
sales_tax = (product_data['sj'] * product_data['xxs'] * df_members['sl']).sum()
# 计算利润
profit_contribution = sales_total - cost - sales_tax

# 标签
labels = ['销售额贡献', '利润贡献']

# 数据
sizes = [sales_contribution, 1 - sales_contribution]

# 颜色
colors = ['#ff9999', '#66b3ff']

# 突出显示会员群体的贡献
explode = (0.1,0)

# 绘图
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
plt.title('会员对商场销售额和利润的贡献比例')
plt.show()