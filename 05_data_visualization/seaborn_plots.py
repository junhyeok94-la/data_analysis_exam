import seaborn as sns
import matplotlib.pyplot as plt

# 샘플 데이터 로드
tips = sns.load_dataset("tips")

# 히스토그램
sns.histplot(tips['total_bill'], kde=True)
plt.show()

# 산점도
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.show()
