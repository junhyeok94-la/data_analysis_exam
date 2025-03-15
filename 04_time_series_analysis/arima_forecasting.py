import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

# 샘플 시계열 데이터 생성
data = np.cumsum(np.random.randn(100))  # 누적합으로 시계열 데이터 생성
df = pd.Series(data)

# ARIMA 모델 학습 및 예측
model = ARIMA(df, order=(2, 1, 2))
model_fit = model.fit()
forecast = model_fit.forecast(steps=10)

print("예측 결과:", forecast)
