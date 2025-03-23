import pandas as pd
from sqlalchemy import create_engine


# Database connection settings
DB_USER = "Izenberk"
DB_PASSWORD = "Pass1234"
DB_HOST = "postgres"
DB_PORT = "5432"
DB_NAME = "mydatabase"

# Define PostgreSQL connection string
db_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(db_url)

# LOAD CSV data
csv_file = "/opt/airflow/dags/data/ecommerce_transactions_new.csv"
df = pd.read_csv(csv_file)

# Data Cleaning
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df = df.drop_duplicates()
df = df[df["quantity"] > 0]

# Load into PostgreSQL
df.to_sql("ecommerce_transactions", engine, if_exists="append", index=False)

print("✅ ETL process completed. Data loaded into PostgreSQL.")