import sqlite3

def get_connection():
    return sqlite3.connect("cinema.db")

def create_tables():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS sessoes (
                id INTEGER PRIMARY KEY,
                filme TEXT,
                capacidade INTEGER,
                publico_atual INTEGER
            )
        """)
        # Seed inicial para teste
        cursor = conn.cursor()
        if not cursor.execute("SELECT id FROM sessoes").fetchone():
            conn.execute("INSERT INTO sessoes (id, filme, capacidade, publico_atual) VALUES (1, 'Batman', 100, 0)")