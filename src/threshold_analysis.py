import pandas as pd
import numpy as np

from sklearn.metrics import (
    confusion_matrix
)


def evaluate_threshold(
    actual,
    probabilities,
    threshold
):

    predicted = np.where(
        probabilities >= threshold,
        1,
        0
    )

    tn, fp, fn, tp = confusion_matrix(
        actual,
        predicted
    ).ravel()

    approval_rate = (
        (tn + fn)
        /
        len(actual)
    ) * 100

    fraud_capture_rate = (
        tp
        /
        (tp + fn)
    ) * 100

    false_positive_rate = (
        fp
        /
        (fp + tn)
    ) * 100

    return [

        threshold,

        approval_rate,

        fraud_capture_rate,

        false_positive_rate
    ]


if __name__ == "__main__":

    df = pd.read_csv(
        "../outputs/model_results/model_predictions.csv"
    )

    thresholds = np.arange(
        0.1,
        1.0,
        0.1
    )

    results = []

    for threshold in thresholds:

        results.append(

            evaluate_threshold(

                df["actual_fraud"],

                df["fraud_probability"],

                threshold
            )
        )

    output = pd.DataFrame(

        results,

        columns=[

            "Threshold",

            "Approval_Rate",

            "Fraud_Capture_Rate",

            "False_Positive_Rate"
        ]
    )

    output.to_csv(

        "../outputs/model_results/threshold_results.csv",

        index=False
    )

    print(output)
