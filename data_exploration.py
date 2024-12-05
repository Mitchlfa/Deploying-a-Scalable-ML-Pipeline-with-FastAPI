import pandas as pd

data = pd.read_csv('data/census.csv')

print(data.head())
print(data.isnull().sum())
print(data.info())
print(data.describe())
print(data['salary'].unique())
print(data.duplicated().sum())