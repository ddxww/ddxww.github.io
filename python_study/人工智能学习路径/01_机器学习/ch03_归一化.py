import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
X = np.array([[10],[20],[30],[40],[50]])
scaler=MinMaxScaler()
X_scaled=scaler.fit_transform(X)
print(X_scaled)