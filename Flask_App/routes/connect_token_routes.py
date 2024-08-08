from flask import Blueprint, jsonify, request
import requests
from Flask_App.config import Config
from Flask_App.routes.get_key_routes import get_api_key

connect_token_bp = Blueprint('connect_token', __name__)

@connect_token_bp.route("/connect_token", methods=["POST"])
# Route to handle POST requests for creating a connect token
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