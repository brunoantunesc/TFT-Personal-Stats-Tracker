# src/app.py
from flask import Flask, render_template, request
from db import get_connection
import pandas as pd

app = Flask(__name__)

def load_filters():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT DISTINCT portal FROM matches WHERE portal IS NOT NULL")
    portals = [row[0] for row in cur.fetchall()]

    # pegar augments de 3 colunas diferentes
    cur.execute("SELECT augment1, augment2, augment3 FROM matches")
    rows = cur.fetchall()
    augment_set = set()
    for a1, a2, a3 in rows:
        for a in (a1, a2, a3):
            if a and a.strip():
                augment_set.add(a)
    augments = sorted(augment_set)

    cur.execute("SELECT DISTINCT composition FROM matches WHERE composition IS NOT NULL")
    compositions = [row[0] for row in cur.fetchall()]

    conn.close()
    return portals, augments, compositions


def build_query_filter(portal, augment, composition):
    conditions = []
    params = []

    if portal and portal != "Todos":
        conditions.append("portal = ?")
        params.append(portal)

    if composition and composition != "Todos":
        conditions.append("composition = ?")
        params.append(composition)

    if augment and augment != "Todos":
        conditions.append("(augment1 = ? OR augment2 = ? OR augment3 = ?)")
        params.extend([augment, augment, augment])

    where_clause = " WHERE " + " AND ".join(conditions) if conditions else ""
    return where_clause, params


@app.route("/", methods=["GET"])
def index():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM matches", conn)

    # ---- Filtros ----
    portal = request.args.get("portal")
    augment = request.args.get("augment")
    patch = request.args.get("patch")

    filtered = df.copy()

    if portal and portal != "Todos":
        filtered = filtered[filtered["portal"] == portal]

    if augment and augment != "Todos":
        filtered = filtered[
            (filtered["augment1"] == augment) |
            (filtered["augment2"] == augment) |
            (filtered["augment3"] == augment)
        ]

    if patch and patch != "Todos":
        filtered = filtered[filtered["patch"] == patch]

    # ---- Estatística por composição ----
    tmp = filtered.groupby("composition").agg(
        avg_placement=("placement", "mean"),
        plays=("placement", "count")
    ).reset_index()

    comp_stats = [
        (row["composition"], row["avg_placement"], row["plays"])
        for _, row in tmp.iterrows()
    ]

    # ---- Valores para selects ----
    portals = ["Todos"] + sorted(df["portal"].dropna().unique().tolist())

    # cria lista única de augments
    augments = sorted(
        set(df["augment1"].dropna()) |
        set(df["augment2"].dropna()) |
        set(df["augment3"].dropna())
    )
    augments = ["Todos"] + augments

    patches = ["Todos"] + sorted(df["patch"].dropna().unique().tolist())

    return render_template(
        "index.html",
        stats=comp_stats,
        portals=portals,
        augments=augments,
        patches=patches,
        selected_portal=portal or "Todos",
        selected_augment=augment or "Todos",
        selected_patch=patch or "Todos"
    )



if __name__ == "__main__":
    app.run(debug=True)
