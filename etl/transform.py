import pandas as pd
import numpy as np

REGION_MULTIPLIER = {
    "Europe": 1.2,
    "North America": 1.2,
    "Southeast Asia": 1.0,
    "Africa": 0.9,
    "Middle East": 1.1,
    "Latin America": 1.0,
    "Caribbean": 1.3,
    "Oceania": 1.2,
    "Asia": 1.0
}

THEME_MULTIPLIER = {
    "Countryside": 1.0,
    "Island": 1.2,
    "Boutique": 1.1,
    "Nature": 1.0,
    "Contemporary": 1.05,
    "Palace": 1.2,
    "Safari": 1.1,
    "Beachfront": 1.2,
    "Coastal": 1.1,
    "Manor": 1.1,
    "Lodge": 1.05,
    "Mediterranean": 1.2
}

def transform(df: pd.DataFrame) -> pd.DataFrame:
    print("Column names in dataset:", df.columns)

    df = df.rename(columns={
        "Hotel": "name",
        "Region": "region",
        "Score": "rating",
        "Rooms": "rooms",
        "Theme": "theme"
    })

    df["theme"] = df["theme"].fillna("Countryside")

    base_price = df["rating"] * 50

    room_factor = 100 / (df["rooms"] + 20)

    region_factor = df["region"].map(lambda x: REGION_MULTIPLIER.get(x, 1.0))

    theme_factor = df["theme"].map(lambda x: THEME_MULTIPLIER.get(x, 1.0))

    category_factor = np.random.choice([0.3, 0.5, 1.0, 1.5], size=len(df), p=[0.3,0.4,0.2,0.1])

    df["price_per_night"] = ((base_price + room_factor * 50) * region_factor * theme_factor * category_factor *np.random.uniform(0.9, 1.1, size=len(df))).round(2)

    df["availability"] = np.random.choice([0, 1], size=len(df))

    df = df[["name", "region", "price_per_night", "availability", "rating", "rooms"]]

    df = df.dropna(subset=["name", "region", "price_per_night"])

    df["region"] = df["region"].str.title()

    return df

if __name__ == "__main__":
    raw = pd.read_csv("../data/hotels.csv")
    clean = transform(raw)
    print(clean.head())
