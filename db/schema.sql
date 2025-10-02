CREATE TABLE IF NOT EXISTS hotels_cleaned (
    hotel_id TEXT PRIMARY KEY,
    name TEXT,
    province TEXT,
    price_per_night NUMERIC,
    availability INTEGER,
    rating NUMERIC,
    last_updated DATE DEFAULT CURRENT_DATE
);