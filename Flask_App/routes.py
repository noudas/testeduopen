from flask import jsonify
import requests
from .config import Config

def init_app(app):
    @app.route("/transacao/<conta_id>", methods=["GET"])
    def get_transacao(conta_id):
        client_ID = Config.PLUGGY_CLIENT_ID
        client_SECRET = Config.PLUGGY_CLIENT_SECRET
        url = f'https://api.pluggy.ai/api/v1/items/{conta_id}/transactions'
        headers = {'client_id': client_ID, 'client_secret': client_SECRET}

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": f"Erro ao buscar transações. Status Code: {response.status_code}", "details": response.text})