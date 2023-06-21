# KafkaIO Repository
Welcome to sap156/KafkaIO repository! This repository hosts a collection of Python scripts and Docker Compose files aimed to help you interact with Apache Kafka, a leading open-source distributed event streaming platform.

# Introduction
Apache Kafka is a robust event streaming platform that can process trillions of events daily. It offers low-latency, real-time handling and is used for a variety of applications such as data pipelines, analytics, data integration, and mission-critical applications.

This repository contains Python scripts demonstrating how to produce data to Kafka, consume data from Kafka, fetch server names, and topic names. In addition, this repository includes Docker Compose YAML files for setting up a Kafka environment.

# Prerequisites
To make the most out of this repository, you should have a basic understanding of:

1. Python programming
2. Apache Kafka
3. Docker and Docker Compose

# Installation
Before running the scripts or applications in this repository, ensure Apache Kafka and Docker are installed on your system.

Refer to the official documentation for installation guides:

1. Apache Kafka
2. Docker
3. Docker Compose

This repository contains scripts and configurations for producing, consuming, and processing data with Kafka, along with Docker Compose configurations for running Kafka and Zookeeper.

## Repository Structure

- `Database_Persist_and_Produce/`: This directory contains scripts that both produce data to Kafka and write data to a PostgreSQL database. These scripts can work with data from various sources including APIs, CSV and Parquet files, and OPC UA servers.
  
- `Database_Persist_only/`: This directory contains Kafka consumer scripts that consume data from Kafka and can persist it to a PostgreSQL database.
  
- `GeneralScripts/`: This directory contains general Kafka utility scripts such as listing Kafka brokers, creating Kafka topics, testing Kafka consumers, and checking Kafka connections.
  
- `Producers/`: This directory contains scripts to produce data to a Kafka topic. The scripts can handle various data sources such as APIs, log files, CSV and Parquet files, and OPC UA servers.

- `Kafka_Connect/`: This directory contains everything needed to create a custom Docker image from the Confluent Kafka Connect image, including a Dockerfile and a number of plugins.

