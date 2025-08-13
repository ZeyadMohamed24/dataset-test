from sklearn.datasets import fetch_openml
import os

RAW_DATA_PATH = os.path.join("data", "raw", "credit_g.csv")

def download_and_save(path=RAW_DATA_PATH):
    print("Downloading German Credit dataset (version 2)...")
    data = fetch_openml(name="credit-g", version=2, as_frame=True)
    df = data.frame

    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)

    print(f"Dataset saved to {path}")
    return df

df = download_and_save()
print(df)

