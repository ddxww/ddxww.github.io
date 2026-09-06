import numpy as np
import pandas as plt
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix,classification_report,roc_auc_score,roc_curve
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

y_true=['猫','猫','猫','猫','猫','猫','狗','狗','狗','狗']
y_pred=['猫','猫','狗','猫','猫','猫','猫','猫','狗','狗']
matrix=confusion_matrix(y_true,y_pred)
print(matrix)
print(classification_report(y_true,y_pred))
#生成数据
X,y=make_classification(n_samples=1000,n_features=20,n_classes=2,random_state=42)
print(X.shape)
print(y.shape)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)
model=LogisticRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
report = classification_report(y_test,y_pred)
print(report)
#获取预测正类的概率值
y_pred_proba=model.predict_proba(X_test)[:,1]
print(y_pred_proba)
roc_auc=roc_auc_score(y_test,y_pred_proba)
print(roc_auc)
# 绘制 ROC 曲线
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

plt.figure(figsize=(6, 5))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
# 对角线（随机猜测基准）
plt.plot([0, 1], [0, 1], color='navy',lw=2,)

plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
plt.title('ROC Curve')
plt.legend(loc="lower right")
plt.show()