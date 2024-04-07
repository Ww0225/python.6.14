from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 加载数据
member_info = pd.read_excel('附件1-会员信息表.xlsx', engine='openpyxl')
consumption_detail = pd.read_excel('附件3-会员消费明细表.xlsx', engine='openpyxl')

# 将会员信息表中的生日列转换为日期时间类型
member_info['csny'] = pd.to_datetime(member_info['csny'], errors='coerce')

# 合并会员信息和消费记录
df_merged = pd.merge(member_info, consumption_detail, on='kh', how='left')

# 删除包含NaN值的行
df_merged.dropna(inplace=True)

# 数据预处理：处理日期时间列
df_merged['dtime'] = pd.to_datetime(df_merged['dtime'], errors='coerce')  # 将消费日期转换为日期时间类型

# 清洗掉 'je' 列中的 NaN 值，并将 NaN 填充为 0
df_merged['je'] = df_merged['je'].fillna(0)

# 计算会员的年龄
df_merged['Age'] = (pd.Timestamp.now().year - df_merged['csny'].dt.year).astype(int)

# 将会员卡号转换为字符串类型
df_merged['kh'] = df_merged['kh'].astype(str)

# 根据会员消费明细计算最后一次购买时间、平均购买价值和购买频率等特征
df_merged['last_purchase_date'] = df_merged.groupby('kh')['dtime'].transform('max')
df_merged['avg_spent_per_transaction'] = df_merged['je'] / df_merged.groupby('kh')['je'].transform('count')

# 根据需要计算活跃状态
end_date = pd.Timestamp(2017, 6, 1)

# 计算是否为活跃会员，活跃定义为最后一次购买日期在90天内
df_merged['Active'] = (df_merged['last_purchase_date'] >= end_date - pd.Timedelta(days=90)).astype(int)

# 选择并创建 DataFrame
df = df_merged[['kh', 'Age', 'xb', 'last_purchase_date', 'avg_spent_per_transaction', 'Active']]

# 创建副本以避免警告
df_copy = df.copy()

# 将日期时间列转换为距离今天的天数
df['last_purchase_days'] = (pd.Timestamp.now() - df['last_purchase_date']).dt.days

# 使用 .loc[] 方法创建新列，并删除原始日期时间列
df['last_purchase_date'] = df['last_purchase_days']  # 将 last_purchase_days 重命名为 last_purchase_date
df.drop(columns=['last_purchase_days'], inplace=True)  # 删除原始日期时间列

# 加载非活跃数据表
inactive_member_info = pd.read_excel('非活跃会员数据.xlsx', engine='openpyxl')

# 合并活跃数据表和非活跃数据表
df_merged = pd.merge(df, inactive_member_info, on='kh', how='left')

# 将所有列的数据类型转换为字符串或浮点数类型
df_merged = df_merged.astype(str)

# 处理缺失值
df_merged.fillna('unknown', inplace=True)  # 填充 NaN 值为字符串 'unknown'

# 对非数值型特征进行标签编码
label_encoders = {}
for column in df_merged.columns:
    if df_merged[column].dtype == 'object':
        label_encoders[column] = LabelEncoder()
        df_merged[column] = label_encoders[column].fit_transform(df_merged[column])

# 分离特征和标签
X = df_merged.drop('Active', axis=1)
y = df_merged['Active']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建随机森林模型
model = RandomForestClassifier()

# 训练模型
model.fit(X_train, y_train)

# 预测测试集
y_pred = model.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# 打印分类报告
report = classification_report(y_test, y_pred)
print(report)

# 加载非活跃会员数据
inactive_member_info = pd.read_excel('非活跃会员数据.xlsx', engine='openpyxl')

# 选择特征和目标列
train_features = ['xb', 'days_since_registration', 'avg_spent_per_transaction']
target_column = 'state'

# 获取活跃会员特征
inactive_members_features = inactive_member_info[train_features]

# 使用 LabelEncoder 对分类特征进行编码
label_encoders = {}
for column in inactive_members_features.select_dtypes(include=['object']).columns:
    label_encoders[column] = LabelEncoder()
    inactive_members_features[column] = label_encoders[column].fit_transform(inactive_members_features[column])

# 拆分数据集
X_train, X_test, y_train, y_test = train_test_split(inactive_members_features, inactive_member_info[target_column], test_size=0.2, random_state=42)

# 训练模型
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 预测并评估模型
predictions = model.predict(X_test)
print("Accuracy:", model.score(X_test, y_test))
print(classification_report(y_test, predictions))

# 检查特征名字列表和 DataFrame 的列名的差异
data_columns = inactive_members_features.columns.tolist()
missing_columns = [col for col in train_features if col not in data_columns]
extra_columns = [col for col in data_columns if col not in train_features]

print("Missing columns:", missing_columns)
print("Extra columns:", extra_columns)

# 调整特征名字列表，确保列名一致
train_features = [col for col in train_features if col in data_columns]

# 使用调整后的特征名字列表重新选择特征
inactive_members_features = inactive_members_features[train_features]

# 使用调整后的特征重新预测
activation_probabilities = model.predict_proba(inactive_members_features)[:, 0]
print(activation_probabilities)