"""
Project 1 — Call Center Performance & CSAT Analysis
Author: Khattab Salim
Reads call_center_tickets.csv, computes operational KPIs, and produces
CSAT trend, handle-time vs CSAT, and team-performance visualizations.
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/call_center_tickets.csv", parse_dates=["date"])

# --- KPIs ---
kpis = {
    "Total tickets": len(df),
    "Avg CSAT (1-5)": round(df.csat.mean(), 2),
    "CSAT % (4-5)": round((df.csat >= 4).mean() * 100, 1),
    "Avg handle time (min)": round(df.handle_time_min.mean(), 1),
    "FCR %": round(df.first_contact_resolution.mean() * 100, 1),
    "Escalation %": round(df.escalated.mean() * 100, 1),
}
print("KPIs:", kpis)

# --- Monthly CSAT trend ---
monthly = (df.set_index("date")
             .groupby(pd.Grouper(freq="ME"))
             .agg(csat=("csat", "mean"),
                  fcr=("first_contact_resolution", "mean")))
print("\nMonthly:\n", monthly)

# --- Team performance ---
team = df.groupby("team").agg(
    csat_pct=("csat", lambda s: (s >= 4).mean() * 100),
    fcr_pct=("first_contact_resolution", lambda s: s.mean() * 100),
    avg_aht=("handle_time_min", "mean"))
print("\nTeam performance:\n", team.round(1))

# Insight: correlation between handle time and CSAT
print("\nCorr(handle_time, csat):", round(df.handle_time_min.corr(df.csat), 3))
