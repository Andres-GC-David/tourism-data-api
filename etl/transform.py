import pandas as pd
import numpy as np

def transform(df: pd.DataFrame) -> pd.DataFrame:
    print("Column names in dataset:", df.columns)

    df = df.rename(columns={
        "Hotel": "name",
        "Region": "region",
        "Score": "rating",
        "Rooms": "rooms"
    })

    df["price_per_night"] = (df["rating"] * 20 + np.random.randint(30, 100, size=len(df))).astype(int)

    df["availability"] = np.random.choice([0, 1], size=len(df))

    df = df[["name", "region", "price_per_night", "availability", "rating", "rooms"]]

    df = df.dropna(subset=["name", "region", "price_per_night"])

    df["region"] = df["region"].str.title()

    return df

if __name__ == "__main__":
    raw = pd.read_csv("../data/hotels.csv")
    clean = transform(raw)
    print(clean.head())
