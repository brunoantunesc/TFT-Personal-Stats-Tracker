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
            print(f"Placement must be between {min_v} and {max_v}.")
        except ValueError:
            print("Please enter an integer.")


def ask_text(prompt, allow_empty=False):
    while True:
        v = input(prompt).strip()
        if v or allow_empty:
            return v
        print("This field cannot be empty.")


def register_one():
    """Ask fields for a single match and save it to the DB."""
    print("\n=== Register TFT Match ===")
    patch = ask_text("Match patch (e.g. 14.2): ")
    placement = ask_int("Placement (1–8): ")
    portal = ask_text("Starting portal: ")
    print("\nEnter the 3 augments (press Enter if none):")
    augment1 = ask_text("Augment 1: ", allow_empty=True)
    augment2 = ask_text("Augment 2: ", allow_empty=True)
    augment3 = ask_text("Augment 3: ", allow_empty=True)
    composition = ask_text("Composition name (simple): ")

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO matches (patch, placement, portal, augment1, augment2, augment3, composition)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (patch, placement, portal, augment1, augment2, augment3, composition),
    )
    conn.commit()
    conn.close()
    print("✔ Match registered successfully!\n")


def main():
    """
    Loop registering matches until the user chooses to exit.
    Rule: press Enter (empty input) to add another match,
    or type any other key (then Enter) to save and exit.
    """
    while True:
        register_one()
        choice = input("Press Enter to add a new game, or type any other key then Enter to save and exit: ").strip()
        if choice == "":
            # continue loop and register another match (asks all fields again)
            continue
        else:
            print("Saved. Exiting.")
            break


if __name__ == "__main__":
    main()
