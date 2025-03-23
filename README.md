# 📦 data-engineering-project

## 🚀 End-to-End Data Engineering Pipeline with Airflow, dbt, and PostgreSQL

This project demonstrates a complete batch data pipeline using **Apache Airflow**, **dbt**, and **PostgreSQL**. It extracts E-commerce transactional data, loads it into a PostgreSQL database, transforms it using dbt, and prepares it for visualization.

---

## 🗺️ Project Architecture

> E-commerce Data → ETL (Python) → PostgreSQL (raw) → dbt (modeled) → Dashboard (Looker Studio)

---

## 🛠️ Tech Stack

- 🐳 Docker & Docker Compose
- ⏰ Apache Airflow (Orchestration)
- 🐘 PostgreSQL (Storage)
- 🐍 Python (`etl_load.py`)
- 📦 dbt (Transformations)
- 📊 Google Looker Studio *(optional – for dashboarding)*

---

## 🗂️ Project Structure

```
data-engineering-project/
├── dags/                   # Airflow DAGs (via symlinks)
├── etl/                    # Python ETL scripts
│   └── etl_load.py
├── dbt_project/            # dbt models and config
│   └── models/
├── docker/
│   └── Dockerfile          # Custom Airflow image with dbt & dependencies
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

---

## 🧠 Key Features

- Clean separation between ETL and transformation logic
- Uses **symlinks** to keep `dags/` clean
- Connects to PostgreSQL differently for local vs Docker (`localhost` → `postgres`)
- Custom Airflow image with:
  - `dbt-postgres`
  - `pandas`, `sqlalchemy`, etc.

---

## 📸 Screenshots (Optional)

- Airflow DAG
- dbt model graph
- Dashboard (Looker Studio)

---

## ✅ To-Do / Future Improvements

- [ ] Add Airflow sensors or more DAGs
- [ ] Add dbt tests & documentation
- [ ] Create automated dashboard refresh
- [ ] Add CI/CD pipeline

---

## 👤 Author

**Korn-aphichit Ngaopan**  
🌐 GitHub: [@Izenberk](https://github.com/Izenberk)
