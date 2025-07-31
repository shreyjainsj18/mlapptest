import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Train a simple model (only if run as script)
if __name__ == "__main__":
    iris = load_iris()
    X, y = iris.data, iris.target
    clf = RandomForestClassifier()
    clf.fit(X, y)
    joblib.dump(clf, "iris_model.pkl")
