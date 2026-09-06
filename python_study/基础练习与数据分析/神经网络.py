import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical


# 设置中文显示（优先选择字符完整的字体）
def set_chinese_font():
    # 扩展字体检测列表，优先选择字符更完整的字体
    font_priorities = [
        'microsoft yahei',  # 微软雅黑（字符完整度高）
        'simhei',  # 黑体
        'pingfang sc',  # 苹方
        'heiti tc',  # 黑体（macOS）
        'simsun',  # 宋体（作为备选）
    ]

    # 查找系统中可用的字体
    available_fonts = []
    for font_path in fm.findSystemFonts():
        font_name = fm.FontProperties(fname=font_path).get_name().lower()
        for priority_font in font_priorities:
            if priority_font in font_name:
                available_fonts.append((font_priorities.index(priority_font), font_path))
                break

    if available_fonts:
        # 按优先级排序，选择最优字体
        available_fonts.sort(key=lambda x: x[0])
        best_font = available_fonts[0][1]
        font_name = fm.FontProperties(fname=best_font).get_name()
        plt.rcParams["font.family"] = font_name
        print(f"使用字体：{font_name}")
    else:
        print("警告：未检测到中文字体，可能无法正常显示中文")

    plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题


set_chinese_font()

# 1. 生成模拟花卉数据（4种花卉，每种100个样本）
np.random.seed(42)  # 固定随机种子，保证结果可复现

# 定义4种花卉的特征均值（模拟真实花卉的特征分布）
# 特征顺序：[花瓣长度, 花瓣宽度, 花萼长度, 花萼宽度]
flower_means = {
    "玫瑰": [4.5, 2.0, 5.0, 2.5],
    "郁金香": [3.0, 1.5, 4.0, 1.8],
    "向日葵": [6.0, 2.5, 7.0, 3.0],
    "百合": [5.0, 1.8, 6.0, 2.2]
}

# 生成带噪声的特征数据
data = []
labels = []
flower_names = list(flower_means.keys())

for label, name in enumerate(flower_names):
    mean = flower_means[name]
    # 为每种花卉生成100个样本，添加少量噪声
    samples = np.random.normal(loc=mean, scale=0.3, size=(100, 4))  # 均值+高斯噪声
    data.extend(samples)
    labels.extend([label] * 100)  # 标签：0-玫瑰，1-郁金香，2-向日葵，3-百合

# 转换为DataFrame，方便查看
df = pd.DataFrame(data, columns=["花瓣长度(cm)", "花瓣宽度(cm)", "花萼长度(cm)", "花萼宽度(cm)"])
df["花卉种类"] = [flower_names[i] for i in labels]
print("模拟数据集前5行：")
print(df.head())
print(f"\n数据集规模：{df.shape[0]}个样本，{df.shape[1] - 1}个特征")

# 2. 数据预处理
X = np.array(data)  # 特征
y = np.array(labels)  # 标签

# 划分训练集（70%）和测试集（30%）
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# 特征标准化
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 标签独热编码（4类→4维向量）
y_train_onehot = to_categorical(y_train, 4)
y_test_onehot = to_categorical(y_test, 4)

# 3. 构建神经网络模型
model = Sequential([
    Dense(32, activation='relu', input_shape=(4,)),  # 输入层+隐藏层1：32个神经元
    Dense(16, activation='relu'),  # 隐藏层2：16个神经元
    Dense(4, activation='softmax')  # 输出层：4个神经元（对应4类花卉）
])

# 编译模型
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# 打印模型结构
print("\n模型结构：")
model.summary()

# 4. 训练模型
history = model.fit(
    X_train_scaled, y_train_onehot,
    epochs=30,
    batch_size=16,
    validation_split=0.1,
    verbose=1
)

# 5. 模型评估
test_loss, test_acc = model.evaluate(X_test_scaled, y_test_onehot, verbose=0)
print(f"\n测试集准确率：{test_acc:.4f}")

# 预测结果
y_pred = np.argmax(model.predict(X_test_scaled), axis=1)

# 分类报告
print("\n分类报告：")
print(classification_report(y_test, y_pred, target_names=flower_names))

# 混淆矩阵可视化
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens',
            xticklabels=flower_names,
            yticklabels=flower_names)
plt.xlabel('预测类别')
plt.ylabel('真实类别')
plt.title('花卉分类混淆矩阵')
plt.show()

# 6. 用新数据进行预测（模拟3个未知样本）
# 新样本特征：[花瓣长度, 花瓣宽度, 花萼长度, 花萼宽度]
new_samples = [
    [4.6, 2.1, 5.2, 2.6],  # 接近玫瑰的特征
    [3.1, 1.4, 3.9, 1.7],  # 接近郁金香的特征
    [5.9, 2.4, 6.8, 2.9]  # 接近向日葵的特征
]

# 预处理新样本（用训练集的scaler标准化）
new_samples_scaled = scaler.transform(new_samples)

# 预测
pred_probs = model.predict(new_samples_scaled)  # 预测概率
pred_labels = np.argmax(pred_probs, axis=1)  # 预测类别索引

# 显示预测结果
print("\n新样本预测结果：")
for i in range(len(new_samples)):
    print(f"样本{i + 1}特征：{new_samples[i]}")
    print(f"预测类别：{flower_names[pred_labels[i]]}")
    print(f"类别概率：{dict(zip(flower_names, pred_probs[i].round(4)))}")
    print("---")

# 7. 可视化训练过程
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='训练损失')
plt.plot(history.history['val_loss'], label='验证损失')
plt.title('训练与验证损失')
plt.xlabel('轮次')
plt.ylabel('损失')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='训练准确率')
plt.plot(history.history['val_accuracy'], label='验证准确率')
plt.title('训练与验证准确率')
plt.xlabel('轮次')
plt.ylabel('准确率')
plt.legend()
plt.tight_layout()
plt.show()
