''' 
This script imports Flask, establishes a database connection, initializes database tables, and configures the application's routes. 

Imports:
- Flask: A lightweight WSGI web application framework. Serving as the foundation for this application.
- Database creation functions (`db_create_pessoa`, `db_create_credenciais`, `db_create_instituicao`) and routing setup (`routes`) from the current directory.
- `get_db_connection`: A function designed to establish a connection to the database.

Function `create_app()` orchestrates the initialization and configuration of the Flask application:
1. An instance of the Flask application is created.
2. Attempts to establish a connection to the database using `get_db_connection`.
   - If successful, prints a success message and proceeds to initialize the required database tables (`pessoas`, `instituicao`, `credenciais`) by passing the connection object to their respective creation functions.
   - If the connection fails, prints an error message.
3. Initializes the application's routes with the `init_app` method, linking them to the Flask application instance.
4. Returns the fully configured Flask application instance, ready for deployment or further customization.

Note: This script assumes the existence of certain modules and functions within the project structure, specifically those related to database operations and route management.
''' 

from flask import Flask
from . import db_create_pessoa, db_create_credenciais, db_create_instituicao , routes
from .db_connect import get_db_connection

def create_app():
    app = Flask(__name__)

    conn = get_db_connection()
    if conn:
        print("Conectado ao DB com sucesso.")
        db_create_pessoa.create_pessoas_table(conn)
        db_create_instituicao.create_instituicao_table(conn)
        db_create_credenciais.create_credenciais_table(conn)
    else:
        print("Falha ao conectar com o DB.")

    routes.init_app(app)
    return app
