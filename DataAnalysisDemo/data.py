import pandas as pd

def process_excel(input_file_path, output_file_path):
    # 读取 Excel 文件
    data = pd.read_excel(input_file_path)

    # 在此处进行数据处理，例如：
    # 假设我们将所有数值列乘以 2
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    data[numeric_columns] = data[numeric_columns] * 2

    # 保存处理后的数据到新的 Excel 文件
    data.to_excel(output_file_path, index=False)

# 调用函数
input_file_path = 'D:/HuaweiMoveData/Users/SUN\Desktop/data.xlsx'
output_file_path = 'D:/HuaweiMoveData/Users/SUN/Desktop/data.xlsx'
process_excel(input_file_path, output_file_path)
