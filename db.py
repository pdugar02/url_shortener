import sqlite3

DB_NAME="links.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS links(
                id         INTEGER     PRIMARY KEY AUTOINCREMENT,
                code       TEXT        NOT NULL UNIQUE,
                long_url   TEXT        NOT NULL,
                created_at TIMESTAMP   DEFAULT CURRENT_TIMESTAMP,
                expires_at TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

def get_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory=sqlite3.Row
    return conn