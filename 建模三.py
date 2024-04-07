import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号#有中文出现的情况，需要u'内容'

# 加载数据
member_info = pd.read_excel('附件1-会员信息表.xlsx', engine='openpyxl')
consumption_detail = pd.read_excel('附件3-会员消费明细表.xlsx', engine='openpyxl')

# 合并会员信息和消费记录
df_merged = pd.merge(member_info, consumption_detail, on='kh', how='left')

# 删除包含NaN值的行
df_merged.dropna(inplace=True)

# 数据预处理：处理日期时间列
df_merged['dtime'] = pd.to_datetime(df_merged['dtime'], errors='coerce')  # 将消费日期转换为日期时间类型

# 清洗掉 'je' 列中的 NaN 值
df_merged['je'] = df_merged['je'].fillna(0)

df_merged['kh'] = df_merged['kh'].astype(str)

# 计算会员的生命周期阶段特征
df_merged['days_since_registration'] = (df_merged['dtime'] - df_merged['djsj']).dt.days

# 去除注册天数为负数的数据
df_merged = df_merged[df_merged['days_since_registration'] >= 0]

df_merged['total_spent'] = df_merged.groupby('kh')['je'].transform('sum')
df_merged['avg_spent_per_transaction'] = df_merged['je'] / df_merged.groupby('kh')['je'].transform('count')
df_merged['last_purchase_date'] = df_merged.groupby('kh')['dtime'].transform('max')
df_merged['days_since_last_purchase'] = (pd.Timestamp.now() - df_merged['last_purchase_date']).dt.days

# 划分生命周期阶段（这里仅作为示例，实际业务中可能更复杂）
df_merged['lifecycle_stage'] = np.where(df_merged['days_since_registration'] <= 30, 'New Member',
                                        np.where(df_merged['days_since_last_purchase'] <= 90, 'Active Member',
                                                 np.where(df_merged['days_since_last_purchase'] <= 180,
                                                          'Inactive Member',
                                                          'Lost Member')))

# 选择用于状态划分的特征
features = ['total_spent', 'avg_spent_per_transaction', 'days_since_registration', 'days_since_last_purchase']
X = df_merged.groupby('kh')[features].agg('mean').reset_index()

# 数据标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X[features])

kmeans = KMeans(n_clusters=4, random_state=0)
X_clusters = kmeans.fit_predict(X_scaled)

# 将聚类结果添加回原始数据
X['state'] = X_clusters

# 将状态标签合并到原始DataFrame中
df_merged = pd.merge(df_merged, X[['kh', 'state']], on='kh', how='left')

# 删除状态为3的行
df_merged = df_merged[df_merged['state'] != 3]

# 查看结果
print(df_merged[['kh', 'lifecycle_stage', 'state']])

# 绘制状态分布柱状图
plt.figure(figsize=(10, 6))
sns.countplot(x='state', data=df_merged, palette='Set2')
plt.title('会员状态分布')
plt.xlabel('状态')
plt.ylabel('会员数量')
plt.show()

# 绘制生命周期阶段分布柱状图
plt.figure(figsize=(10, 6))
sns.countplot(x='lifecycle_stage', data=df_merged, palette='Set3')
plt.title('会员生命周期阶段分布')
plt.xlabel('生命周期阶段')
plt.ylabel('会员数量')
plt.show()

# 查看状态和生命周期阶段的联合分布，使用堆叠柱状图
plt.figure(figsize=(10, 6))
sns.countplot(x='lifecycle_stage', hue='state', data=df_merged, palette='Set2')
plt.title('会员生命周期阶段与状态分布')
plt.xlabel('生命周期阶段')
plt.ylabel('会员数量')
plt.legend(title='状态')
plt.show()

# 绘制散点图，根据会员状态对会员注册天数和总消费进行着色
sns.scatterplot(x='days_since_registration', y='total_spent', hue='state', data=df_merged, palette='Set2')
plt.title('会员注册天数与总消费（按状态划分）')
plt.xlabel('注册天数')
plt.ylabel('总消费')
plt.show()

# # 筛选出状态为非活跃的会员数据
# inactive_members = df_merged[df_merged['state'] == 2]
#
# # 将筛选结果保存到新的 Excel 文件中
# inactive_members.to_excel('非活跃会员数据.xlsx', index=False, engine='openpyxl')

df_merged.to_excel('各个state会员数据.xlsx', index=False, engine='openpyxl')
