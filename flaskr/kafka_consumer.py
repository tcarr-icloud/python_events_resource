import json
import os

from kafka import KafkaConsumer

from flaskr import dynamodb

KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'events')
KAFKA_BOOTSTRAP_SERVER = os.getenv('KAFKA_BOOTSTRAP_SERVER', 'localhost:39092')


def safe_deserialize(x):
    try:
        return json.loads(x.decode('utf-8')) if x else None
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        return None


def kafka_consumer_thread():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
        group_id='event_consumer_group',
        value_deserializer=safe_deserialize
    )
    for message in consumer:
        event = message.value
        dynamodb.put_event(KAFKA_TOPIC, event)
