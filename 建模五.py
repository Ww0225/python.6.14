import pandas as pd
from itertools import combinations
from joblib import Parallel, delayed

# 读取数据
sales_data = pd.read_excel('附件3-会员消费明细表.xlsx')

# 只保留 'spbm' 列中的字符串类型数据
sales_data = sales_data[sales_data['spbm'].apply(lambda x: isinstance(x, str))]

# 并行计算商品连带率
def calculate_cohesion_parallel(data):
    item_combos = pd.DataFrame(combinations(data['spbm'].unique(), 2))
    item_combos['count'] = Parallel(n_jobs=-1)(delayed(count_combinations)(data, combo) for combo in item_combos.itertuples(index=False))
    item_combos['cohesion'] = item_combos['count'] / item_combos['count'].max()
    return item_combos

# 并行计算商品组合出现的次数
def count_combinations(data, combo):
    item1, item2 = combo
    count = ((data['spbm'] == item1) & (data['spbm'] == item2)).sum()
    return count

# 计算商品连带率
item_combos = calculate_cohesion_parallel(sales_data)

# 找出连带率最高的商品对
high_cohesion_items = item_combos.sort_values(by='cohesion', ascending=False).head(10)

# 输出连带率最高的商品对
print("连带率最高的商品对:")
print(high_cohesion_items)

# 生成促销建议
promotions = high_cohesion_items.merge(sales_data.groupby('spbm').mean(), on='spbm')

# 打印促销建议
print("\n促销建议:")
for index, row in promotions.iterrows():
    print(f"商品编号: {row['spbm']} - 连带商品: {row['spbm']}")
