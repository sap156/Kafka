from confluent_kafka.admin import AdminClient

# Prompt user for inputs
kafka_broker = "localhost:9092"
kafka_broker = input("Enter Kafka broker (format - localhost:9092): ") or kafka_broker

# Create a Kafka AdminClient
admin_client = AdminClient({'bootstrap.servers': kafka_broker})

# Fetch cluster metadata
cluster_metadata = admin_client.list_topics(timeout=10)

# Get list of all brokers in the cluster
brokers = cluster_metadata.brokers

# Print details of each broker
for broker in brokers.values():
    print("Broker ID: {}, Host: {}:{}".format(broker.id, broker.host, broker.port))
