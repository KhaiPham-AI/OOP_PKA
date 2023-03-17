def performance_logger(model):
    def decorator(func):
        def wrapper(*args, **kwargs):
            dataset = func(*args, **kwargs)
            X, y = dataset
            accuracy = model.score(X, y)
            print(f"{model.__class__.__name__} accuracy on {func.__name__}: {accuracy}")
            return dataset
        return wrapper
    return decorator

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)

import pandas as pd
@performance_logger(model)
def load_titanic_dataset():
    titanic = pd.read_csv('titanic.csv')
    X = titanic.drop(columns=['Survived'])
    y = titanic['Survived']
    return X, y

@performance_logger(model)
def load_iris_dataset():
    X = X_test
    y = y_test
    return X, y

load_titanic_dataset()
load_iris_dataset()