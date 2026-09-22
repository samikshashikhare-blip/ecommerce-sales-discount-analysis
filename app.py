from pathlib import Path
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "sample"

orders = pd.read_csv(DATA / "olist_orders_sample.csv", parse_dates=[
    "order_purchase_timestamp", "order_delivered_customer_date",
    "order_estimated_delivery_date"
])
items = pd.read_csv(DATA / "olist_order_items_sample.csv")
customers = pd.read_csv(DATA / "olist_customers_sample.csv")

st.set_page_config(page_title="Olist E-Commerce Dashboard", layout="wide")
st.title("Brazilian E-Commerce — Olist Dashboard")
st.caption("Portfolio dashboard built from a related sample of the public Olist dataset.")

# Merge for a simple interactive view.
df = items.merge(
    orders[[
        "order_id", "order_purchase_timestamp", "order_status",
        "customer_id"
    ]],
    on="order_id", how="left"
).merge(
    customers[["customer_id", "customer_state"]],
    on="customer_id", how="left"
)

categories = sorted(df["order_id"].dropna().unique())
states = sorted(df["customer_state"].dropna().unique())

c1, c2 = st.columns(2)
with c1:
    selected_states = st.multiselect(
        "Customer State",
        states,
        default=states
    )
with c2:
    status = st.multiselect(
        "Order Status",
        sorted(df["order_status"].dropna().unique()),
        default=sorted(df["order_status"].dropna().unique())
    )

filtered = df[
    df["customer_state"].isin(selected_states)
    & df["order_status"].isin(status)
]

m1, m2, m3, m4 = st.columns(4)
m1.metric("Orders", f"{filtered['order_id'].nunique():,}")
m2.metric("Items", f"{len(filtered):,}")
m3.metric("Sales", f"R$ {filtered['price'].sum():,.0f}")
m4.metric("Freight", f"R$ {filtered['freight_value'].sum():,.0f}")

st.subheader("Monthly Sales")
monthly = (
    filtered.assign(month=filtered["order_purchase_timestamp"].dt.to_period("M").astype(str))
            .groupby("month")["price"].sum()
)
st.line_chart(monthly)

st.subheader("Top Customer States")
state_sales = (
    filtered.groupby("customer_state")["price"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
)
st.bar_chart(state_sales)

st.info(
    "The original Olist dataset does not contain a direct discount field. "
    "This dashboard therefore does not invent a discount measure."
)
