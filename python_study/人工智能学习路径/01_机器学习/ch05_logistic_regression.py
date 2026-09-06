import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression

# model=LogisticRegression(
#     solver='sag',
#     multi_class='multinomial',
#     class_weight='balanced',
#     max_iter=1000,
#     random_state=42,
#     penalty='l1',
#     C=1.0
# )
dataset=pd.read_csv('heart_disease.csv')
dataset.dropna(inplace=True)
X=dataset.iloc[:,:-1]
y=dataset.iloc[:,-1]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
#特征工程
numerical_features=['年龄','静息血压','胆固醇','最大心率','运动后的ST下降','主血管数量']
categorical_features=['胸痛类型','静息心电图结果','峰值ST段的斜率','地中海贫血']
binary_features=['性别','空腹血糖','运动性心绞痛']

#列转换器ColumnTransformer
columnTransformer=ColumnTransformer(
    transformers=[
        ('num',StandardScaler(),numerical_features),
        ('cat',OneHotEncoder(drop='first'),categorical_features),
        ('bin','passthrough',binary_features),
    ]
)

#特征和转换
X_train=columnTransformer.fit_transform(X_train)
X_test=columnTransformer.transform(X_test)

#模型定义
model=LogisticRegression()
model.fit(X_train,y_train)

print(model.score(X_test,y_test))
# model_ovr1=LogisticRegression(multi_class='ovr')
# from sklearn.multiclass import OneVsRestClassifier
# model_ovr2=OneVsRestClassifier(LogisticRegression())
# model_softmax=LogisticRegression(multi_class='multinomial')