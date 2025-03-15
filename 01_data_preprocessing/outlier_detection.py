import pandas as pd

# 샘플 데이터 생성 (이상치 포함)
data = {'value': [10, 12, 14, 15, 100, 17, 18, 200, 20, 22]}
df = pd.DataFrame(data)

# IQR 방법으로 이상치 탐지
Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['value'] < lower_bound) | (df['value'] > upper_bound)]
df_cleaned = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]

print("이상치 데이터:", outliers)
print("이상치 제거 후 데이터:", df_cleaned)
