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
