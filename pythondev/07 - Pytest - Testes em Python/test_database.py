import pytest
import sqlite3

@pytest.fixture
def db_connection():
    """
    Fixtures que configura uma conexão com o banco de dados SQLite
    temporário e garante a limpeza dos recursos após o teste.
    """
    conn = sqlite3.connect(":memory:") #Cria um banco de dados em memória
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE users(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
        """
    )

    conn.commit()
    yield conn, cursor

    conn.close()


def test_database_insert(db_connection):
    """
    Testa a inserção de um usuario na tabela users
    do banco sqlite
    """
    conn, cursor = db_connection

    cursor.execute(
        """
        INSERT INTO users (name, email)
        VALUES (?,?)
        """, ("Jhon Doe", "jhondoe@example.com")
    )

    conn.commit()

    # Verificar a inserção

    cursor.execute("SELECT * FROM users WHERE email = ?", ("jhondoe@example.com",))
    user = cursor.fetchone()

    # assert user is None
    assert user[1] == "Jhon Doe"
    assert user[2] == "jhondoe@example.com"

def test_database_duplicate_emails(db_connection):
    """
    Testa a inserção de users com emails duplicados
    """

    conn, cursor = db_connection

    cursor.execute(
        """
        INSERT INTO users (name, email)
        VALUES (?,?)
        """, ("Jane Smith", "janesmith@example.com")
    )
    conn.commit()

    # Verificar tentativa de email duplicado
    with pytest.raises(sqlite3.IntegrityError):
            cursor.execute(
        """
        INSERT INTO users (name, email)
        VALUES (?,?)
        """, ("Duplicate User", "janesmith@example.com")
    )
    conn.commit()


