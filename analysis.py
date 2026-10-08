import pandas as pd

df = pd.read_csv("sales_data.csv", parse_dates=["Order_Date"])

df["Profit_Margin"] = df["Profit_INR"] / df["Net_Sales_INR"] * 100
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

print("\n=== KPI SUMMARY ===")
print(f"Orders: {len(df):,}")
print(f"Net Sales: ₹{df['Net_Sales_INR'].sum():,.2f}")
print(f"Profit: ₹{df['Profit_INR'].sum():,.2f}")
print(f"Profit Margin: {df['Profit_INR'].sum()/df['Net_Sales_INR'].sum()*100:.2f}%")
print(f"Average Order Value: ₹{df['Net_Sales_INR'].mean():,.2f}")
print(f"Return Rate: {(df['Returned'].eq('Yes').mean()*100):.2f}%")

print("\n=== SALES BY REGION ===")
print(df.groupby("Region")["Net_Sales_INR"].sum().sort_values(ascending=False))

print("\n=== SALES BY CATEGORY ===")
print(df.groupby("Category")["Net_Sales_INR"].sum().sort_values(ascending=False))

print("\n=== PROFIT BY CHANNEL ===")
print(df.groupby("Channel")["Profit_INR"].sum().sort_values(ascending=False))

print("\n=== MONTHLY SALES ===")
print(df.groupby("Month")["Net_Sales_INR"].sum().sort_values(ascending=False).head(12))
