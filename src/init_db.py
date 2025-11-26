# src/init_db.py
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "tft.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    print("🔄 Resetando o banco...")

    # Droppa a tabela inteira
    cur.execute("DROP TABLE IF EXISTS matches")

    # Recria a tabela já com campo 'patch'
    cur.execute("""
        CREATE TABLE matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            placement INTEGER NOT NULL,
            patch TEXT,
            portal TEXT,
            augment1 TEXT,
            augment2 TEXT,
            augment3 TEXT,
            composition TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # índices úteis
    cur.execute("CREATE INDEX idx_portal ON matches(portal)")
    cur.execute("CREATE INDEX idx_composition ON matches(composition)")
    cur.execute("CREATE INDEX idx_patch ON matches(patch)")

    conn.commit()
    conn.close()
    print(f"✔ Banco recriado do zero em {DB_PATH}")

if __name__ == "__main__":
    init_db()
