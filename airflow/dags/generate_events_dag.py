from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import json, os, time

DATA_DIR = "/opt/airflow/dags/data"

def generate():
    os.makedirs(DATA_DIR, exist_ok=True)
    ts = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    path = os.path.join(DATA_DIR, f"events_{ts}.jsonl")
    with open(path, "w", encoding="utf-8") as f:
        for i in range(25):
            event = {
                "ts": datetime.utcnow().isoformat(),
                "order_id": i + 1,
                "amount": round(10 + i * 1.25, 2),
                "currency": "USD"
            }
            f.write(json.dumps(event) + "\n")
    return path

with DAG(
    dag_id="generate_events_dag",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@hourly",
    catchup=False,
    default_args={"owner": "airflow"}
) as dag:
    generate_events = PythonOperator(
        task_id="generate_events",
        python_callable=generate
    )