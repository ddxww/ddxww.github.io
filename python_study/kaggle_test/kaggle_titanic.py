import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

train_df=pd.read_csv(r"D:\机器学习data\lx2\train.csv")
test_df=pd.read_csv(r"D:\机器学习data\lx2\test.csv")
X=train_df.copy()
X.drop(columns=['Survived','PassengerId','Name','Ticket','Cabin'], inplace=True)
X["Pclass"] = X["Pclass"].astype("object")
y=train_df['Survived']

#找到出现最多的embarked
embarked_mode = X["Embarked"].mode()[0]
X["Embarked"] = X["Embarked"].fillna(embarked_mode)
age_median = X["Age"].median()
X["Age"] = X["Age"].fillna(age_median)

#分类，分别进行预处理
df_object_columns = X.select_dtypes(include=["object"]).columns
df_num_columns = X.select_dtypes(include=["number"]).columns

#列转换器ColumnTransformer
columnTransformer=ColumnTransformer(
    transformers=[
        ('num',StandardScaler(),df_num_columns),
        ('cat',OneHotEncoder(drop='first',handle_unknown='ignore'),df_object_columns),
    ]
)
X_processed = columnTransformer.fit_transform(X)
#分类
X_train, X_test, y_train, y_test = train_test_split(X_processed,y,test_size=0.3,random_state=42)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

model=LogisticRegression(max_iter=10000)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
# print(accuracy_score(y_test,y_pred))
# cm = confusion_matrix(y_test, y_pred)
# print(cm)
print(classification_report(y_test,y_pred,target_names=["死亡", "生还"]))

# 保存PassengerId，提交结果时需要
test_id = test_df["PassengerId"]

# 删除与训练集相同的列
X_kaggle = test_df.copy()
X_kaggle.drop(
    columns=["PassengerId", "Name", "Ticket", "Cabin"],
    inplace=True
)

# Pclass和训练集保持相同类型
X_kaggle["Pclass"] = X_kaggle["Pclass"].astype("object")

# 使用训练集计算出的众数和中位数填充
X_kaggle["Embarked"] = X_kaggle["Embarked"].fillna(embarked_mode)
X_kaggle["Age"] = X_kaggle["Age"].fillna(age_median)

# Titanic的test.csv中Fare通常缺少1个值
fare_median = X["Fare"].median()
X_kaggle["Fare"] = X_kaggle["Fare"].fillna(fare_median)

# 注意：这里只能transform，不能重新fit_transform
X_kaggle_processed = columnTransformer.transform(X_kaggle)

# 使用全部训练数据重新训练
model.fit(X_processed, y)
test_pred = model.predict(X_kaggle_processed)

# 生成Kaggle要求的提交文件
submission = pd.DataFrame({
    "PassengerId": test_id,
    "Survived": test_pred
})
# 保存文件
submission.to_csv(r"D:\机器学习data\lx2\submission.csv",index=False)
print(submission.head())
print("提交文件已生成")

#随机森林
from sklearn.ensemble import RandomForestClassifier
rf_model = RandomForestClassifier(
    n_estimators=500,
    max_depth=6,
    min_samples_leaf=3,
    random_state=42
)

rf_model.fit(X_train, y_train)
rf_y_pred = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_y_pred)
print("随机森林验证集准确率：", rf_accuracy)
rf_model.fit(X_processed, y)
test_pred = rf_model.predict(X_kaggle_processed)
submission = pd.DataFrame({
    "PassengerId": test_id,
    "Survived": test_pred
})
submission.to_csv(r"D:\机器学习data\lx2\submission_rf.csv",index=False)
#网格搜索
from sklearn.model_selection import GridSearchCV

param_grid = {
    "n_estimators": [300, 500],
    "max_depth": [4, 6, 8, None],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 3, 5],
    "max_features": ["sqrt", "log2"]
}

grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    scoring="accuracy",
    cv=5,
    n_jobs=-1,
    verbose=1
)
grid_search.fit(X_processed, y)
print("最佳参数：", grid_search.best_params_)
print("最佳交叉验证准确率：", grid_search.best_score_)
best_model = grid_search.best_estimator_

test_pred = best_model.predict(X_kaggle_processed)
submission = pd.DataFrame({"PassengerId": test_id,"Survived": test_pred})
submission.to_csv(r"D:\机器学习data\lx2\submission_grid.csv",index=False)