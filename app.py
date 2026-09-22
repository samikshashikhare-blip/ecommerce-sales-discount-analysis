import streamlit as st
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent
df = pd.read_csv(ROOT / "data" / "sample_sales.csv", parse_dates=["order_date"])

st.set_page_config(page_title="E-Commerce Sales Dashboard", layout="wide")
st.title("E-Commerce Sales & Discount Analysis")
st.caption("A beginner-friendly Data Science portfolio project")

# Filters
col1, col2, col3 = st.columns(3)
with col1:
    categories = st.multiselect("Category", sorted(df["category"].unique()),
                                default=sorted(df["category"].unique()))
with col2:
    regions = st.multiselect("Region", sorted(df["region"].unique()),
                             default=sorted(df["region"].unique()))
with col3:
    max_discount = st.slider("Maximum discount", 0, 30, 30)

filtered = df[
    df["category"].isin(categories)
    & df["region"].isin(regions)
    & (df["discount"] <= max_discount / 100)
]

m1, m2, m3, m4 = st.columns(4)
m1.metric("Orders", f"{len(filtered):,}")
m2.metric("Units", f"{filtered['units'].sum():,}")
m3.metric("Sales", f"₹{filtered['sales'].sum():,.0f}")
m4.metric("Profit", f"₹{filtered['profit'].sum():,.0f}")

st.subheader("Sales by Category")
category_sales = filtered.groupby("category")["sales"].sum().sort_values(ascending=False)
st.bar_chart(category_sales)

st.subheader("Monthly Sales")
monthly = filtered.assign(month=filtered["order_date"].dt.to_period("M").astype(str))
monthly = monthly.groupby("month")["sales"].sum()
st.line_chart(monthly)

st.subheader("Discount Analysis")
discounted = filtered.copy()
discounted["discount_band"] = pd.cut(
    discounted["discount"],
    bins=[-0.001, 0.05, 0.15, 0.25, 0.31],
    labels=["0-5%", "5-15%", "15-25%", "25%+"]
)
band = discounted.groupby("discount_band", observed=False)["profit"].sum()
st.bar_chart(band)

st.info(
    "This repository includes a small sample dataset so the project runs immediately. "
    "For a real-world version, replace data/sample_sales.csv with a permitted real dataset "
    "and update the data-loading section if its columns differ."
)
