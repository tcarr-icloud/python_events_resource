import datetime
import os

from flask import Blueprint, jsonify, request

from flaskr import dynamodb, kafka
from flaskr.authentication import auth_decorator

events_bp = Blueprint('events_bp', __name__, url_prefix='/events')

TABLE = os.getenv('EVENTS_TABLE_NAME', 'events')


@events_bp.route('/<string:aggregate_id>', methods=['GET'])
@auth_decorator
def get_one_all(aggregate_id):
    aggregates = dynamodb.get_one_all(TABLE, aggregate_id)
    if aggregates:
        return jsonify(aggregates), 200
    else:
        return "", 404


@events_bp.route('/<string:aggregate_id>/<string:timestamp>', methods=['GET'])
@auth_decorator
def get_one(aggregate_id, timestamp):
    aggregate = dynamodb.get_one(TABLE, aggregate_id, timestamp)
    if aggregate:
        return jsonify(aggregate), 200
    else:
        return "", 404


@events_bp.route('', methods=['POST'])
@auth_decorator
def post():
    event = request.get_json()
    event["Timestamp"] = str(datetime.datetime.now(datetime.timezone.utc))
    dynamodb.put(TABLE, event)
    kafka.send_event(event)
    return '', 201
