# src/register.py
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "tft.db"



def ask_int(prompt, min_v=1, max_v=8):
    while True:
        try:
            v = int(input(prompt).strip())
            if min_v <= v <= max_v:
                return v
            print(f"Colocação precisa ser entre {min_v} e {max_v}.")
        except ValueError:
            print("Digite um número inteiro.")

def ask_text(prompt, allow_empty=False):
    while True:
        v = input(prompt).strip()
        if v or allow_empty:
            return v
        print("Não pode ser vazio.")

def register_match():
    print("\n=== Registrar Partida de TFT ===")
    patch = ask_text("Patch da partida (ex: 14.2): ")
    placement = ask_int("Colocação (1–8): ")
    portal = ask_text("Portal inicial: ")
    print("\nDigite os 3 augments (pressione Enter se não houver):")
    augment1 = ask_text("Augment 1: ", allow_empty=True)
    augment2 = ask_text("Augment 2: ", allow_empty=True)
    augment3 = ask_text("Augment 3: ", allow_empty=True)
    composition = ask_text("Composição (nome simples): ")

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO matches (patch, placement, portal, augment1, augment2, augment3, composition)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (patch, placement, portal, augment1, augment2, augment3, composition))
    conn.commit()
    conn.close()
    print("✔ Partida registrada com sucesso!\n")

if __name__ == "__main__":
    register_match()
