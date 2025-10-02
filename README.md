# 🏨 Tourism ETL + API 

## 📌 About this project
This project was created as a **portfolio piece** to showcase my skills in **Data Engineering, Data Analytics, and Backend Development**.  

The idea is to simulate a **real-world tourism analytics system**:  
- Hotels are extracted from a raw dataset.  
- Data is **cleaned, enriched, and transformed** (adding nightly prices and availability).  
- A **REST API (FastAPI)** serves the cleaned data and exposes useful analytics endpoints.  

👉 The goal is to demonstrate how I can **design, implement, and deploy data-driven systems** that solve practical business problems.

---

## 🚀 Why is this important?
Hotels and tourism operators need **data systems** to answer questions such as:  
- What is the **average nightly price** in a region?  
- Which are the **top-rated hotels**?  
- What is the **availability rate**?  
- How are **prices distributed** across regions?  

This project shows that I can:  
- Build a **full ETL pipeline** (Extract → Transform → Load).  
- Simulate **realistic business metrics** (price, availability).  
- Deliver insights through a **clean, well-designed API**.  
- Make **data engineering + backend development** work together in a practical context.  

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **Pandas** → data cleaning & feature engineering
- **SQLite** → lightweight relational database
- **FastAPI** → REST API framework
- **Uvicorn** → ASGI server

---

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

## ⚙️ How to Run

### 1. Clone the repository

git clone https://github.com/Andres-GC-David/tourism-data-api.git
cd tourism-etl-api

### 2. Create and activate virtual environment

python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Running the ETL Pipeline

The ETL (Extract, Transform, Load) pipeline cleans the raw data and loads it into a local SQLite database.

python etl/pipeline.py

This script performs the following:

Extracts raw hotel data.

Transforms it by cleaning fields and feature engineering (e.g., simulating price_per_night and availability).

Loads the cleaned data into db/hotels.db within the hotels_cleaned table.

### 5. Running the API

uvicorn api.main:app --reload

👉 API docs available at http://127.0.0.1:8000/docs

### 6. Endpoints Overview

- Get hotels
GET /hotels?limit=5


Returns first N hotels.

- Average price per region
GET /average-price?region=Guanacaste


Returns the average nightly price in Guanacaste.
⚠️ Note: price_per_night is simulated, since the original dataset did not include it.

- Top hotels
GET /top-hotels?region=Guanacaste&limit=3


Returns top-rated hotels in a region.

- Availability
GET /availability?region=San Jose


Returns the % of available hotels in San José.

- Price range
GET /price-range?region=Guanacaste


Returns min, max, and avg prices for a region.

- Stats
GET /stats


Returns:

Total number of hotels

Average price (simulated)

Average rating

Hotel counts per region