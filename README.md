# Real-Time Sales Analytics Platform (Snowflake + dbt + Kafka + Airflow)

A production-style data platform that streams e-commerce events to Kafka, lands raw data in cloud storage, loads to Snowflake, transforms with dbt, and orchestrates end-to-end with Airflow. Includes data quality tests and dimensional models for analytics.

## Architecture
```mermaid
flowchart LR
A[Python Generator] -->|JSON events| K[Apache Kafka]
K --> C[Consumer]
C -->|land raw| D[(Azure Data Lake / Blob)]
D --> S[Snowflake Staging]
S -->|ELT| T[dbt Models (Staging → Marts)]
T --> BI[BI / Queries]
A -. Airflow DAG orchestrates .-> K

