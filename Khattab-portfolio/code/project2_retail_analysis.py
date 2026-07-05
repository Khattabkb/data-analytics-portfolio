"""
Project 2 — Retail Sales & Profitability Analysis
Author: Khattab Salim
Reads retail_orders.csv, computes sales/profit KPIs, monthly trend,
region breakdown, and discount-vs-profit analysis by category.
See sql/retail_analysis.sql for the equivalent SQL query set.
"""
import pandas as pd

df = pd.read_csv("../data/retail_orders.csv", parse_dates=["order_date"])

# --- Headline KPIs ---
kpis = {
    "Total sales (AED)": round(df.sales.sum(), 0),
    "Total profit (AED)": round(df.profit.sum(), 0),
    "Profit margin %": round(df.profit.sum() / df.sales.sum() * 100, 1),
    "Orders": len(df),
    "Avg order value": round(df.sales.mean(), 0),
}
print("KPIs:", kpis)

# --- Sales & margin by region ---
region = df.groupby("region").agg(
    sales=("sales", "sum"), profit=("profit", "sum"))
region["margin_pct"] = (region.profit / region.sales * 100).round(1)
print("\nBy region:\n", region.round(0))

# --- Discount impact by category (key insight) ---
disc = (df.groupby(["category", "discount"])
          .profit.mean().round(2)
          .unstack("discount"))
print("\nAvg profit per order by discount level:\n", disc)

# Flag loss-making segments
loss = df[df.profit < 0].groupby("category").agg(
    orders=("order_id", "count"), total_loss=("profit", "sum"))
print("\nLoss-making orders by category:\n", loss.round(0))
