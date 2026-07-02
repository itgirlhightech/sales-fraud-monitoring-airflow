from airflow import DAG 
from airflow.operators.python import PythonOperator
from datetime import datetime as dt

import os
from dotoenv import load_dotenv
import psycopg2
import logging

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

    conn = psycopg2.connect( 
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.gentenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

    cursor = conn.cursor()

    with open("src/sql/daily_report.sql", "r") as  file:
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
        task_id= "run_elt",
        python_callable=run_etl
    )

    report_task = PythonOperator(
        task_id="run_daily_report",
        python_callable=run_daily_report
    )

    etl_task >> report_task

 
