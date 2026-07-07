from airflow import DAG 
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime as dt

import os
import sys
import psycopg 
from dotenv import load_dotenv
import logging

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)
sys.path.insert(0, PROJECT_ROOT)

from src.scripts.extract import extract
from src.scripts.transform import transform
from src.scripts.load import load

""" ETL function """

def run_etl():
    df = extract()
    df = transform(df)
    load(df)

""" DAG definition"""

def run_daily_report():

    load_dotenv() 

    conn = psycopg.connect( 
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

    cursor = conn.cursor()

    sql_path = os.path.join(PROJECT_ROOT, "src", "sql", "daily_report.sql")

    with open(sql_path, "r") as  file:
        sql_file = file.read()
        queries = sql_file.split(";")

    for query in queries:
        query = query.strip()

        if not query:
            continue
        try: 
            cursor.execute(query)
            result = cursor.fetchall()

            logging.info(f"Query result: {result}")

        except Exception as e:
            logging.error(f"Error executing query: {query}")
            logging.error(str(e))

    cursor.close()
    conn.close()


with DAG(
    dag_id="fraud_monitoring_dag",
    start_date=dt(2026, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:
    
    etl_task = PythonOperator(
        task_id= "run_etl",
        python_callable=run_etl
    )

    report_task = PythonOperator(
        task_id="run_daily_report",
        python_callable=run_daily_report
    )

    etl_task >> report_task

 
