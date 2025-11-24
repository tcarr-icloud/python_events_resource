import os

from flask import Blueprint, jsonify, request

from flaskr import dynamodb
from flaskr.authentication import auth_decorator

TABLE_NAME = os.getenv('TABLE_NAME', 'events')
dynamodb_bp = Blueprint('dynamodb_bp', __name__, url_prefix='/dynamodb')


@dynamodb_bp.route('/<string:aggregate_id>', methods=['GET'])
@auth_decorator
def get_event_by_pk(aggregate_id):
    aggregates = dynamodb.get_event_by_pk(TABLE_NAME, aggregate_id)
    if aggregates:
        return jsonify(aggregates), 200
    else:
        return "", 404


@dynamodb_bp.route('/<string:aggregate_id>/<string:timestamp>', methods=['GET'])
@auth_decorator
def get_event_by_pk_and_sk(aggregate_id, timestamp):
    aggregate = dynamodb.get_event_by_pk_and_sk(TABLE_NAME, aggregate_id, timestamp)
    if aggregate:
        return jsonify(aggregate), 200
    else:
        return "", 404


@dynamodb_bp.route('', methods=['POST'])
@auth_decorator
def put_event():
    event = request.get_json()
    dynamodb.put_event(TABLE_NAME, event)
    return '', 201
