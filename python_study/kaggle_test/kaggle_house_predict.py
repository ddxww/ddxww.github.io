import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.linear_model import LinearRegression,Ridge
from sklearn.metrics import r2_score,mean_squared_error

print("模型训练完成")
df = pd.read_csv(r"D:\机器学习data\lx1\train.csv")

X = df.drop(columns=["Id", "SalePrice"])
y = np.log1p(df["SalePrice"])
df_object_columns = X.select_dtypes(include=["object"]).columns
df_num_columns = X.select_dtypes(include=["number"]).columns

# 类别缺失值填字符串 None
X[df_object_columns] = X[df_object_columns].fillna("None")

# 数值缺失值填每一列的中位数
X[df_num_columns] = X[df_num_columns].fillna(X[df_num_columns].median())

onehot_encoder = OneHotEncoder(handle_unknown='ignore',sparse_output=False)
X_object = onehot_encoder.fit_transform(X[df_object_columns])
scaler = StandardScaler()
X_num = scaler.fit_transform(X[df_num_columns])
X_processed = np.hstack([X_num,X_object])

X_train, X_test, y_train, y_test = train_test_split(X_processed,y,test_size=0.3,random_state=42)
# # 线性回归
# model = LinearRegression()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print("R²：", model.score(X_test, y_test))
# 正则化
# ridge = Ridge(alpha=0.1)
# model_rider = ridge.fit(X_train, y_train)
# y_pred = model_rider.predict(X_test)
# r2 = r2_score(y_test, y_pred)
# print(r2)
# result = pd.DataFrame({
#     "真实房价": y_test.values,
#     "预测房价": y_pred,
#     "误差": y_test.values - y_pred
# })
# print(result.head(10))
param_grid = {
    "alpha": [0.0001,0.001, 0.01, 0.1, 1, 10, 30, 50, 100]
}

grid_search = GridSearchCV(
    estimator=Ridge(),
    param_grid=param_grid,
    cv=5,
    scoring="r2",
    n_jobs=-1
)

grid_search.fit(X_train, y_train)

print("最优 alpha：", grid_search.best_params_["alpha"])
print("交叉验证平均 R²：", grid_search.best_score_)

best_ridge = grid_search.best_estimator_
y_pred = best_ridge.predict(X_test)

print("测试集 R²：", r2_score(y_test, y_pred))
print("测试集 RMSE：",np.sqrt(mean_squared_error(y_test, y_pred)))
#读取test
test_df = pd.read_csv(r"D:\机器学习data\lx1\test.csv")

test_ids = test_df["Id"].copy()
X_kaggle_test = test_df.drop(columns=["Id"]).copy()

train_medians = X[df_num_columns].median()

# 处理缺失值
X_kaggle_test[df_object_columns] = (
    X_kaggle_test[df_object_columns].fillna("None")
)

X_kaggle_test[df_num_columns] = (
    X_kaggle_test[df_num_columns].fillna(train_medians)
)

# 使用训练阶段已经拟合好的编码器和标准化器
X_kaggle_object = onehot_encoder.transform(
    X_kaggle_test[df_object_columns]
)

X_kaggle_num = scaler.transform(
    X_kaggle_test[df_num_columns]
)

X_kaggle_processed = np.hstack([
    X_kaggle_num,
    X_kaggle_object
])

print("训练特征数：", X_processed.shape[1])
print("测试特征数：", X_kaggle_processed.shape[1])

# 使用最佳 alpha，在全部训练数据上训练
final_model = Ridge(
    alpha=grid_search.best_params_["alpha"]
)

final_model.fit(X_processed, y)

# 预测并还原房价
test_pred_log = final_model.predict(
    X_kaggle_processed
)

test_pred_price = np.expm1(test_pred_log)

submission = pd.DataFrame({
    "Id": test_ids,
    "SalePrice": test_pred_price
})

print(submission.head())
submission.to_csv(
    r"D:\机器学习data\lx1\submission.csv",
    index=False
)
print("submission.csv 保存完成")