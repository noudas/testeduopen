from flask import jsonify, request
import requests

from Flask_App.db_connect import get_db_connection
from .config import Config

def get_api_key():
    """
    Autenticar e pegar a API key do Pluggy API.
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

def init_app(app):
    @app.route("/transacao/<item_id>", methods=["GET"])
    def get_transacao(item_id):
        client_ID = Config.PLUGGY_CLIENT_ID
        client_SECRET = Config.PLUGGY_CLIENT_SECRET
        
        # Obtendo o token de acesso
        auth_url = f"{Config.PLUGGY_API_BASE_URL}/auth"
        auth_response = requests.post(auth_url, json={
            "clientId": client_ID,
            "clientSecret": client_SECRET
        })

        if auth_response.status_code != 200:
            return jsonify({"error": "Falha na autenticação.", "details": auth_response.text}), auth_response.status_code

        access_token = auth_response.json()["accessToken"]

        # Recuperando transações
        transactions_url = f'{Config.PLUGGY_API_BASE_URL}/items/{item_id}/transactions'
        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        response = requests.get(transactions_url, headers=headers)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": f"Erro ao buscar transações. Status Code: {response.status_code}", "details": response.text})

    
    @app.route("/pessoas", methods=["POST"])
    def create_pessoa():
        data = request.json
        cpf = data.get("cpf")
        idade = data.get("idade")
        aceita_termos = data.get("aceita_termos")

        conn = get_db_connection()
        cursor = conn.cursor()

        insert_query = """
        INSERT INTO pessoas (cpf, idade, aceita_termos)
        VALUES (%s, %s, %s)
        RETURNING id;
        """

        try:
            cursor.execute(insert_query, (cpf, idade, aceita_termos))
            conn.commit()
            pessoa_id = cursor.fetchone()[0]
            return jsonify({"id": pessoa_id}), 201
        except Exception as e:
            return jsonify({"error": f"Erro ao criar pessoa: {e}"}), 500
        finally:
            cursor.close()
            conn.close()

    @app.route("/connect_token", methods=["POST"])
    def create_connect_token():
        client_ID = Config.PLUGGY_CLIENT_ID
        client_SECRET = Config.PLUGGY_CLIENT_SECRET

        # Obtendo o token de acesso
        auth_url = f"{Config.PLUGGY_API_BASE_URL}/auth"
        auth_response = requests.post(auth_url, json={
            "clientId": client_ID,
            "clientSecret": client_SECRET
        })

        if auth_response.status_code != 200:
            return jsonify({"error": "Falha na autenticação.", "details": auth_response.text}), auth_response.status_code

        access_token = auth_response.json()["accessToken"]

        # Criando connect token
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
            return jsonify({"error": f"Erro ao criar connect token. Status Code: {response.status_code}", "details": response.text})

    @app.route("/connectors", methods=["GET"])
    def get_connectors():
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
                return jsonify({"error": f"Erro ao buscar conectores. Status Code: {response.status_code}", "details": response.text}), response.status_code
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route("/connectors/<int:connector_id>", methods=["GET"])
    def get_connector(connector_id):
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
                return jsonify({"error": "Conector não encontrado."}), 404
            else:
                return jsonify({"error": f"Erro ao buscar conector. Status Code: {response.status_code}", "details": response.text}), response.status_code
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route("/connectors/<int:connector_id>/validate", methods=["POST"])
    def validate_connector(connector_id):
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