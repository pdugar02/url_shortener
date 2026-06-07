from datetime import datetime as dt, timezone
from db import get_db
import sqlite3

def create_link(code: str, long_url: str, expires_at: dt):
    conn = get_db()
    row = conn.execute("INSERT INTO links (code, long_url expires_at) VALUES (?, ?, ?, ?)",
    [code, long_url, expires_at])
    conn.commit()
    return get_link(code)

def get_link(code: str):
    conn = get_db()
    row = conn.execute("SELECT * FROM links WHERE code = ?", [code]).fetchone()
    if not row:
        return None
    if row["expires_at"] and dt.fromisoformat(row["expires_at"])<dt.now(timezone.utc):
        return None
    return row
