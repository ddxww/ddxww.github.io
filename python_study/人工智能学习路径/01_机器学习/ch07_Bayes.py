import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv(
    r"C:\Users\lenovo\Downloads\SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "text"]
)
# print(df.head())
# print(df.shape)
# print(df.isna().sum())
# print(df["label"].value_counts())
df.dropna(inplace=True)
df['target']=df['label'].map({'ham': '0', 'spam': '1'})
X=df[['text']]
y=df['target']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)
print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)


