import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 샘플 데이터 생성
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5])

# 모델 학습
model = LinearRegression()
model.fit(X, y)

# 예측값 생성
y_pred = model.predict(X)

# 시각화
plt.scatter(X, y, color='blue', label="Actual")
plt.plot(X, y_pred, color='red', label="Predicted")
plt.legend()
plt.show()
