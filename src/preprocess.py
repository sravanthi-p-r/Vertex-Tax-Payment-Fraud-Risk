import pandas as pd

df = pd.read_csv(
    "data/synthetic_transactions.csv"
)

print(df.info())

print(df.isnull().sum())

print(df.describe())
