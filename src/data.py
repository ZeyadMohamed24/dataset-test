from sklearn.datasets import fetch_openml
import os
import pandas as pd

RAW_DATA_PATH = os.path.join("data", "raw", "credit_g.csv")


def download_and_save(path=RAW_DATA_PATH):
    print("Downloading German Credit dataset (version 2)...")
    data = fetch_openml(name="credit-g", version=2, as_frame=True)
    df = data.frame

    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)

    print(f"Dataset saved to {path}")
    return df


df = pd.read_csv(r"E:\FCAI\Dataset Experiment\data\raw\credit_g.csv")
# print("Description: ",df.describe())  # statistics for numeric columns
# print(df.describe(include="object"))  # stats for categorical columns
# print(df.nunique())  # number of unique values per column
# print(df.isnull().sum())  # count missing values
# print(df.dtypes)

# print(df[df["class"] == "good"].head())
# df.to_json("data.json")
# df.to_json(df)

# json_str = df[df["class"] == "good"].head().to_json(orient="records")
# print(json_str)


json_str = df[df["class"] == "good"].head().to_json(orient="records", indent=2)
print(json_str)
