# src/stats.py
import pandas as pd

def compute_stats(matches):
    if not matches:
        return None, None, None

    df = pd.DataFrame(matches)

    # média por portal
    portal_stats = (
        df.groupby("portal")["placement"]
        .mean()
        .reset_index()
        .rename(columns={"placement": "avg_placement"})
        .sort_values("avg_placement")
    )

    # média por composição
    comp_stats = (
        df.groupby("composition")["placement"]
        .mean()
        .reset_index()
        .rename(columns={"placement": "avg_placement"})
        .sort_values("avg_placement")
    )

    # média por augment
    aug_df = pd.melt(
        df,
        id_vars=["placement"],
        value_vars=["augment1", "augment2", "augment3"],
        value_name="augment"
    ).dropna(subset=["augment"])

    aug_stats = (
        aug_df.groupby("augment")["placement"]
        .mean()
        .reset_index()
        .rename(columns={"placement": "avg_placement"})
        .sort_values("avg_placement")
    )

    return portal_stats, comp_stats, aug_stats
