import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("business_dashboard.csv")

# Title
st.title("Global Business Dashboard")

# Sidebar Filters
city = st.sidebar.selectbox(
    "Select City",
    df["City"].unique()
)

category = st.sidebar.selectbox(
    "Select Category",
    df["Category"].unique()
)

# Filter dataset
filtered_df = df[
    (df["City"] == city) &
    (df["Category"] == category)
]


# KPIs
total_sales = filtered_df["Total_Sales"].sum()
total_profit = filtered_df["Profit"].sum()

st.metric("Total Sales", f"${total_sales:,.2f}")
st.metric("Total Profit", f"${total_profit:,.2f}")

# Sales by Sub-Category
sales_subcategory = filtered_df.groupby("Sub_Category")["Total_Sales"].sum()

fig, ax = plt.subplots()

sales_subcategory.plot(kind="bar", ax=ax)

plt.title("Total_Sales by Sub_Category")

st.pyplot(fig)

# Top Customers
top_customers = filtered_df.groupby("Customer_Name")["Total_Sales"] \
                           .sum() \
                           .sort_values(ascending=False) \
                           .head(5)

st.write("Top 5 Customers by Sales")

st.dataframe(top_customers)