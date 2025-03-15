import matplotlib.pyplot as plt
import numpy as np

# 샘플 데이터
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 선 그래프
plt.plot(x, y, label="Sine Wave")
plt.legend()
plt.show()

# 바 그래프
categories = ["A", "B", "C", "D"]
values = [3, 7, 1, 8]

plt.bar(categories, values, color="skyblue")
plt.show()
