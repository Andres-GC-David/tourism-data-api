from fastapi import FastAPI
import sqlite3
import pandas as pd
import os

app = FastAPI(title="Tourism Hotels API", version="1.0")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "db", "hotels.db")

def query_db(sql: str):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/hotels")
def get_hotels(limit: int = 10):
    df = query_db(f"SELECT * FROM hotels_cleaned LIMIT {limit}")
    return df.to_dict(orient="records")

@app.get("/average-price")
def average_price(region: str = None):
    if region:
        df = query_db(
            f"SELECT region, AVG(price_per_night) as avg_price "
            f"FROM hotels_cleaned WHERE region='{region}' GROUP BY region"
        )
    else:
        df = query_db("SELECT AVG(price_per_night) as avg_price FROM hotels_cleaned")
    return df.to_dict(orient="records")

@app.get("/top-hotels")
def top_hotels(region: str = None, limit: int = 5):
    query = "SELECT name, region, rating, price_per_night FROM hotels_cleaned"
    if region:
        query += f" WHERE region='{region}'"
    query += " ORDER BY rating DESC LIMIT {limit}".format(limit=limit)
    df = query_db(query)
    return df.to_dict(orient="records")

@app.get("/availability")
def availability(region: str = None):
    query = "SELECT region, AVG(availability) * 100 as availability_rate FROM hotels_cleaned"
    if region:
        query += f" WHERE region='{region}'"
    query += " GROUP BY region"
    df = query_db(query)
    return df.to_dict(orient="records")

@app.get("/price-range")
def price_range(region: str):
    df = query_db(
        f"SELECT region, MIN(price_per_night) as min_price, "
        f"MAX(price_per_night) as max_price, "
        f"AVG(price_per_night) as avg_price "
        f"FROM hotels_cleaned WHERE region='{region}' GROUP BY region"
    )
    return df.to_dict(orient="records")

@app.get("/stats")
def stats():
    df = query_db("SELECT * FROM hotels_cleaned")

    return {
        "total_hotels": len(df),
        "avg_price": round(df["price_per_night"].mean(), 2),
        "avg_rating": round(df["rating"].mean(), 2),
        "region_counts": df["region"].value_counts().to_dict(),
    }
