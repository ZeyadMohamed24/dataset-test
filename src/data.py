import os
import pandas as pd
from sklearn.datasets import fetch_openml

RAW_DATA_PATH = os.path.join("data", "raw", "iris.csv")

def download_and_save(path=RAW_DATA_PATH):
    print("Downloading Iris dataset (OpenML ID: 61)...")
    data = fetch_openml(data_id=61, as_frame=True)  # Iris dataset
    df = data.frame  # This is the actual DataFrame

    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)

    print(f"Dataset saved to {path}")
    return df

df = download_and_save()
print(df.head())