from flask import Flask
from . import db_create_item, db_create_pessoa, routes
from .db_connect import get_db_connection

def create_app():
    app = Flask(__name__)

    conn = get_db_connection()
    if conn:
        print("Conectado ao DB com sucesso.")
        db_create_item.create_itens_table(conn)
        db_create_pessoa.create_pessoas_table(conn)
    else:
        print("Falha ao conectar com o DB.")

    routes.init_app(app)
    return app