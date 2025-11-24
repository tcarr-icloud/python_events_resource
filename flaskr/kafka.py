import json
import os

from kafka import KafkaProducer

KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'events')
KAFKA_BOOTSTRAP_SERVER = os.getenv('KAFKA_BOOTSTRAP_SERVER', 'localhost:39092')

producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVER)


def send_event(event):
    serialize_event = json.dumps(event).encode('utf-8')
    producer.send(KAFKA_TOPIC, serialize_event)
