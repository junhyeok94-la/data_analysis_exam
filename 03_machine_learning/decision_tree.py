from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# 데이터 로드
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# 모델 학습
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# 정확도 출력
accuracy = clf.score(X_test, y_test)
print("Decision Tree Accuracy:", accuracy)
