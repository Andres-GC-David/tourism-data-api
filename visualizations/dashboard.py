import streamlit as st
import pandas as pd
import sqlite3
import os
import plotly.express as px

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "db", "hotels.db")

@st.cache_data
def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM hotels_cleaned", conn)
    conn.close()
    return df

df = load_data()

st.title("Hotels Dashboard 🌴")
st.write("Overview of hotels by region, price and rating")

region_filter = st.sidebar.selectbox("Select region", ["All"] + df["region"].unique().tolist())

if region_filter != "All":
    df = df[df["region"] == region_filter]

st.subheader("Top 10 Hotels by Rating")
st.dataframe(df.sort_values("rating", ascending=False).head(10))

st.subheader("Average Price per Region")
avg_price = df.groupby("region")["price_per_night"].mean().reset_index()

fig = px.bar(avg_price, x="region", y="price_per_night", 
             color="price_per_night", 
             color_continuous_scale="Viridis",
             labels={"price_per_night":"Avg Price ($)", "region":"Region"})
st.plotly_chart(fig)

st.subheader("Average Availability by Region")
availability = df.groupby("region")["availability"].mean() * 100
st.bar_chart(availability)
