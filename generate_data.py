import pandas as pd
import random

data = []

for i in range(1, 10001):
    data.append([
        i,
        random.randint(100, 500),
        random.randint(1000, 100000),
        random.choice(["CREDIT", "DEBIT"]),
        random.choice(["SUCCESS", "SUCCESS", "SUCCESS", "FAILED"])
    ])

df = pd.DataFrame(
    data,
    columns=[
        "transaction_id",
        "user_id",
        "amount",
        "transaction_type",
        "status"
    ]
)

df.to_csv("data/transactions_large.csv", index=False)

print("Generated 10000 transactions successfully!")