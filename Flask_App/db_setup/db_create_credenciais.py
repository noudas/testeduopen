# db_create_credenciais.py

'''
The `create_credenciais_table` function is responsible for creating a table named 'credenciais' in the database. 
It takes a database connection object (`conn`) as its parameter and performs the following operations:
1. Creates a cursor object from the provided connection to interact with the database.
2. Defines a SQL query string to create the 'credenciais' table if it doesn't already exist. 
   - The table has several columns: 'id', 'institution_id', 'validation', 'validation_message', 'label', 'name', 'tipo', 'placeholder', and 'optional'. 
   - Notably, 'institution_id' is a foreign key referencing the 'id' column in another table ('instituicoes'), enforcing referential integrity.
3. Executes the SQL query through the cursor object. If successful, commits the transaction and prints a success message.
4. Catches any exceptions that occur during the execution of the SQL query, printing an error message detailing the exception.
5. Ensures the cursor is closed after the operation, regardless of whether it was successful or not, to free up resources.

This function is crucial for setting up the database schema, allowing the application to store and manage credential information associated with institutions.
'''

def create_credenciais_table(conn):
    cursor = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS credenciais (
    id SERIAL PRIMARY KEY,
    institution_id INT REFERENCES instituicoes(id),
    validation VARCHAR(255),
    validation_message TEXT,
    label VARCHAR(50),
    name VARCHAR(50),
    tipo VARCHAR(50),
    placeholder VARCHAR(100),
    optional BOOLEAN
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
