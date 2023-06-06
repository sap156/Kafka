from confluent_kafka.admin import AdminClient, NewTopic

# Prompt user for inputs
kafka_broker = input("Enter Kafka broker (format - localhost:9092): ")
kafka_topic = input("Enter new Kafka topic: ")
num_partitions = int(input("Enter number of partitions: "))
replication_factor = int(input("Enter replication factor: "))

# Create a Kafka admin client
admin_client = AdminClient({
    'bootstrap.servers': kafka_broker
})

topic = NewTopic(
    name=kafka_topic,
    num_partitions=num_partitions,
    replication_factor=replication_factor
)

# Attempt to create the topic

admin_client.create_topics([topic])

