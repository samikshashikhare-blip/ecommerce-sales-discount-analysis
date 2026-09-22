"""
Brazilian E-Commerce (Olist) Analysis

The script automatically uses the full dataset in data/raw/ when available.
Otherwise it uses the included related sample in data/sample/.

Run:
    python src/analysis.py
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
SAMPLE = ROOT / "data" / "sample"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

def load_data(folder, sample=False):
    if sample:
        names = {
            "orders": "olist_orders_sample.csv",
            "items": "olist_order_items_sample.csv",
            "customers": "olist_customers_sample.csv",
            "products": "olist_products_sample.csv",
            "reviews": "olist_order_reviews_sample.csv",
            "translation": "product_category_name_translation.csv",
        }
    else:
        names = {
            "orders": "olist_orders_dataset.csv",
            "items": "olist_order_items_dataset.csv",
            "customers": "olist_customers_dataset.csv",
            "products": "olist_products_dataset.csv",
            "reviews": "olist_order_reviews_dataset.csv",
            "translation": "product_category_name_translation.csv",
        }

    return {
        key: pd.read_csv(folder / filename)
        for key, filename in names.items()
    }

use_sample = not (RAW / "olist_orders_dataset.csv").exists()
data = load_data(SAMPLE if use_sample else RAW, sample=use_sample)

orders = data["orders"]
items = data["items"]
customers = data["customers"]
products = data["products"]
reviews = data["reviews"]
translation = data["translation"]

for c in [
    "order_purchase_timestamp",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]:
    orders[c] = pd.to_datetime(orders[c], errors="coerce")

items["item_total"] = items["price"] + items["freight_value"]

enriched = (
    items
    .merge(
        orders[[
            "order_id",
            "order_purchase_timestamp",
            "order_delivered_customer_date",
            "order_estimated_delivery_date"
        ]],
        on="order_id",
        how="left"
    )
    .merge(
        products[["product_id", "product_category_name"]],
        on="product_id",
        how="left"
    )
    .merge(
        translation,
        on="product_category_name",
        how="left"
    )
)

enriched["category"] = (
    enriched["product_category_name_english"]
    .fillna(enriched["product_category_name"])
    .fillna("Unknown")
)

enriched["delivery_days"] = (
    enriched["order_delivered_customer_date"]
    - enriched["order_purchase_timestamp"]
).dt.total_seconds() / 86400

summary = {
    "orders": orders["order_id"].nunique(),
    "customers": customers["customer_unique_id"].nunique(),
    "sales": items["price"].sum(),
    "freight": items["freight_value"].sum(),
    "average_review": reviews["review_score"].mean(),
    "median_delivery_days": enriched["delivery_days"].median(),
}

print("\nOlist E-Commerce Analysis")
print("-------------------------")
print("Data source:", "sample included in repository" if use_sample else "full Olist dataset")

for key, value in summary.items():
    if isinstance(value, float):
        print(f"{key}: {value:,.2f}")
    else:
        print(f"{key}: {value:,}")

category = (
    enriched.groupby("category")["price"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

category.to_csv(OUT / "category_sales_from_script.csv")

plt.figure(figsize=(9, 5))
category.sort_values().plot(kind="barh")
plt.title("Top 10 Categories by Sales")
plt.xlabel("Sales")
plt.tight_layout()
plt.savefig(OUT / "category_sales_from_script.png", dpi=160)
plt.close()

print("\nAnalysis completed. See outputs/.")
