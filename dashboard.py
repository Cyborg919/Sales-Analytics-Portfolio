import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Intelligence Dashboard", layout="wide")
st.title("📊 Sales Intelligence Dashboard")
st.caption("Portfolio project — synthetic retail dataset")

df = pd.read_csv("sales_data.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

regions = st.sidebar.multiselect("Region", sorted(df["Region"].unique()), default=sorted(df["Region"].unique()))
cats = st.sidebar.multiselect("Category", sorted(df["Category"].unique()), default=sorted(df["Category"].unique()))

f = df[df["Region"].isin(regions) & df["Category"].isin(cats)]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Net Sales", f"₹{f['Net_Sales_INR'].sum():,.0f}")
c2.metric("Profit", f"₹{f['Profit_INR'].sum():,.0f}")
c3.metric("Orders", f"{len(f):,}")
c4.metric("Profit Margin", f"{f['Profit_INR'].sum()/f['Net_Sales_INR'].sum()*100:.1f}%")

monthly = f.groupby(f["Order_Date"].dt.to_period("M").astype(str), as_index=False)["Net_Sales_INR"].sum()
st.plotly_chart(px.line(monthly, x="Order_Date", y="Net_Sales_INR", title="Monthly Net Sales"), use_container_width=True)

cat = f.groupby("Category", as_index=False)["Net_Sales_INR"].sum().sort_values("Net_Sales_INR", ascending=False)
st.plotly_chart(px.bar(cat, x="Category", y="Net_Sales_INR", title="Sales by Category"), use_container_width=True)

region = f.groupby("Region", as_index=False)["Profit_INR"].sum().sort_values("Profit_INR", ascending=False)
st.plotly_chart(px.bar(region, x="Region", y="Profit_INR", title="Profit by Region"), use_container_width=True)
