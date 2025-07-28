
import sqlite3

def get_connection():
    conn = sqlite3.connect("pos_data.db")
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT UNIQUE,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        stock INTEGER DEFAULT 0
    )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
