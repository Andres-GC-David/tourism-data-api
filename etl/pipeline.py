import os
from extract import extract
from transform import transform
from load import load

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "hotel_100_2022.csv")
DB_PATH = os.path.join(BASE_DIR, "db", "hotels.db")

def run_pipeline():
    print("Extracting data from:", DATA_PATH)
    raw = extract(DATA_PATH)

    print("Raw shape:", raw.shape)
    clean = transform(raw)
    print("Clean shape:", clean.shape)
    print(clean.head())

    load(clean, DB_PATH)
    print("Pipeline executed successfully. Data saved to", DB_PATH)

if __name__ == "__main__":
    run_pipeline()
