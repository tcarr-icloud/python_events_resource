import datetime

from flask import Blueprint, request

import flaskr.kafka_producer
from flaskr.authentication import auth_decorator

events_bp = Blueprint('events_bp', __name__, url_prefix='/events')


@events_bp.route('', methods=['POST'])
@auth_decorator
def produce_event():
    event = request.get_json()
    event["Timestamp"] = str(datetime.datetime.now(datetime.timezone.utc))
    flaskr.kafka_producer.produce_event(event)
    return '', 201
