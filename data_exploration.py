import pandas as pd
from ml.data import process_data

data = pd.read_csv('data/census.csv')

print(data.head())
print(data.isnull().sum())
print(data.info())
print(data.describe())
print(data['salary'].unique())
print(data.duplicated().sum())

# Handle missing values in categorical columns
data['workclass'].fillna(data['workclass'].mode()[0], inplace=True)
data['occupation'].fillna(data['occupation'].mode()[0], inplace=True)
data['native-country'].fillna(data['native-country'].mode()[0], inplace=True)

# Define the categorical features and label column
categorical_features = [
    "workclass", "education", "marital-status", "occupation", "relationship",
    "race", "sex", "native-country"
]
label = "salary"

# Process the data using the process_data function from ml/data.py
X_train, y_train, encoder, lb = process_data(
    data, categorical_features=categorical_features, label=label, training=True
)

# Print some outputs to confirm the processing
print(f"\nProcessed feature matrix X_train: {X_train.shape}")
print(f"Processed label vector y_train: {y_train.shape}")
