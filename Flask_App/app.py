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
