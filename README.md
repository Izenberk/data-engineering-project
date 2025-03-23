✅ Updated README.md for Your Project

# 📦 data-engineering-project

## 🚀 End-to-End Data Engineering Pipeline with Airflow, dbt, PostgreSQL & Streamlit

This project demonstrates a complete batch data pipeline using **Apache Airflow**, **dbt**, and **PostgreSQL** for backend processing, with a front-end dashboard built in **Streamlit** for visualization.

It extracts E-commerce transactional data, loads it into PostgreSQL, transforms it using dbt models, and displays the results via an interactive dashboard.

---

## 🗺️ Project Architecture

> E-commerce Data → ETL (Python) → PostgreSQL (raw) → dbt (modeled) → Dashboard (Streamlit)

---

## 🛠️ Tech Stack

- 🐳 Docker & Docker Compose
- ⏰ Apache Airflow (Orchestration)
- 🐘 PostgreSQL (Storage)
- 🐍 Python (`etl_load.py`)
- 📦 dbt (Transformations)
- 📊 Streamlit (Dashboard)

---

## 🗂️ Project Structure


data-engineering-project/
├── dags/                   # Airflow DAGs (via symlinks)
├── etl/                    # Python ETL scripts
│   └── etl_load.py
├── dbt_project/            # dbt models and config
│   └── models/
├── dashboard/              # Streamlit dashboard
│   └── dashboard.py
├── docker/
│   └── Dockerfile          # Custom Airflow image with dbt & dependencies
├── docker-compose.yml
└── README.md


---

## ⚙️ How to Run

### 1. 🐳 Start Services

```bash
docker-compose up -d

This starts Airflow, PostgreSQL, and required services.

2. 🧪 Activate Virtual Environment (Optional)

source .venv/bin/activate

3. 🌐 Access Airflow UI

Open browser: http://localhost:8080

Login: airflow / airflow (default)

4. ▶️ Trigger the DAG

DAG name: etl_with_dbt

Runs:

etl_load.py → load raw data

dbt run → transform data

(Optional) dbt test

5. 🖥️ Run Streamlit Dashboard

streamlit run dashboard/dashboard.py

Open: http://localhost:8501

🧠 Key Features

End-to-end orchestration with Apache Airflow

Modular pipeline with clean ETL and dbt transformations

Interactive Streamlit dashboard with metrics and visualizations

Realistic dev setup using Docker Compose

dbt model outputs used directly in dashboard (no duplication!)

📸 Screenshots

✅ Airflow DAG
![Airflow](https://github.com/user-attachments/assets/2fd338cf-8e42-4cd6-90bc-f699cc7a7d66)

✅ Streamlit dashboard (with metrics and chart)
![Dashboard_1](https://github.com/user-attachments/assets/6e6d3b75-4f70-4f5b-a730-134c066166ea)
![Dashboard_2](https://github.com/user-attachments/assets/7f8e2784-da97-468d-aa66-e37a2dc43918)



✅ To-Do / Future Improvements

Add Airflow sensors or DAG dependencies

Add dbt tests and CI checks

Deploy dashboard to Streamlit Cloud

Add automated data refresh schedule

Enhance visualizations with filters and charts

👤 Author

Korn-aphichit Ngaopan🌐 GitHub: @Izenberk
