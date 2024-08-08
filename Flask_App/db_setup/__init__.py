# db_stetup/__init__.py

from .db_create_pessoa import create_pessoas_table
from .db_create_instituicao import create_instituicao_table
from .db_create_credenciais import create_credenciais_table
from Flask_App.db_connect import get_db_connection

def initialize_database():
    """
    Initializes the database by creating all necessary tables.
    """
    connection = get_db_connection()
    try:
        create_pessoas_table(connection)
        create_instituicao_table(connection)
        create_credenciais_table(connection)
    except Exception as e:
        print(f"Erro ao inicializar o banco de dados: {e}")
    finally:
        connection.close()