import psycopg2
from dotenv import load_dotenv

import os

load_dotenv()

def get_db_connection():
  conn = None
  try:
    conn = psycopg2.connect(
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    print("Conexão com o banco de dados estabelecida.")
  except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
  return conn