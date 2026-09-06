import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,MinMaxScaler

def get_data():
    data=pd.read_csv('train1.csv')
    X=data.drop(columns=['label'])
    y=data['label']
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)
    scaler=MinMaxScaler()
    scaler.fit(X_train)
    X_train=scaler.transform(X_train)
    X_test=scaler.transform(X_test)
    #转化为ndarray
    y_train=y_train.values
    y_test=y_test.values

    return X_train,X_test,y_train,y_test
