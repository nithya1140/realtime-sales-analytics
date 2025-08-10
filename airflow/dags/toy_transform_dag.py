from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os, json, glob

DATA_DIR = "/opt/airflow/dags/data"
OUT_DIR = os.path.join(DATA_DIR, "_outputs")

def transform():
    os.makedirs(OUT_DIR, exist_ok=True)
    files = sorted(glob.glob(os.path.join(DATA_DIR, "events_*.jsonl")))
    total = 0.0
    rows = 0
    for fp in files:
        with open(fp, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    rec = json.loads(line)
                    total += float(rec.get("amount", 0))
                    rows += 1
                except Exception:
                    pass
    out_path = os.path.join(OUT_DIR, "summary.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({"files_processed": len(files), "rows": rows, "total_amount": round(total, 2)}, f, indent=2)
    return out_path

with DAG(
    dag_id="toy_transform_dag",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@hourly",
    catchup=False,
    default_args={"owner": "airflow"}
) as dag:
    compute_summary = PythonOperator(
        task_id="compute_summary",
        python_callable=transform
    )