import os
import time
import json
from opcua import Client, ua
from confluent_kafka import Producer

# Get user inputs
print("Please enter the OPC-UA server URL in the following format: opc.tcp://hostname:port")
opcua_url = input("Enter the OPC-UA server URL: ")
kafka_broker = input("Enter the Kafka broker (format - localhost:9092): ")
kafka_topic = input("Enter the Kafka topic: ")
print("Please enter the name of the OPC-UA object to read from.")
opcua_object_name = input("Enter the OPC-UA object name: ")

# Create a producer to send data to Kafka
producer = Producer({
    'bootstrap.servers': kafka_broker,
    'queue.buffering.max.messages': 10000000,  # Set the desired queue size
    'compression.type': 'zstd'  # Or 'snappy', 'lz4', 'zstd'
})

def process_opcua_data(opcua_data):
    for variable, value in opcua_data:
        timestamp = value.ServerTimestamp.isoformat()
        data_value = value.Value.Value
        # Check if value is boolean and convert it
        if isinstance(data_value, bool):
            data_value = 1 if data_value else 0
        # Create a message to be sent to Kafka
        message = {
            'timestamp': timestamp,
            'sensor_name': str(variable),  # Modify this as needed
            'value': data_value
        }
        # Serialize the message to JSON
        message_json = json.dumps(message)
        # Send the message to Kafka
        producer.produce(topic=kafka_topic, value=message_json, key=str(variable))

# Connect to OPC-UA server
client = Client(opcua_url)
client.connect()

# Get the OPC-UA object
root = client.get_root_node()
object_node = root.get_child(["0:Objects", f"1:{opcua_object_name}"])

# Get the variables within the object
variables = object_node.get_variables()

while True:
    try:
        # Read OPC-UA data
        opcua_data = [(variable, variable.get_data_value()) for variable in variables]
        # Process the data and send to Kafka
        process_opcua_data(opcua_data)
        # Wait for a while before reading the data again
        time.sleep(10)
    finally:
        # Close the producer
        producer.flush()

# Disconnect from OPC-UA server
client.disconnect()