- `*.yml`: These are Docker Compose files for running Kafka and Zookeeper configurations.

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/sap156/KafkaIO.git
    cd KafkaIO
    ```

2. Depending on your use case, navigate to the appropriate directory and run the necessary scripts. For example, if you want to produce data to a Kafka topic from a CSV file, you would use the `Kafka_CSVFile_Data_Producer.py` script in the `Producers/` directory.
   
3. To run Kafka and Zookeeper using Docker, use one of the provided Docker Compose configurations. For example, to run a single Zookeeper instance with multiple Kafka instances, you might use the `single-zk-multiple3-kafka.yml` file:
    ```bash
    docker-compose -f single-zk-multiple3-kafka.yml up -d
    ```

We hope this repository is a useful resource for your Kafka projects. If you encounter any issues or have questions, please raise an issue on this repository.


# KafkaIO Repository Structure

## Database_Persist_and_Produce

This directory contains scripts that both produce data to Kafka and write data to a PostgreSQL database. These scripts can work with data from various sources including APIs, CSV and Parquet files, and OPC UA servers. The files in this directory are:

- `Kafka_API_Data_Persist_and_Produce.py`: This script fetches data from APIs, sends it to Kafka, and also persists it in a PostgreSQL database.
- `Kafka_CSVFile_Data_Persist_and_Produce.py`: This script reads data from CSV files, sends it to Kafka, and also persists it in a PostgreSQL database.
- `Kafka_OPCUA_Data_Persist_and_Produce.py`: This script fetches data from OPC UA servers, sends it to Kafka, and also persists it in a PostgreSQL database.
- `Kafka_ParquetFile_Data_Persist_and_Produce.py`: This script reads data from Parquet files, sends it to Kafka, and also persists it in a PostgreSQL database.

## Database_Persist_only

This directory contains Kafka consumer scripts that consume data from Kafka and can persist it to a PostgreSQL database. The files in this directory are:

- `Kafka_Database_Persist_Consumer.py`: This script consumes data from Kafka and persists it in a PostgreSQL database.
- `Kafka_OPCUA_Database_Persist_Consumer.py`: This script consumes data from Kafka, specifically from OPC UA servers, and persists it in a PostgreSQL database.

## GeneralScripts

This directory contains general Kafka utility scripts such as listing Kafka brokers, creating Kafka topics, testing Kafka consumers, and checking Kafka connections. The files in this directory are:

- `Kafka_Broker_List.py`: This script lists all the Kafka brokers.
- `Kafka_Consumer_Test.py`: This script is used for testing Kafka consumers.
- `Kafka_Create_Topic.py`: This script is used for creating Kafka topics.
- `Kafka_Test_Connection.py`: This script is used for testing the connection to Kafka.
- `List_Kafka_Topics.py`: This script lists all the Kafka topics.

## Producers

This directory contains scripts to produce data to a Kafka topic. The scripts can handle various data sources such as APIs, log files, CSV and Parquet files, and OPC UA servers. The files in this directory are:

- `Kafka_APIAuth_Data_Producer.py`: This script fetches data from APIs with authentication and sends it to Kafka.
- `Kafka_API_Data_Producer.py`: This script fetches data from APIs and sends it to Kafka.
- `Kafka_CSVFile_Data_Producer.py`: This script reads data from CSV files and sends it to Kafka.
- `Kafka_LogFile_Data_Producer.py`: This script reads data from log files and sends it to Kafka.
- `Kafka_OPCUA_Data_Producer.py`: This script fetches data from OPC UA servers and sends it to Kafka.
- `Kafka_ParquetFile_Data_Producer.py`: This script reads data from Parquet files and sends it to Kafka.
- `Kafka_Random_Data_Producer.py`: This script generates random data and sends it to Kafka.

## Kafka_Connect

This directory contains everything needed to create a custom Docker image from the Confluent Kafka Connect image, including a Dockerfile and a number of plugins. The files in this directory are:

- `Dockerfile`: This Dockerfile extends from the latest Confluent Kafka Connect Base image and copies the connector plugins from the plugins/ directory to /opt/kafka/plugins/ in the image. It also sets the Kafka Connect plugin path to this directory
Sure, here is the content in Markdown format:

markdown
Copy code
# KafkaIO Repository Structure

## Database_Persist_and_Produce

This directory contains scripts that both produce data to Kafka and write data to a PostgreSQL database. These scripts can work with data from various sources including APIs, CSV and Parquet files, and OPC UA servers. The files in this directory are:

- `Kafka_API_Data_Persist_and_Produce.py`: This script fetches data from APIs, sends it to Kafka, and also persists it in a PostgreSQL database.
- `Kafka_CSVFile_Data_Persist_and_Produce.py`: This script reads data from CSV files, sends it to Kafka, and also persists it in a PostgreSQL database.
- `Kafka_OPCUA_Data_Persist_and_Produce.py`: This script fetches data from OPC UA servers, sends it to Kafka, and also persists it in a PostgreSQL database.
- `Kafka_ParquetFile_Data_Persist_and_Produce.py`: This script reads data from Parquet files, sends it to Kafka, and also persists it in a PostgreSQL database.

## Database_Persist_only

This directory contains Kafka consumer scripts that consume data from Kafka and can persist it to a PostgreSQL database. The files in this directory are:

- `Kafka_Database_Persist_Consumer.py`: This script consumes data from Kafka and persists it in a PostgreSQL database.
- `Kafka_OPCUA_Database_Persist_Consumer.py`: This script consumes data from Kafka, specifically from OPC UA servers, and persists it in a PostgreSQL database.

## GeneralScripts

This directory contains general Kafka utility scripts such as listing Kafka brokers, creating Kafka topics, testing Kafka consumers, and checking Kafka connections. The files in this directory are:

- `Kafka_Broker_List.py`: This script lists all the Kafka brokers.
- `Kafka_Consumer_Test.py`: This script is used for testing Kafka consumers.
- `Kafka_Create_Topic.py`: This script is used for creating Kafka topics.
- `Kafka_Test_Connection.py`: This script is used for testing the connection to Kafka.
- `List_Kafka_Topics.py`: This script lists all the Kafka topics.

## Producers

This directory contains scripts to produce data to a Kafka topic. The scripts can handle various data sources such as APIs, log files, CSV and Parquet files, and OPC UA servers. The files in this directory are:

- `Kafka_APIAuth_Data_Producer.py`: This script fetches data from APIs with authentication and sends it to Kafka.
- `Kafka_API_Data_Producer.py`: This script fetches data from APIs and sends it to Kafka.
- `Kafka_CSVFile_Data_Producer.py`: This script reads data from CSV files and sends it to Kafka.
- `Kafka_LogFile_Data_Producer.py`: This script reads data from log files and sends it to Kafka.
- `Kafka_OPCUA_Data_Producer.py`: This script fetches data from OPC UA servers and sends it to Kafka.
- `Kafka_ParquetFile_Data_Producer.py`: This script reads data from Parquet files and sends it to Kafka.
- `Kafka_Random_Data_Producer.py`: This script generates random data and sends it to Kafka.

## Kafka_Connect

This directory contains everything needed to create a custom Docker image from the Confluent Kafka Connect image, including a Dockerfile and a number of plugins. The files in this directory are:

- `Dockerfile`: This Dockerfile extends from the latest Confluent Kafka Connect Base image and copies the connector plugins from the plugins/ directory to /opt/kafka/plugins/ in the image. It also sets the Kafka Connect plugin path to this directorySure, here is the content in Markdown format:



