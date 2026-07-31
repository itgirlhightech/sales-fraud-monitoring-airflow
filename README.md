# Sales Fraud Monitoring Airflow

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-3.2.2-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple)

---

## About

This project is an end-to-end data engineering pipeline built with Apache Airflow, Python, Pandas, SQL, and PostgreSQL.

The pipeline automates the ETL (Extract, Transform, Load) process using a subset of the Credit Card Fraud Detection dataset. It extracts raw transaction data, transforms it by identifying suspicious transactions, loads the processed dataset into PostgreSQL, and generates automated SQL reports through Apache Airflow.

The project was developed to demonstrate practical skills in workflow orchestration, ETL development, SQL reporting, and database integration.

---

## Features

- Automated ETL pipeline
- Apache Airflow DAG orchestration
- Data extraction using Python
- Data transformation with Pandas
- PostgreSQL integration
- Automated SQL reports
- Fraud transaction identification
- Modular project architecture

---

## Technologies

- Apache Airflow 3.2.2
- Python 3.12
- Pandas
- PostgreSQL
- SQL
- Psycopg3
- python-dotenv

---

## Project Structure

```text
sales-fraud-monitoring-airflow/
│
├── airflow_home/
│   └── dags/
│       └── fraud_monitoring_dag.py
│
├── src/
│   ├── data/
│   │   └── creditcard_sample_10000.csv
│   │
│   ├── scripts/
│   │   ├── extract.py
│   │   ├── transform.py
│   │   └── load.py
│   │
│   └── sql/
│       └── daily_report.sql
│
├── requirements.txt
└── README.md
```

![tree](<assets/Captura de tela 2026-07-07 192324.png>)
---

## Pipeline Architecture

```text
Credit Card Dataset (CSV)
            │
            ▼
      Extract (Python)
            │
            ▼
    Transform (Pandas)
            │
            ▼
 Load into PostgreSQL
            │
            ▼
 Apache Airflow DAG
     │             │
     ▼             ▼
 run_etl()   run_daily_report()
```

---

## Workflow

1. Read transaction data from a CSV dataset.
2. Transform the dataset and classify suspicious transactions.
3. Store processed data in PostgreSQL.
4. Execute SQL reports.
5. Orchestrate the complete workflow with Apache Airflow.

---

## Screenshots

### Airflow Dashboard

![dash](<assets/Captura de tela 2026-07-07 192623.png>)
---

### DAG Graph

![graph](<assets/fraud_monitoring_dag-graph.png>)

---

### DAG Grid


![grid](<assets/Captura de tela 2026-07-07 192717.png>)


![grid](<assets/Captura de tela 2026-07-07 192717.png>)


---

### SQL Reports

!![sql reports](<assets/sql_reports.png>)


## Data Source

Sample of the Kaggle Credit Card Fraud Detection dataset
(10,000 transactions subset for local development).

Original dataset:

https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

---
