from functools import wraps
from sklearn.metrics import accuracy_score

def accuracy_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        model = args[0]
        X_test = args[1][0]
        y_test = args[1][1]
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Accuracy: {accuracy}")
        return accuracy
    return wrapper

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

model1 = LogisticRegression()
model1.fit(X_train, y_train)

@accuracy_decorator
def test_accuracy(model, data):
    return model.score(data[0], data[1])

accuracy = test_accuracy(model1, (X_test, y_test))
print(f"Accuracy: {accuracy}")

