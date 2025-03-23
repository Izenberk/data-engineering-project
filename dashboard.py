import streamlit as st
import pandas as pd
import psycopg2

st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

st.title("📦 E-Commerce Transactions Dashboard")

# Connect to PostgreSQL
@st.cache_resource
def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="mydatabase",
        user="Izenberk",
        password="Pass1234"
   )

conn = get_connection()

# Load data
df = pd.read_sql("SELECT * FROM public.daily_sales", conn)


st.subheader("Raw Data Preview")
st.dataframe(df)


st.subheader("Metrics")

# Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Get the latest date
latest_order_date = df["order_date"].max()

# Get the sales amount for the latest date
latest_sales = df.loc[df["order_date"] == latest_order_date, "total_sales"].sum()

# Display metrics
st.metric("Latest Order Date", str(latest_order_date.date()))
st.metric("Total Sales on Latest Date", f"${latest_sales:.2f}")

st.subheader("📈 Daily Sales Over Time")

# Sort by date
df = df.sort_values("order_date")

# Set order_date as index for the line chart
df_chart = df.set_index("order_date")[["total_sales"]]

# Line chart
st.line_chart(df_chart)