import pandas as pd

data = pd.read_csv('data.csv')
print(data.dtypes)
print(data.isna().sum())