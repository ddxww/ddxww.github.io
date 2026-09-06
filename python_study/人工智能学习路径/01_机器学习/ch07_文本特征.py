from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

X_train = [
    "win a free prize",
    "meeting at ten",
    "claim your reward",
    "please send the report"
]

y_train = [1, 0, 1, 0]

X_test = [
    "win your reward",
    "send the report"
]

# 测试集的正确答案
y_test = [1, 0]

# 特征提取
vectorizer = CountVectorizer(stop_words="english")

X_train_count = vectorizer.fit_transform(X_train)
X_test_count = vectorizer.transform(X_test)

print("词表：")
print(vectorizer.get_feature_names_out())

print("训练集词频矩阵：")
print(X_train_count.toarray())

print("测试集词频矩阵：")
print(X_test_count.toarray())

# 模型训练
model = LogisticRegression()
model.fit(X_train_count, y_train)

# 模型预测
predictions = model.predict(X_test_count)

print("正确答案：", y_test)
print("预测结果：", predictions)

# 模型评价
print("准确率：", accuracy_score(y_test, predictions))

print("混淆矩阵：")
print(confusion_matrix(y_test, predictions))

print("分类报告：")
print(
    classification_report(
        y_test,
        predictions,
        target_names=["正常信息", "垃圾信息"],
    )
)