'''
This function, `create_instituicao_table`, is responsible for creating a table named 'instituicoes' in the database. 
It accepts a database connection object as its parameter and uses this connection to execute SQL commands.

Steps performed by the function:
1. Creates a cursor object from the provided database connection. Cursors are database control structures that allow executing SQL statements and fetching data returned by those statements.
2. Defines a SQL query string to create the 'instituicoes' table if it doesn't already exist. The table schema includes various fields such as 'id', 'nome', 'primary_color', etc., each with specific data types and constraints like PRIMARY KEY, VARCHAR, CHAR, BOOLEAN, and TIMESTAMP WITH TIME ZONE.
3. Executes the SQL query using the cursor object. This operation attempts to create the table in the database according to the defined schema.
4. Commits the transaction to finalize the changes made by the SQL command. If the table creation is successful, it prints a success message.
5. Catches any exceptions that occur during the execution of the SQL command, printing an error message detailing the issue encountered.
6. Ensures the cursor is closed after the operation, regardless of whether it was successful or not, through a finally block. Properly closing cursors is important for releasing database resources efficiently.

Note: This function is designed to be called with a valid database connection object, ensuring that the database operations can be executed successfully.
'''

def create_instituicao_table(conn):
    cursor = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS instituicoes (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(255),
        primary_color CHAR(6),
        institution_url VARCHAR(255),
        pais CHAR(2),
        tipo VARCHAR(50),
        image_url VARCHAR(255),
        has_mfa BOOLEAN,
        oauth BOOLEAN,
        health_status VARCHAR(20),
        health_stage VARCHAR(50),
        created_at TIMESTAMP WITH TIME ZONE,
        is_sandbox BOOLEAN,
        is_open_finance BOOLEAN,
        updated_at TIMESTAMP WITH TIME ZONE,
        supports_payment_initiation BOOLEAN,
        supports_scheduled_payments BOOLEAN,
        supports_smart_transfers BOOLEAN
    );
    """

    try:
        cursor.execute(create_table_query)
        conn.commit()
        print("Tabela de instituições criada com sucesso.")
    except Exception as e:
        print(f"Erro ao criar a tabela de instituições: {e}")
    finally:
        cursor.close()
