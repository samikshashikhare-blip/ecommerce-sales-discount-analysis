"""
E-Commerce Sales & Discount Analysis
-------------------------------------
Run:
    python src/analysis.py

Outputs are saved in the outputs/ folder.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sample_sales.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["order_date"])

# Basic metrics
summary = pd.DataFrame({
    "Metric": [
        "Total Orders",
        "Total Units",
        "Total Sales",
        "Total Profit",
        "Average Order Value",
        "Average Discount"
    ],
    "Value": [
        len(df),
        df["units"].sum(),
        round(df["sales"].sum(), 2),
        round(df["profit"].sum(), 2),
        round(df["sales"].mean(), 2),
        round(df["discount"].mean() * 100, 2)
    ]
})
summary.to_csv(OUT / "summary_metrics.csv", index=False)

# Category analysis
category_summary = (
    df.groupby("category", as_index=False)
      .agg(
          orders=("order_id", "count"),
          units=("units", "sum"),
          sales=("sales", "sum"),
          profit=("profit", "sum"),
          avg_discount=("discount", "mean")
      )
      .sort_values("sales", ascending=False)
)
category_summary.to_csv(OUT / "category_summary.csv", index=False)

# Discount analysis
discount_summary = (
    df.assign(
        discount_band=pd.cut(
            df["discount"],
            bins=[-0.001, 0.05, 0.15, 0.25, 0.31],
            labels=["0-5%", "5-15%", "15-25%", "25%+"]
        )
    )
    .groupby("discount_band", observed=False, as_index=False)
    .agg(
        orders=("order_id", "count"),
        sales=("sales", "sum"),
        profit=("profit", "sum"),
        avg_sales=("sales", "mean")
    )
)
discount_summary.to_csv(OUT / "discount_analysis.csv", index=False)

# Monthly trend
monthly = (
    df.assign(month=df["order_date"].dt.to_period("M").astype(str))
      .groupby("month", as_index=False)
      .agg(sales=("sales", "sum"), profit=("profit", "sum"))
)
monthly.to_csv(OUT / "monthly_sales.csv", index=False)

# Charts
plt.figure(figsize=(9, 5))
plt.bar(category_summary["category"], category_summary["sales"])
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=25)
plt.tight_layout()
plt.savefig(OUT / "sales_by_category.png", dpi=150)
plt.close()

plt.figure(figsize=(9, 5))
plt.plot(monthly["month"], monthly["sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=60)
plt.tight_layout()
plt.savefig(OUT / "monthly_sales_trend.png", dpi=150)
plt.close()

plt.figure(figsize=(9, 5))
plt.bar(discount_summary["discount_band"].astype(str), discount_summary["profit"])
plt.title("Profit by Discount Band")
plt.xlabel("Discount Band")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig(OUT / "profit_by_discount_band.png", dpi=150)
plt.close()

print("Analysis completed.")
print(f"Results saved to: {OUT}")
