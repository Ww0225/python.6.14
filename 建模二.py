# coding: UTF-8
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号#有中文出现的情况，需要u'内容'


# 加载数据
member_info = pd.read_excel('附件1-会员信息表.xlsx', engine='openpyxl')
consumption_detail = pd.read_excel('附件3-会员消费明细表.xlsx', engine='openpyxl')
product_info = pd.read_excel('附件4-商品信息表.xlsx', engine='openpyxl')

# 数据预处理：合并会员信息和消费明细
member_consumption = pd.merge(consumption_detail, member_info, on='kh')

# 数据预处理：处理日期时间列
member_consumption['dtime'] = pd.to_datetime(member_consumption['dtime'], errors='coerce')  # 将消费日期转换为日期时间类型

# 清洗掉 'je' 列中的 NaN 值
member_consumption['je'] = member_consumption['je'].fillna(0)

# 数据预处理：合并消费明细和商品信息
member_consumption_with_product = pd.merge(member_consumption, product_info, on='spbm')

member_consumption_with_product['kh'] = member_consumption_with_product['kh'].astype(str)


# 计算消费指标
member_consumption_with_product['消费金额累计'] = member_consumption_with_product.groupby('kh')['je'].cumsum()
member_consumption_with_product['消费次数'] = member_consumption_with_product.groupby('kh')['je'].cumcount() + 1
member_consumption_grouped = member_consumption_with_product.groupby('kh').agg({
    'je': ['sum', 'count'],
    'jf': 'sum'
}).reset_index()
member_consumption_grouped.columns = ['_'.join(col).strip() for col in member_consumption_grouped.columns.values]
member_consumption_grouped['平均单次消费金额'] = member_consumption_grouped['je_sum'] / member_consumption_grouped[
    'je_count']

member_consumption_grouped['消费金额累计'] = member_consumption_with_product.groupby('kh')['je'].cumsum()
member_consumption_grouped.to_excel('会员消费统计结果.xlsx', index=False)

# # 构建综合购买力指数
# member_consumption_grouped['CPPI'] = (member_consumption_grouped['je_sum'] * 0.5 +
#                                       member_consumption_grouped['jf_sum'] * 0.3 +
#                                       member_consumption_grouped['平均单次消费金额'] * 0.2)
#
# # 归一化处理
# scaler = StandardScaler()
# member_consumption_grouped['CPPI_scaled'] = scaler.fit_transform(member_consumption_grouped[['CPPI']])
#
# # 使用标准化后的 CPPI 进行 K-means 聚类
# kmeans = KMeans(n_clusters=3, random_state=0).fit(member_consumption_grouped[['CPPI_scaled']])
# member_consumption_grouped['会员层级'] = kmeans.labels_
#
# # 输出结果或进一步分析
# print(member_consumption_grouped)
#
# # 假设df是包含会员指标数据的DataFrame，其中包含'会员层级'和'总消费金额'列
# df = pd.DataFrame({
#     '会员层级': ['高级','中级','低级'],
#     '总消费金额': [100000, 50000, 20000]}
# )
#
# # 绘制柱状图
# plt.bar(df['会员层级'], df['总消费金额'])
# plt.xlabel('会员层级')
# plt.ylabel('总消费金额')
# plt.title('不同会员层级的消费金额对比')
# plt.show()
#
# df = pd.DataFrame({
#     '会员ID':member_consumption_with_product['kh'],
#     '消费金额':member_consumption_with_product['消费金额累计']
# })
#
# # 绘制箱线图
# plt.boxplot(df['消费金额'])
# plt.xlabel('消费金额')
# plt.ylabel('数值')
# plt.title('会员消费金额分布')
# plt.show()
#
# df = pd.DataFrame({
#       '消费金额':member_consumption_with_product['消费金额累计'],
#     '消费频率': member_consumption_grouped['CPPI']
# })
#
# # 绘制散点图
# plt.scatter(df['消费频率'], df['消费金额'])
# plt.xlabel('消费频率')
# plt.ylabel('消费金额')
# plt.title('消费频率与消费金额的关系')
# plt.show()
