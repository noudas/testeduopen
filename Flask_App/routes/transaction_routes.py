from flask import Blueprint, jsonify, request
import requests
from Flask_App.config import Config
from Flask_App.routes.get_key_routes import get_api_key

transaction_bp = Blueprint('transaction', __name__)

@transaction_bp.route("/transactions/<accountId>", methods=["GET"])
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
