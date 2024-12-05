from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model, compute_model_metrics
import numpy as np


# Test if train_model function returns a model of type RandomForestClassifier
def test_train_model():
    X_train = np.array([[0, 1], [1, 0], [0, 0], [1, 1]])  # Sample training data
    y_train = np.array([0, 1, 0, 1])  # Sample labels
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier), "Model is not of type RandomForestClassifier"


# Test if the model uses the expected algorithm (RandomForestClassifier)
def test_model_algorithm():
    X_train = np.array([[0, 1], [1, 0], [0, 0], [1, 1]])  # Sample training data
    y_train = np.array([0, 1, 0, 1])  # Sample labels
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier), "Model is not a RandomForestClassifier"


# Test if compute_model_metrics returns the expected values
def test_compute_model_metrics():
    y_test = np.array([0, 1, 0, 1])  # Sample true labels
    preds = np.array([0, 1, 0, 0])  # Sample predictions
    precision, recall, fbeta = compute_model_metrics(y_test, preds)
    assert isinstance(precision, float), "Precision is not a float"
    assert isinstance(recall, float), "Recall is not a float"
    assert isinstance(fbeta, float), "Fbeta is not a float"
    assert precision >= 0 and precision <= 1, "Precision is out of range"
    assert recall >= 0 and recall <= 1, "Recall is out of range"
    assert fbeta >= 0 and fbeta <= 1, "Fbeta is out of range"
