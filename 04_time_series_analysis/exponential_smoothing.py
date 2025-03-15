import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# 샘플 데이터 생성
data = np.cumsum(np.random.randn(100))  # 시계열 데이터
df = pd.Series(data)

# 지수 평활법 모델 학습 및 예측
model = ExponentialSmoothing(df, trend="add", seasonal=None) #seasonal_periods=1
model_fit = model.fit()
forecast = model_fit.forecast(steps=10)

print("예측 결과:", forecast)
