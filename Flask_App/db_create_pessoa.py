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
