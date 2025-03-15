import pandas as pd
import numpy as np

# 샘플 데이터 생성
data = {
    'X': np.random.randint(1, 100, 50),
    'Y': np.random.randint(1, 100, 50)
}

df = pd.DataFrame(data)

# 상관관계 분석
correlation = df.corr()
print("상관계수 행렬:\n", correlation)
