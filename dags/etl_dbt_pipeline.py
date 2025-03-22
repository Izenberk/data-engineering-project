from airflow import DAG #type: ignore
from airflow.operators.bash import BashOperator #type: ignore
from datetime import datetime


with DAG(
    dag_id='etl_dbt_pipeline',
    default_args=default_args,
    schedule_interval=None,
    description='Run ETL script and the dbt model'
    tags=['etl', 'dbt']
) as dag:

    run_etl = BashOperator(
        task_id='run_etl_script',
        bash_command='python /opt/airflow/dags/script/etl_load.py'
    )

    run_dbt = BashOperator(
        task_id='run_dbt_script'
        bash_command='cd /opt/airflow/dags/analytics && dbt run'
    )

    run_etl >> run_dbt