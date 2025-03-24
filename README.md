# 📦 data-engineering-project

## 🚀 End-to-End Data Engineering Pipeline with Airflow, dbt, PostgreSQL & Streamlit

This project demonstrates a complete batch data pipeline using **Apache Airflow**, **dbt**, and **PostgreSQL** for backend processing, with a front-end dashboard built in **Streamlit** for visualization.

It extracts E-commerce transactional data, loads it into PostgreSQL, transforms it using dbt models, and displays the results via an interactive dashboard.

---

## 🗺️ Project Architecture
                                ┌─────────────────────────┐
                                │      Data Sources       │
                                │   • CSV files (local)   │
                                └───────────┬─────────────┘
                                            │
                                            ▼
                                ┌─────────────────────────┐
                                │     Extraction Layer    │
                                │  (Python scripts via    │
                                │   Airflow DAGs)         │
                                └───────────┬─────────────┘
                                            │
                                            ▼
                                ┌─────────────────────────┐
                                │   Staging Layer (Raw)   │
                                │    PostgreSQL Database  │
                                └───────────┬─────────────┘
                                            │
                                            ▼
                                ┌─────────────────────────┐
                                │  Transformation Layer   │
                                │        (dbt Core)       │
                                └───────────┬─────────────┘
                                            │
                                            ▼
                                ┌─────────────────────────┐
                                │  Analytics Layer (DB)   │
                                │  • Cleaned Tables       │
                                │  • Aggregated Tables    │
                                └───────────┬─────────────┘
                                            │
                                            ▼
                                ┌─────────────────────────┐
                                │  Visualization Layer    │
                                │      (Streamlit App)    │
                                └─────────────────────────┘


---

## 🛠️ Tech Stack

- 🐳 Docker & Docker Compose
- ⏰ Apache Airflow (Orchestration)
- 🐘 PostgreSQL (Storage)
- 🐍 Python (ETL load, Pipline)
- 📦 dbt (Transformations)
- 📊 Streamlit (Dashboard)

---

## 🗂️ Project Structure

```
data-engineering-project/
├── dags/                     # Airflow DAGs
├── scripts/                  # Python ETL scripts
│   └── etl_load.py
├── analytics/                # dbt models and config (rename from dbt/)
│   └── models/
├── venv/                     # setup virtual environment
├── dashboard.py              # Streamlit dashboard
├── Dockerfile                # Custom Airflow image with dbt & dependencies          
├── docker-compose.yml
└── README.md
```

---

## ⚙️ How to Run

### 1. 🐳 Start Services

```bash
docker-compose up -d
```

This starts Airflow, PostgreSQL, and required services.

### 2. 🧪 Activate Virtual Environment (Optional)

```bash
source .venv/bin/activate
```

### 3. 🌐 Access Airflow UI

- Open browser: [http://localhost:8080](http://localhost:8080)
- Login: `airflow` / `airflow` (default)

### 4. ▶️ Trigger the DAG

- DAG name: `etl_with_dbt`
- Runs:
  - `etl_load.py` → load raw data
  - `dbt run` → transform data
  - (Optional) `dbt test`

### 5. 🖥️ Run Streamlit Dashboard

```bash
streamlit run dashboard/dashboard.py
```

- Open: [http://localhost:8501](http://localhost:8501)

---

## 🧠 Key Features

- End-to-end orchestration with Apache Airflow
- Modular pipeline with clean ETL and dbt transformations
- Interactive Streamlit dashboard with metrics and visualizations
- Realistic dev setup using Docker Compose
- dbt model outputs used directly in dashboard (no duplication!)

---

## 📸 Screenshots

- ✅ Airflow DAG
  ![Airflow](https://github.com/user-attachments/assets/f3bb32a5-8452-449c-8048-c3ab41bc9555)
- ✅ Streamlit dashboard (with metrics and chart)
  ![Dashboard_1](https://github.com/user-attachments/assets/eaeaeede-93b1-4c29-8366-47194e2abdf8)
  ![Dashboard_2](https://github.com/user-attachments/assets/415a4bc0-969b-40d1-b79c-47ea123f4481)

---

## ✅ To-Do / Future Improvements

- Add Airflow sensors or DAG dependencies
- Add dbt tests and CI checks
- Deploy dashboard to Streamlit Cloud
- Add automated data refresh schedule
- Enhance visualizations with filters and charts





---

## 👤 Author

**Korn-aphichit Ngaopan**\
🌐 GitHub: [@Izenberk](https://github.com/Izenberk)
