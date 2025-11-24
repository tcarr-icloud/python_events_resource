import os
import threading

from flask import Flask

from flaskr.dynamodb_controller import dynamodb_bp
from flaskr.events_controller import events_bp
from flaskr.kafka_consumer import kafka_consumer_thread


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping()
    app.register_blueprint(events_bp)
    app.register_blueprint(dynamodb_bp)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    consumer_thread = threading.Thread(target=kafka_consumer_thread)
    consumer_thread.daemon = True  # Allow the main thread to exit even if consumer is running
    consumer_thread.start()

    return app
