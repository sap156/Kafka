import os
import time
import pandas as pd
from confluent_kafka import Producer
import json

# Get user inputs
data_dir = input("Enter the directory path containing the CSV files: ")
kafka_broker = input("Enter the Kafka broker (format - localhost:9092): ")
kafka_topic = input("Enter the Kafka topic: ")

# Create a producer to send data to Kafka
producer = Producer({
    'bootstrap.servers': kafka_broker,
    'queue.buffering.max.messages': 10000000,  # Set the desired queue size
    'compression.type': 'zstd'  # Or 'snappy', 'lz4', 'zstd'
})

def process_file(filepath):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(filepath)

    try:
        for _, row in df.iterrows():
            # Convert each row to a dictionary
            row_dict = row.to_dict()
            
            # Serialize the row to JSON
            message_json = json.dumps(row_dict)

            # Send the message to Kafka
            producer.produce(topic=kafka_topic, value=message_json)
            
            time.sleep(0.1)
    finally:
        # Flush any outstanding messages
        producer.flush()

# Get the list of files already processed
processed_files = set()

while True:
    # List all CSV files in the directory
    files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]

    # Process any new files
    for file in files:
        if file not in processed_files:
            process_file(os.path.join(data_dir, file))
            processed_files.add(file)

    # Wait for a while before checking the directory again
    time.sleep(10)
