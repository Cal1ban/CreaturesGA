from kafka import KafkaConsumer
from Utilities.Serialization.parser import parse


def start_stream(topic, processing_function, filters):
    consumer = KafkaConsumer(topic, bootstrap_servers=['0.0.0.0:9092'])
    for message in consumer:
        parsed = parse(message.value)
        if filters is None or type(parsed) in filters:
            processing_function(parsed)
