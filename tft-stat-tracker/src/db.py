# src/db.py
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "tft.db"

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def fetch_all_matches():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM matches ORDER BY created_at DESC")
    rows = cur.fetchall()

    columns = [col[0] for col in cur.description]
    conn.close()

    return [dict(zip(columns, row)) for row in rows]
