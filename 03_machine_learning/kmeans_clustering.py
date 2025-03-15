import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 샘플 데이터 생성
X = np.random.rand(100, 2)

# K-Means 클러스터링
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# 결과 시각화
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis', alpha=0.6)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='red', marker='x', label="Centers")
plt.legend()
plt.show()
