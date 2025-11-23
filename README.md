# Python Events Resource

A Flask-based application for managing events backed by AWS DynamoDB.

## Project Structure

The project is organized as a Flask application package:

*   `flaskr/`: Contains the core application logic.
    *   `events_controller.py`: Handles API endpoints and logic for event management.
    *   `dynamodb.py`: Manages connections and operations with AWS DynamoDB.
    *   `constants.py`: Application-wide constants.
*   `config.py`: Configuration settings for the application.
*   `requests.http`: Collection of HTTP requests for testing the API (compatible with JetBrains IDEs).

## Prerequisites

*   Python 3.14
*   `virtualenv` tool
*   AWS Credentials configured (locally or via environment variables) for DynamoDB access.
*   DynamoDB table as shown in example. Set region as needed.
    ```bash
    aws dynamodb create-table \
    --endpoint-url "http://localhost:8000" \
    --region <<region>> \
    --table-name events \
    --attribute-definitions \
      AttributeName=AggregateId,AttributeType=S \
      AttributeName=Timestamp,AttributeType=S \
    --key-schema \
      AttributeName=AggregateId,KeyType=HASH \
      AttributeName=Timestamp,KeyType=RANGE \
    --billing-mode PAY_PER_REQUEST \
    --table-class STANDARD
    ```

## Installation

1.  **Create and activate a virtual environment:**

    ```bash
    virtualenv .venv
    source .venv/bin/activate
    # On Windows use: .venv\Scripts\activate
    ```

2.  **Install dependencies:**

    The project relies on the following key packages: `flask`, `boto3`, `click`, `jinja2`, `werkzeug`.

    ```bash
    pip install flask boto3
    ```

## Running the Application

1.  Set the Flask application environment variable (optional, defaults to `flaskr` in this structure often):

    ```bash
    export FLASK_APP=flaskr
    ```

2.  Run the server:

    ```bash
    flask run
    ```

## API Usage

Refer to the `requests.http` file for examples of how to interact with the API endpoints defined in the `events_controller`.

**Curl Examples**

```bash
# Create an event
curl -X POST \
--location "http://127.0.0.1:5000/events" \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"aggregate_id": "aggregate_2", "event": "update-2", "data": "string_data"}'
```

```bash
# Get all events for aggregate
curl -X GET \
--location "http://127.0.0.1:5000/events/aggregate_2" \
-H "Accept: application/json"
```