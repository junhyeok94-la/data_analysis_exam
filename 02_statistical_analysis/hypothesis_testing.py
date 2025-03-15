import scipy.stats as stats
import numpy as np

# 샘플 데이터 생성
group1 = np.random.normal(50, 10, 30)  # 평균 50, 표준편차 10
group2 = np.random.normal(55, 10, 30)  # 평균 55, 표준편차 10

# 독립표본 t-검정 수행
t_stat, p_value = stats.ttest_ind(group1, group2)

print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("귀무가설 기각: 두 그룹의 평균 차이가 통계적으로 유의함")
else:
    print("귀무가설 채택: 두 그룹의 평균 차이가 유의하지 않음")
