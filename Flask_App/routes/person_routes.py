from flask import Blueprint, jsonify, request
from Flask_App.db_connect import get_db_connection
from Flask_App.routes.get_key_routes import get_api_key

person_bp = Blueprint('person', __name__)

@person_bp.route("/pessoas", methods=["POST"])
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