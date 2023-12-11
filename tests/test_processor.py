import pandas as pd
from processor import process
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

threshold = 0.56

def test_predictions_within_threshold():
    test_data = load_test_data()
    y_test, predictions = process(test_data)

    assert all(accuracy_score(y_test, prediction) >= threshold for prediction in predictions)

def test_models_below_expectations():
    test_data = load_test_data()

    test_data = test_data.dropna()
    X = test_data[["hits", "takeaways", "faceOffWinPercentage"]]
    y = test_data["won"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    lr_classifier = LogisticRegression(random_state=42)
    lr_classifier.fit(X_train, y_train)
    lr_prediction = lr_classifier.predict(X_test)

    svm_classifier = SVC(random_state=42)
    svm_classifier.fit(X_train, y_train)
    svm_prediction = svm_classifier.predict(X_test)
    
    assert not(accuracy_score(y_test, lr_prediction) >= threshold)
    assert not(accuracy_score(y_test, svm_prediction) >= threshold)


def load_test_data():
    test_data = pd.read_csv('tests/game_teams_stats.csv')
    return pd.DataFrame(test_data)