# Real-Time Sales Analytics Platform  
*Snowflake + dbt + Kafka + Airflow + Azure Storage*

A production-style data platform that streams e-commerce events into Kafka, lands raw data in cloud storage, loads it to Snowflake, transforms it with dbt, and orchestrates the pipeline end-to-end with Airflow.  
Includes **data quality checks**, **dimensional models**, and a ready-to-use analytics layer.

---

## 📌 Architecture

```mermaid
flowchart LR
  A[Python Generator] -->|JSON events| K[Apache Kafka]
  K --> C[Consumer]
  C -->|land raw| D[(Azure Data Lake / Blob)]
  D --> S[Snowflake Staging]
  S -->|ELT| T[dbt Models - Staging to Marts]
  T --> BI[BI / Queries]
  A -. Airflow DAG orchestrates .-> K
