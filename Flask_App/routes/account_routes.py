from flask import Blueprint, jsonify, request
import requests
from Flask_App.config import Config
from Flask_App.routes.get_key_routes import get_api_key

account_bp = Blueprint('account', __name__)

@account_bp.route("/accounts/<item_id>", methods=["GET"])
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