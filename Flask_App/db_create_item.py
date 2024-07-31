def create_itens_table(conn):
    cursor = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS items (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        description TEXT,
        price DECIMAL(10, 2)
    );
    """

    try:
        cursor.execute(create_table_query)
        conn.commit()
        print("Table criada com sucesso.")
    except Exception as e:
        print(f"Error criando a table: {e}")
    finally:
        cursor.close()
