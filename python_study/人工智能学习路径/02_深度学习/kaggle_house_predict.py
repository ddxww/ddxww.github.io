import torch
import torch.nn as nn
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from torch.utils.data import TensorDataset,DataLoader


# 创建数据集
def create_dataset():
    # 1.从文件读取数据
    data=pd.read_csv('house_prices.csv')

    # 2.去除无关列
    data.drop(columns=['Id'],inplace=True)

    # 3.划分特征和目标
    X=data.drop(columns=['SalePrice'])
    y=data['SalePrice']

    # 4.划分训练集和测试集
    x_train,x_test,y_train,y_test=train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # 5.特征工程
    # 5.1按照特征数据类型划分成数值型和类别型
    numerical_features=X.select_dtypes(
        exclude=['object']
    ).columns

    categorical_features=X.select_dtypes(
        include=['object']
    ).columns

    # 5.2.1数值型特征
    numerical_transformer=Pipeline(
        steps=[
            (
                'fillna',
                SimpleImputer(strategy='mean')
            ),
            (
                'std',
                StandardScaler()
            )
        ]
    )

    # 5.2.2类别型特征
    categorical_transformer=Pipeline(
        steps=[
            (
                'fillna',
                SimpleImputer(
                    strategy='constant',
                    fill_value='NaN'
                )
            ),
            (
                'onehot',
                OneHotEncoder(
                    handle_unknown='ignore'
                )
            )
        ]
    )

    # 5.2.3组合列转换器
    transformer=ColumnTransformer(
        transformers=[
            (
                'num',
                numerical_transformer,
                numerical_features
            ),
            (
                'cat',
                categorical_transformer,
                categorical_features
            )
        ]
    )

    # 5.3进行特征转换
    x_train=transformer.fit_transform(x_train)
    x_test=transformer.transform(x_test)

    x_train=pd.DataFrame(
        x_train.toarray(),
        columns=transformer.get_feature_names_out()
    )

    x_test=pd.DataFrame(
        x_test.toarray(),
        columns=transformer.get_feature_names_out()
    )

    # 6.构建Tensor数据集
    train_dataset=TensorDataset(
        torch.tensor(x_train.values).float(),
        torch.tensor(y_train.values).float()
    )

    test_dataset=TensorDataset(
        torch.tensor(x_test.values).float(),
        torch.tensor(y_test.values).float()
    )

    # 多返回一个训练好的列转换器
    return (
        train_dataset,
        test_dataset,
        x_train.shape[1],
        transformer
    )


# 加载数据
train_dataset,test_dataset,feature_num,transformer=create_dataset()


# 创建模型
model=nn.Sequential(
    nn.Linear(feature_num,128),
    nn.BatchNorm1d(128),
    nn.ReLU(),
    nn.Dropout(0.2),
    nn.Linear(128,1)
)


# 自定义损失函数
def log_rmse(y_pred,target):
    y_pred=torch.clamp(
        y_pred,
        1,
        float('inf')
    )

    mse=nn.MSELoss()

    return torch.sqrt(
        mse(
            torch.log(y_pred),
            torch.log(target)
        )
    )


# 模型训练
def train_test(
    model,
    train_dataset,
    test_dataset,
    lr,
    epochs,
    batch_size,
    device
):
    # 参数初始化
    def init_params(layer):
        if isinstance(layer,nn.Linear):
            nn.init.xavier_normal_(layer.weight)

    model.apply(init_params)

    # 将模型加载到设备
    model=model.to(device)

    # 定义优化器
    optimizer=torch.optim.Adam(
        model.parameters(),
        lr=lr
    )

    train_loss_list=[]
    test_loss_list=[]

    for epoch in range(epochs):
        model.train()

        train_loader=DataLoader(
            train_dataset,
            batch_size=batch_size,
            shuffle=True
        )

        train_loss_total=0.0

        # 按批次训练
        for batch_idx,(X,y) in enumerate(train_loader):
            X,y=X.to(device),y.to(device)

            # 前向传播
            y_pred=model(X)

            # 计算损失
            loss_value=log_rmse(
                y_pred.squeeze(),
                y
            )

            # 反向传播
            loss_value.backward()

            # 更新参数
            optimizer.step()

            # 梯度清零
            optimizer.zero_grad()

            # 使用item转换为普通float
            train_loss_total+=(
                loss_value.item()*X.shape[0]
            )

        this_train_loss=(
            train_loss_total/
            len(train_dataset)
        )

        train_loss_list.append(
            this_train_loss
        )

        # 测试
        model.eval()

        test_loader=DataLoader(
            test_dataset,
            batch_size=batch_size,
            shuffle=True
        )

        test_loss_total=0.0

        with torch.no_grad():
            for X,y in test_loader:
                X,y=X.to(device),y.to(device)

                y_pred=model(X)

                loss_value=log_rmse(
                    y_pred.squeeze(),
                    y
                )

                test_loss_total+=(
                    loss_value.item()*X.shape[0]
                )

        this_test_loss=(
            test_loss_total/
            len(test_dataset)
        )

        test_loss_list.append(
            this_test_loss
        )

        print(
            f"epoch:{epoch+1},"
            f"train_loss:{this_train_loss},"
            f"test_loss:{this_test_loss}"
        )

    return train_loss_list,test_loss_list


device=torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

# 超参数，保持你的设置
lr=0.08
epochs=200
batch_size=64

train_loss_list,test_loss_list=train_test(
    model,
    train_dataset,
    test_dataset,
    lr,
    epochs,
    batch_size,
    device
)


# 绘制损失曲线
plt.plot(
    train_loss_list,
    'r-',
    label='train loss',
    linewidth=3
)

plt.plot(
    test_loss_list,
    'k--',
    label='test loss',
    linewidth=2
)

plt.legend()
plt.show()


# 使用模型预测官方测试集
def predict(
    model,
    transformer,
    file_path,
    device,
    batch_size
):
    # 1.读取测试数据
    data=pd.read_csv(file_path)

    # 2.保存Id
    test_id=data['Id'].copy()

    # 3.删除Id
    data.drop(columns=['Id'],inplace=True)

    # 4.使用训练集拟合好的转换器
    data=transformer.transform(data)

    # 5.稀疏矩阵转换为普通数组
    data=data.toarray()

    # 6.转换为Tensor数据集
    data=torch.tensor(data).float()

    predict_dataset=TensorDataset(data)

    predict_loader=DataLoader(
        predict_dataset,
        batch_size=batch_size,
        shuffle=False
    )

    # 7.预测
    model.eval()
    result=[]

    with torch.no_grad():
        for (X,) in predict_loader:
            X=X.to(device)

            y_pred=model(X).squeeze()

            # 防止出现负房价
            y_pred=torch.clamp(
                y_pred,
                min=1
            )

            result.extend(
                y_pred.cpu().numpy()
            )

    # 8.生成结果表
    submission=pd.DataFrame({
        'Id':test_id,
        'SalePrice':result
    })

    return submission


submission=predict(
    model,
    transformer,
    r'D:\机器学习data\lx1\test.csv',
    device,
    batch_size
)

submission.to_csv(
    r'D:\机器学习data\lx1\submission.csv',
    index=False
)

print(submission.head())
print('预测完成')