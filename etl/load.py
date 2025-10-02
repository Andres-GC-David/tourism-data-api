import sqlite3
import pandas as pd

def load(df: pd.DataFrame, db_path="../db/hotels.db"):
    conn = sqlite3.connect(db_path)
    df.to_sql("hotels_cleaned", conn, if_exists="replace", index=False)
    conn.close()

if __name__ == "__main__":
    df = pd.read_csv("../data/hotels_cleaned.csv")
    load(df)
    print("Data loaded into DB!")
