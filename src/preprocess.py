import pandas as pd


def load_data(path):

    return pd.read_csv(path)


def validate_dataset(df):

    print("Shape")

    print(df.shape)

    print("\nMissing Values")

    print(df.isnull().sum())

    print("\nDuplicates")

    print(df.duplicated().sum())

    print("\nSummary")

    print(df.describe())


if __name__ == "__main__":

    df = load_data(
        "../data/synthetic_transactions.csv"
    )

    validate_dataset(df)
