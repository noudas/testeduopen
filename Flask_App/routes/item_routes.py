from flask import Blueprint, jsonify, request
import requests
from Flask_App.config import Config
from Flask_App.routes.get_key_routes import get_api_key

item_bp = Blueprint('item', __name__)

@item_bp.route("/items/<item_id>", methods=["GET"])
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