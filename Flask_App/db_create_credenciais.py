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
