import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier

def report(df):
    y_test, predictions = process(df)
    return Report(
        dt_accuracy=accuracy_score(y_test, predictions[0]),
        dt_report=classification_report(y_test, predictions[0]),
        rf_accuracy=accuracy_score(y_test, predictions[1]),
        rf_report=classification_report(y_test, predictions[1]),
        xgb_accuracy=accuracy_score(y_test, predictions[2]),
        xgb_report=classification_report(y_test, predictions[2])
    )

def process(df):

    # Removendo registros com valores faltando
    df = df.dropna()

    # Indicadores de jogadas agressivas
    X = df[["hits", "takeaways", "faceOffWinPercentage"]]

    # Indicador de vitória
    y = df["won"]

    # Dividindo o dataset em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # DecisionTreeClassifier
    print('Processando DecisionTreeClassifier...')
    dt_classifier = DecisionTreeClassifier(random_state=42)
    dt_classifier.fit(X_train, y_train)
    dt_prediction = dt_classifier.predict(X_test)

    # RandomForestClassifier
    print('Processando RandomForestClassifier...')
    rf_classifier = RandomForestClassifier(random_state=42)
    rf_classifier.fit(X_train, y_train)
    rf_prediction = rf_classifier.predict(X_test)

    # XGBClassifier
    print('Processando XGBClassifier...')
    xgb_classifier = XGBClassifier(random_state=42)
    xgb_classifier.fit(X_train, y_train)
    xgb_prediction = xgb_classifier.predict(X_test)

    print("DecisionTreeClassifier:")
    print("Precisão:", accuracy_score(y_test, dt_prediction))
    print("Relatório:\n", classification_report(y_test, dt_prediction))

    print("RandomForestClassifier:")
    print("Precisão:", accuracy_score(y_test, rf_prediction))
    print("Relatório:\n", classification_report(y_test, rf_prediction))

    print("XBGClassifier:")
    print("Precisão:", accuracy_score(y_test, xgb_prediction))
    print("Relatório:\n", classification_report(y_test, xgb_prediction))

    return y_test, [dt_prediction, rf_prediction, xgb_prediction]


class Report:
    dt_accuracy: str
    dt_report: str
    rf_accuracy: str
    rf_report: str
    xgb_accuracy: str
    xgb_report: str

    def __init__(
        self,
        dt_accuracy,
        dt_report,
        rf_accuracy,
        rf_report,
        xgb_accuracy,
        xgb_report,
    ):
        self.dt_accuracy = dt_accuracy
        self.dt_report = dt_report
        self.rf_accuracy = rf_accuracy
        self.rf_report = rf_report
        self.xgb_accuracy = xgb_accuracy
        self.xgb_report = xgb_report
