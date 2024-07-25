import numpy as np
import pandas as pd

def linear_regression_manual(input_file_path):
    data = pd.read_excel(input_file_path)
    X = data.iloc[:, :2].values
    y = data.iloc[:, -1].values
    y = y.reshape(-1, 1)

    X_mean = np.mean(X, axis=0)
    y_mean = np.mean(y)

    # 计算斜率和截距
    numerator = np.sum((X - X_mean) * (y - y_mean), axis=0)
    denominator = np.sum((X - X_mean) ** 2, axis=0)
    slope = numerator / denominator
    intercept = y_mean - np.dot(slope, X_mean)

    print(f"斜率: {slope}")
    print(f"截距: {intercept}")

# 调用函数，传入 Excel 文件路径
input_file_path = 'D:/HuaweiMoveData/Users/SUN/Desktop/data2.xlsx'
linear_regression_manual(input_file_path)