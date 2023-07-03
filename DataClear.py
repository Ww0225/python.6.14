import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from scipy.sparse import hstack
from joblib import Parallel, delayed

# 读取附件二数据文件
data = pd.read_excel('附件二.xlsx')
# 删除缺失值
data = data.dropna()
# 去重
data = data.drop_duplicates()

# 提取单选题- 1-22列的数据
columns_1_to_22 = data.iloc[:,0:22]
# 提取多选题_23_to_30
columns_22_to_30 = data.iloc[:,22:30]

# 创建独热编码器对象
encoder_single_choice = OneHotEncoder(sparse_output=False)
encoder_multi_choice = OneHotEncoder(sparse_output=False)

# 并行处理单选题的独热编码
def encode_single_choice(column):
    column_data = data[[column]]
    encoded_data = encoder_single_choice.fit_transform(column_data)
    encoded_df = pd.DataFrame(encoded_data, columns=encoder_single_choice.get_feature_names_out([column]))
    return encoded_df.reset_index(drop=True)

# 并行处理多选题的独热编码
def encode_multi_choice(column):
    column_data = data[[column]]
    encoded_data = encoder_multi_choice.fit_transform(column_data)
    encoded_df = pd.DataFrame(encoded_data, columns=encoder_multi_choice.get_feature_names_out([column]))
    return encoded_df.reset_index(drop=True)

# 并行处理单选题的独热编码
single_choice_encoded = Parallel(n_jobs=-1)(delayed(encode_single_choice)(column) for column in columns_1_to_22)

# 并行处理多选题的独热编码
multi_choice_encoded = Parallel(n_jobs=-1)(delayed(encode_multi_choice)(column) for column in columns_22_to_30)

# 合并单选题编码结果
encoded_df_single = pd.concat(single_choice_encoded, axis=1) if single_choice_encoded else None

# 合并多选题编码结果
encoded_df_multi = pd.concat(multi_choice_encoded, axis=1) if multi_choice_encoded else None

# 将原始数据和编码后的数据合并
data_encoded = pd.concat([data.reset_index(drop=True), encoded_df_single, encoded_df_multi], axis=1)

# 将数据导出到Excel文件
data_encoded.to_excel('处理后的数据.xlsx', index=False)