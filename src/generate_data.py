import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

np.random.seed(42)

N_TRANSACTIONS = 100000


def generate_transactions():

    transactions = []

    for txn_id in range(N_TRANSACTIONS):

        customer_id = np.random.randint(
            10000,
            50000
        )

        merchant_id = np.random.randint(
            1000,
            2000
        )

        amount = round(
            np.random.exponential(75),
            2
        )

        risk_score = np.random.beta(
            2,
            8
        )

        country = np.random.choice(
            ["US", "CA", "GB", "IN", "BR"],
            p=[0.65, 0.10, 0.10, 0.10, 0.05]
        )

        device_type = np.random.choice(
            ["Mobile", "Desktop", "Tablet"]
        )

        is_new_customer = np.random.choice(
            [0, 1],
            p=[0.8, 0.2]
        )

        approved = (
            1
            if risk_score < 0.70
            else 0
        )

        fraud_probability = risk_score * 0.8

        fraud_flag = np.random.binomial(
            1,
            fraud_probability
        )

        chargeback = (
            1
            if fraud_flag == 1
            and approved == 1
            else 0
        )

        transactions.append([
            txn_id,
            customer_id,
            merchant_id,
            amount,
            risk_score,
            country,
            device_type,
            is_new_customer,
            approved,
            fraud_flag,
            chargeback
        ])

    columns = [
        "transaction_id",
        "customer_id",
        "merchant_id",
        "amount",
        "risk_score",
        "country",
        "device_type",
        "is_new_customer",
        "approved",
        "fraud_flag",
        "chargeback"
    ]

    return pd.DataFrame(
        transactions,
        columns=columns
    )


if __name__ == "__main__":

    df = generate_transactions()

    df.to_csv(
        "../data/synthetic_transactions.csv",
        index=False
    )

    print(df.head())
    print(df.shape)
