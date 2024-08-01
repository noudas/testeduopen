# routes.py

# Import necessary modules and configurations
from flask import jsonify, request
import requests

from Flask_App.db_connect import get_db_connection
from .config import Config

# Function to authenticate and retrieve an API key from the Pluggy API
def get_api_key():
    """
    Authenticate and fetch the API key from the Pluggy API.
    Sends a POST request to the authentication endpoint of the Pluggy API with the client ID and secret.
    Returns the API key upon successful authentication or raises an exception if authentication fails.
    """
    auth_url = f"{Config.PLUGGY_API_BASE_URL}/auth"
    response = requests.post(auth_url, json={
        "clientId": Config.PLUGGY_CLIENT_ID,
        "clientSecret": Config.PLUGGY_CLIENT_SECRET
    })
    if response.status_code == 200:
        return response.json()["apiKey"]
    else:
        raise Exception("Authentication failed: " + response.text)

# Initialize the Flask application and define routes
def init_app(app):
    # Route to handle GET requests for transaction details by item ID
    @app.route("/transactions/<accountId>", methods=["GET"])
    def get_transaction_details(accountId):
        """
        Handles GET requests to "/transacao/<accountId>".
        Authenticates using the client ID and secret, then retrieves transaction details for the specified item ID.
        Returns the transaction details on success or an error message on failure.
        """
        client_id = Config.PLUGGY_CLIENT_ID
        client_secret = Config.PLUGGY_CLIENT_SECRET
        
        # Obtain access token
        auth_url = f"{Config.PLUGGY_API_BASE_URL}/auth"
        auth_response = requests.post(auth_url, json={
            "clientId": client_id,
            "clientSecret": client_secret
        })

        if auth_response.status_code != 200:
            return jsonify({"error": "Authentication failed.", "details": auth_response.text}), auth_response.status_code

        access_token = auth_response.json()["accessToken"]

        # Retrieve transactions
        transactions_url = f'{Config.PLUGGY_API_BASE_URL}/transactions$accountId={accountId}'
        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        response = requests.get(transactions_url, headers=headers)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": f"Failed to fetch transactions. Status Code: {response.status_code}", "details": response.text})

    # Route to handle POST requests for creating a new person
    @app.route("/pessoas", methods=["POST"])
    def create_person():
        """
        Handles POST requests to "/pessoas".
        Extracts data from the request body, connects to the database, and inserts a new person record.
        Returns the newly created person's ID or an error message on failure.
        """
        data = request.json
        cpf = data.get("cpf")
        age = data.get("idade")
        accepts_terms = data.get("aceita_termos")

        connection = get_db_connection()
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO pessoas (cpf, idade, aceita_termos)
        VALUES (%s, %s, %s)
        RETURNING id;
        """

        try:
            cursor.execute(insert_query, (cpf, age, accepts_terms))
            connection.commit()
            person_id = cursor.fetchone()[0]
            return jsonify({"id": person_id}), 201
        except Exception as e:
            return jsonify({"error": f"Error creating person: {e}"}), 500
        finally:
            cursor.close()
            connection.close()

    # Route to handle POST requests for creating a connect token
    @app.route("/connect_token", methods=["POST"])
    def create_connect_token():
        """
        Handles POST requests to "/connect_token".
        Authenticates using the client ID and secret, then creates a connect token.
        Returns the connect token on success or an error message on failure.
        """
        client_id = Config.PLUGGY_CLIENT_ID
        client_secret = Config.PLUGGY_CLIENT_SECRET

        # Obtain access token
        auth_url = f"{Config.PLUGGY_API_BASE_URL}/auth"
        auth_response = requests.post(auth_url, json={
            "clientId": client_id,
            "clientSecret": client_secret
        })

        if auth_response.status_code != 200:
            return jsonify({"error": "Authentication failed.", "details": auth_response.text}), auth_response.status_code

        access_token = auth_response.json()["accessToken"]

        # Create connect token
        connect_token_url = f"{Config.PLUGGY_API_BASE_URL}/connect_token"
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }

        payload = request.json

        response = requests.post(connect_token_url, headers=headers, json=payload)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": f"Failed to create connect token. Status Code: {response.status_code}", "details": response.text})

    # Route to handle GET requests for retrieving all available connectors
    @app.route("/connectors", methods=["GET"])
    def get_all_connectors():
        """
        Handles GET requests to "/connectors".
        Retrieves a list of all available connectors using the API key.
        Returns the list of connectors on success or an error message on failure.
        """
        try:
            api_key = get_api_key()
            connectors_url = f'{Config.PLUGGY_API_BASE_URL}/connectors'
            headers = {
                'X-API-KEY': api_key,
                'accept': 'application/json'
            }
            response = requests.get(connectors_url, headers=headers)
            if response.status_code == 200:
                return jsonify(response.json())
            else:
                return jsonify({"error": f"Failed to fetch connectors. Status Code: {response.status_code}", "details": response.text}), response.status_code
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # Route to handle GET requests for retrieving a specific connector by ID
    @app.route("/connectors/<int:connector_id>", methods=["GET"])
    def get_connector_by_id(connector_id):
        """
        Handles GET requests to "/connectors/<int:connector_id>".
        Retrieves details of a specific connector using its ID and the API key.
        Returns the connector details on success, an error message if the connector is not found, or an error message on other failures.
        """
        try:
            api_key = get_api_key()
            connector_url = f'{Config.PLUGGY_API_BASE_URL}/connectors/{connector_id}'
            headers = {
                'X-API-KEY': api_key,
                'accept': 'application/json'
            }
            response = requests.get(connector_url, headers=headers)
            if response.status_code == 200:
                return jsonify(response.json())
            elif response.status_code == 404:
                return jsonify({"error": "Connector not found."}), 404
            else:
                return jsonify({"error": f"Failed to fetch connector. Status Code: {response.status_code}", "details": response.text}), response.status_code
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # Route to handle POST requests for validating a connector
    @app.route("/connectors/<int:connector_id>/validate", methods=["POST"])
    def validate_connector(connector_id):
        """
        Handles POST requests to "/connectors/<int:connector_id>/validate".
        Validates a specific connector using its ID and the API key.
        Returns validation result on success or an error message on failure.
        """
        try:
            api_key = get_api_key()  # Ensure this returns a clean API key
            validate_url = f"{Config.PLUGGY_API_BASE_URL}/connectors/{connector_id}/validate"
            
            # Ensure the base URL does not end with a slash unless intentional
            if not validate_url.endswith('/'):
                validate_url += '/'
            
            headers = {
                'X-API-KEY': api_key,
                'Content-Type': 'application/json',
                'Accept': 'application/json'  # Note the capitalization; 'accept' was lowercase
            }
            payload = request.json
            
            # Make sure the payload is JSON serializable
            if not isinstance(payload, dict):
                raise ValueError("Payload must be a dictionary")
            
            response = requests.post(validate_url, headers=headers, json=payload)
            if response.status_code == 200:
                return jsonify(response.json())
            else:
                return jsonify({"error": f"Error validating connector. Status Code: {response.status_code}", "details": response.text}), response.status_code
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    # Route to handle GET requests for retrieving item details by item ID
    @app.route("/items/<item_id>", methods=["GET"])
    def get_item_details(item_id):
        """
        Handles GET requests to "/items/<item_id>".
        Fetches details of a specific item using its ID and the API key.
        Returns the item details on success, an error message if the item is not found, or an internal server error message on other failures.
        """
        api_key = get_api_key()
        item_url = f"https://api.pluggy.ai/items/{item_id}"
        headers = {
            "accept": "application/json",
            "X-API-KEY": api_key
        }
        response = requests.get(item_url, headers=headers)
        if response.status_code == 200:
            return jsonify(response.json()), 200
        elif response.status_code == 404:
            return jsonify({"error": "Item not found"}), 404
        else:
            return jsonify({"error": "Server Internal Error"}), 500

    @app.route("/accounts/<item_id>", methods=["GET"])
    def get_all_accounts(item_id):
        """
        Handles GET requests to "/accounts".
        Retrieves a list of all accounts using the API key.
        Returns the list of accounts on success or an error message on failure.
        """
        try:
            api_key = get_api_key()
            accounts_url = f'https://api.pluggy.ai/accounts?itemId={item_id}'
            headers = {
                'X-API-KEY': api_key,
                'accept': 'application/json'
            }
            response = requests.get(accounts_url, headers=headers)
            if response.status_code == 200:
                return jsonify(response.json())
            else:
                return jsonify({"error": f"Failed to fetch accounts. Status Code: {response.status_code}", "details": response.text}), response.status_code
        except Exception as e:
            return jsonify({"error": str(e)}), 500