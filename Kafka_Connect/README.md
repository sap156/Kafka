# Kafka Connect Custom Docker Image

This repository contains a Dockerfile and associated Kafka Connect plugins to create a custom Kafka Connect Docker image based on the Confluent Kafka Connect Base image.

## Dockerfile

The Dockerfile extends from the latest Confluent Kafka Connect Base image and copies the connector plugins from the `plugins/` directory to `/opt/kafka/plugins/` in the image. It also sets the Kafka Connect plugin path to this directory. 

The Dockerfile looks like this:

```Dockerfile
FROM confluentinc/cp-kafka-connect-base:latest

USER root:root

# Copy your connector plugins to the proper directory
COPY ./plugins/ /opt/kafka/plugins/

# Set the Kafka Connect plugin path
ENV CONNECT_PLUGIN_PATH="/opt/kafka/plugins"

# Change user back to the default user
USER 1001

You can build your Docker image using the following command:
'docker build -f /path/to/this/Dockerfile . -t my-connector-image-name'

Remember to replace `/path/to/this/Dockerfile` with the actual path to the Dockerfile.```


## Plugins Folder
This repository includes the following plugins in the plugins/ directory:

clickhouse-kafka-connect-v0.0.10-beta
confluentinc-kafka-connect-mqtt-1.7.0
confluentinc-kafka-connect-avro-converter-7.4.0
confluentinc-kafka-connect-oracle-cdc-2.6.1
confluentinc-kafka-connect-cassandra-2.0.5
confluentinc-kafka-connect-s3-10.5.1
confluentinc-kafka-connect-ftps-1.0.5-preview
debezium-debezium-connector-mysql-2.2.1
confluentinc-kafka-connect-github-2.1.4
debezium-debezium-connector-postgresql-2.2.1
confluentinc-kafka-connect-hdfs3-source-2.5.3
debezium-debezium-connector-sqlserver-2.2.1
confluentinc-kafka-connect-http-1.7.2
mongodb-kafka-connect-mongodb-1.10.1
confluentinc-kafka-connect-influxdb-1.2.8
snowflakeinc-snowflake-kafka-connector-1.9.3
confluentinc-kafka-connect-json-schema-converter-7.4.0

## Source and Sink Properties
The 'source/' and 'sink/' directories contain JSON template files for various source and sink properties. You can use these templates to configure your Kafka Connect sources and sinks.

I hope this repository aids you in setting up and deploying your custom Kafka Connect Docker image. If you have any questions or issues, feel free to raise an issue on this repository.

