import streamlit as st
import pandas as pd
import plotly.express as px

# Page Config
st.set_page_config(
    page_title="Customer Dashboard",
    layout="wide"
)

# Title
st.title("📊 Customer Analytics Dashboard")

# Load Data
try:
    df = pd.read_csv("data/customers.csv")
except FileNotFoundError:
    st.error("customers.csv not found. Run generate_dataset.py first.")
    st.stop()

# KPI Section
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Customers",
        len(df)
    )

with col2:
    st.metric(
        "Average Income",
        f"${int(df['income'].mean()):,}"
    )

with col3:
    st.metric(
        "Average Spending",
        round(df["spending_score"].mean(), 2)
    )

with col4:
    st.metric(
        "Average Visits",
        round(df["monthly_visits"].mean(), 2)
    )

st.divider()

# Spending Score Histogram
st.subheader("Customer Spending Distribution")

fig1 = px.histogram(
    df,
    x="spending_score",
    nbins=20,
    title="Spending Score Distribution"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# Income vs Spending
st.subheader("Income vs Spending Score")

fig2 = px.scatter(
    df,
    x="income",
    y="spending_score",
    color="gender",
    hover_data=["city"],
    title="Income vs Spending"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# City Distribution
st.subheader("Customers by City")

city_count = df["city"].value_counts().reset_index()
city_count.columns = ["City", "Customers"]

fig3 = px.bar(
    city_count,
    x="City",
    y="Customers",
    title="Customer Distribution by City"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# Category Distribution
st.subheader("Favorite Category Analysis")

fig4 = px.pie(
    df,
    names="favorite_category",
    title="Customer Preferred Categories"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# Revenue Analysis
st.subheader("Revenue Analysis")

revenue = df.groupby("city")["income"].sum().reset_index()

fig5 = px.bar(
    revenue,
    x="city",
    y="income",
    title="Revenue by City"
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

# Dataset Preview
st.subheader("Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)

# Download Button
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Dataset",
    data=csv,
    file_name="customers.csv",
    mime="text/csv"
)
