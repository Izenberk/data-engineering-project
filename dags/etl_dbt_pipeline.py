from airflow import DAG #type: ignore
from airflow.operators.bash import BashOperator #type: ignore
from datetime import datetime

# Default argument for DAG
default_args = {
    'start_date': datetime(2024, 1, 1),
    'catchup': False
}

# Define the DAG
with DAG(
    dag_id='etl_dbt_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    description='Run ETL script and the dbt model',
    tags=['etl', 'dbt']
    ) as dag:

    # Task 1: Run the ETL script
    run_etl = BashOperator(
        task_id='run_etl_script',
        bash_command='python /opt/airflow/dags/scripts/etl_load.py'
    )

    # Task 2: Run dbt models
    run_dbt = BashOperator(
        task_id='run_dbt_model',
        bash_command='cd /opt/airflow/dags/analytics && dbt run'
    )

    # Task 3: Run dbt tests
    run_dbt_test = BashOperator(
        task_id='run_dbt_tests',
        bash_command='cd /opt/airflow/dags/analytics && dbt test'
    )

    # Set task dependencies
    run_etl >> run_dbt >> run_dbt_test