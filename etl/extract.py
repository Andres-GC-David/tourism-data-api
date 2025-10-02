import pandas as pd

def extract(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path, encoding="latin1")
    except UnicodeDecodeError:
        print("⚠️ UTF-8 failed, trying latin1 encoding...")
        df = pd.read_csv(file_path, encoding="latin1")
    return df

if __name__ == "__main__":
    df = extract("../data/hotels.csv")
    print(df.head())
