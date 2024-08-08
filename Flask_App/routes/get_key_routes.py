# Import necessary modules and configurations
from flask import jsonify, request
import requests
from Flask_App.config import Config


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