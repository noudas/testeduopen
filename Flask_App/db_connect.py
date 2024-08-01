'''
This script establishes a connection to a PostgreSQL database using environment variables for credentials and details. It utilizes the `psycopg2` library for database connectivity and `dotenv` for loading environment variables from a `.env` file.

Imports:
- `psycopg2`: A PostgreSQL adapter for Python, enabling communication with PostgreSQL databases.
- `load_dotenv`: A function from the `dotenv` package, used to load environment variables from a `.env` file into the system environment.
- `os`: Provides a way of using operating system dependent functionality, such as reading environment variables.

After importing the necessary libraries, `load_dotenv()` is called to load environment variables from a `.env` file located in the root of the project. This step ensures that sensitive information like database credentials can be securely managed outside of the source code.

The `get_db_connection()` function attempts to establish a connection to a PostgreSQL database:
1. It initializes a variable `conn` to `None`, which will later hold the database connection object.
2. In a `try` block, it uses `psycopg2.connect()` to attempt to connect to the database using credentials obtained from environment variables (`DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`). These variables are expected to be set in the `.env` file.
3. Upon successful connection, it prints a confirmation message.
4. If any exception occurs during the connection process, it catches the exception, prints an error message detailing the issue, and returns `None`.

The function then returns the connection object (`conn`) if the connection was successful, or `None` if there was an error. This connection object can be used to interact with the database.

'''

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