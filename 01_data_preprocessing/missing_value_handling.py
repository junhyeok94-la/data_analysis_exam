import pandas as pd
import numpy as np

# 샘플 데이터 생성 (결측치 포함)
data = {'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 2, 3, 4, 5],
        'C': [1, np.nan, np.nan, 4, 5]}

df = pd.DataFrame(data)

# 결측치 처리 방법
df_filled_mean = df.fillna(df.mean())  # 평균값으로 채우기
df_filled_median = df.fillna(df.median())  # 중앙값으로 채우기
df_dropped = df.dropna()  # 결측치가 있는 행 삭제

print("결측치 처리 전:\n", df)
print("평균값으로 채운 후:\n", df_filled_mean)
print("중앙값으로 채운 후:\n", df_filled_median)
print("결측치가 있는 행 삭제 후:\n", df_dropped)
