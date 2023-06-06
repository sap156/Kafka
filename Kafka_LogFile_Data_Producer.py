import os
import time
from confluent_kafka import Producer
import json

# Get user inputs
data_dir = input("Enter the directory path containing the log files: ")
kafka_broker = input("Enter the Kafka broker (format - localhost:9092): ")
kafka_topic = input("Enter the Kafka topic: ")

# Create a producer to send data to Kafka
producer = Producer({
    'bootstrap.servers': kafka_broker,
    'queue.buffering.max.messages': 10000000,  # Set the desired queue size
    'compression.type': 'zstd'  # Or 'snappy', 'lz4', 'zstd'
})

def process_file(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            # Create a message to be sent to Kafka
            message = {
                'log_line': line.strip()  # Remove any trailing newline characters
            }

            # Serialize the message to JSON
            message_json = json.dumps(message)

            # Send the message to Kafka
            producer.produce(topic=kafka_topic, value=message_json)

        # Close the producer
        producer.flush()

# Get the list of files already processed
processed_files = set()

while True:
    # List all log files in the directory
    files = [f for f in os.listdir(data_dir) if f.endswith('.log')]

    # Process any new files
    for file in files:
        if file not in processed_files:
            process_file(os.path.join(data_dir, file))
            processed_files.add(file)

    # Wait for a while before checking the directory again
    time.sleep(10)