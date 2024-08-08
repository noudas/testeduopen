from flask import Blueprint, jsonify, request
import requests
from Flask_App.config import Config
from Flask_App.routes.get_key_routes import get_api_key

connector_bp = Blueprint('connector', __name__)

# Route to handle GET requests for retrieving all available connectors
@connector_bp.route("/connectors", methods=["GET"])
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
@connector_bp.route("/connectors/<int:connector_id>", methods=["GET"])
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
@connector_bp.route("/connectors/<int:connector_id>/validate", methods=["POST"])
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
