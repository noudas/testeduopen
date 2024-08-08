# db_create_pessoa.py

'''
This function, `create_pessoas_table`, is responsible for creating a table named 'pessoas' in the database. 
It takes a database connection object (`conn`) as its parameter, which is used to interact with the database.

Steps performed by the function:
1. Creates a new cursor object from the provided connection. Cursors are database control structures that allow executing SQL commands.
2. Defines a SQL query string (`create_table_query`) to create the 'pessoas' table if it doesn't already exist. 
   - The table has five columns: 'id', 'cpf', 'idade', and 'aceita_termos'. 
   - 'id' is a primary key, ensuring uniqueness and not null values.
   - 'cpf' must be unique and cannot be null.
   - 'idade' must be at least 18 years old.
   - 'aceita_termos' defaults to false and cannot be null.
3. Executes the SQL command using the cursor object. If successful, commits the transaction and prints a success message.
4. Encloses the execution in a try-except-finally block to handle any exceptions that might occur during the process.
   - If an exception occurs, it prints an error message detailing the issue.
5. Ensures the cursor is closed after the operation, regardless of whether it was successful or an exception occurred, by placing the cursor close operation in a finally block.

This function is crucial for setting up the initial database schema, allowing subsequent data insertion and retrieval operations.
'''

def create_pessoas_table(conn):
    cursor = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS pessoas (
        id SERIAL PRIMARY KEY,
        cpf VARCHAR(11) UNIQUE NOT NULL,
        idade INTEGER CHECK (idade >= 18),
        aceita_termos BOOLEAN NOT NULL DEFAULT FALSE
    );
    """

    try:
        cursor.execute(create_table_query)
        conn.commit()
        print("Tabela criada com sucesso.")
    except Exception as e:
        print(f"Erro ao criar a tabela: {e}")
    finally:
        cursor.close()
