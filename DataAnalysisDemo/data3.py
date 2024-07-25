import pandas as pd
import numpy as np

def linear_regression_demo(input_file_path):
    # 读取 Excel 文件
    data = pd.read_excel(input_file_path)

    X = data.iloc[:, :2].values
    y = data.iloc[:, -1].values

    X = np.hstack((np.ones((X.shape[0], 1)), X))
    pinv = np.linalg.pinv(X.T @ X)
    theta = pinv @ X.T @ y
    y_pred = X @ theta

    # 计算均方误差
    mse = np.mean((y - y_pred) ** 2)

    print(f"回归系数: {theta}")
    print(f"均方误差: {mse}")

# 调用函数，传入 Excel 文件路径
input_file_path = 'D:/HuaweiMoveData/Users/SUN/Desktop/data2.xlsx'
linear_regression_demo(input_file_path)