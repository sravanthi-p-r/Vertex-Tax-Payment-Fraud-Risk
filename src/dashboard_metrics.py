import pandas as pd


def calculate_metrics(df):

    total_transactions = len(df)

    approved = df["approved"].sum()

    fraud = df["fraud_flag"].sum()

    chargebacks = df["chargeback"].sum()

    approval_rate = (
        approved
        /
        total_transactions
    ) * 100

    fraud_rate = (
        fraud
        /
        total_transactions
    ) * 100

    chargeback_rate = (
        chargebacks
        /
        total_transactions
    ) * 100

    metrics = pd.DataFrame({

        "Metric": [

            "Total Transactions",

            "Approval Rate",

            "Fraud Rate",

            "Chargeback Rate"
        ],

        "Value": [

            total_transactions,

            round(
                approval_rate,
                2
            ),

            round(
                fraud_rate,
                2
            ),

            round(
                chargeback_rate,
                2
            )
        ]
    })

    return metrics


if __name__ == "__main__":

    df = pd.read_csv(
        "../data/processed/transactions_features.csv"
    )

    metrics = calculate_metrics(df)

    metrics.to_csv(

        "../outputs/dashboard_metrics.csv",

        index=False
    )

    print(metrics)
