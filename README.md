\# High-Throughput Distributed CDC Financial Ledger



\## Overview



A real-time Change Data Capture (CDC) pipeline that captures financial transactions from PostgreSQL Write-Ahead Logs (WAL), streams them through Apache Kafka using Debezium, and prepares them for downstream analytics and Delta Lake storage.



\## Architecture



PostgreSQL

↓

Debezium CDC

↓

Apache Kafka

↓

Spark Streaming

↓

Delta Lake

↓

Power BI Dashboard



\## Technologies



\- PostgreSQL

\- Debezium

\- Apache Kafka

\- Kafka Connect

\- Spark

\- Delta Lake

\- Docker

\- Power BI

\- Python



\## Features



\- Real-time CDC from PostgreSQL WAL

\- Event-driven architecture

\- Kafka streaming

\- Fault-tolerant design

\- Containerized deployment

\- Financial transaction monitoring



\## Project Status



\- \[x] PostgreSQL Setup

\- \[x] Kafka Setup

\- \[x] Debezium CDC Integration

\- \[x] Docker Deployment

\- \[ ] Delta Lake Storage

\- \[ ] Power BI Dashboard

\- \[ ] Chaos Engineering Tests

