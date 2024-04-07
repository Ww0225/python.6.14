import pandas as pd

# 1. 数据加载与清洗
# 读取会员信息数据
member_data = pd.read_excel('附件1-会员信息表.xlsx', engine='openpyxl')

# 读取销售流水表
sales_data = pd.read_excel('附件2-销售流水表.xlsx', engine='openpyxl')

# 读取会员消费明细表
consumption_data = pd.read_excel('附件3-会员消费明细表.xlsx', engine='openpyxl')

# 读取商品信息表
product_data = pd.read_excel('附件4-商品信息表.xlsx', engine='openpyxl')

# 2. 处理缺失值与异常值
member_data.dropna(inplace=True)
sales_data.dropna(inplace=True)
sales_data = sales_data[sales_data['sl'] > 0]
consumption_data.dropna(inplace=True)
consumption_data = consumption_data[consumption_data['sl'] > 0]
consumption_data = consumption_data[consumption_data['jf'] > 0]
consumption_data = consumption_data[consumption_data['sj'] > 0]
consumption_data = consumption_data[consumption_data['je'] > 0]
# 如果不是datetime类型，则将其转换为datetime类型
consumption_data['dtime'] = pd.to_datetime(consumption_data['dtime'])
# 筛选附件3中的数据以匹配附件2的时间范围
start_date = '2016-01-01'
end_date = '2017-12-31'
consumption_data = consumption_data[(consumption_data['dtime'] >= start_date) & (consumption_data['dtime'] <= end_date)]


# 将值为0替换为 NaN
product_data[['wsjj', 'hsjj', 'sj']] = product_data[['wsjj', 'hsjj', 'sj']].replace(0, pd.NA)
# 清除值为NaN的行
product_data.dropna(subset=['wsjj', 'hsjj', 'sj'],inplace=True)
product_data.dropna(inplace=True)
# 从会员消费明细表中筛选出在附件一中的会员消费数据
filtered_consumption_data = consumption_data[consumption_data['kh'].isin(member_data['kh'])]

consumption_data['dtime'] = pd.to_datetime(consumption_data['dtime'])

# 将处理后的数据保存为 Excel 文件
# 保存修改后的数据到原始文件中
member_data.to_excel('附件1-会员信息表.xlsx', index=False)
sales_data.to_excel('附件2-销售流水表.xlsx', index=False)
product_data.to_excel('附件4-商品信息表.xlsx', index=False)
filtered_consumption_data.to_excel('附件3-会员消费明细表.xlsx', index=False)
