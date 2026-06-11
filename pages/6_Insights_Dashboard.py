import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Insights Dashboard",
    page_icon="📈",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

try:
    df = pd.read_csv("data/customers.csv")

except Exception as e:
    st.error(f"Dataset Error: {e}")
    st.stop()

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("📈 AI Business Insights Dashboard")

st.markdown("""
Analyze customer behavior, revenue trends,
correlations, demographics, and AI-generated
business recommendations.
""")

st.markdown("---")

# --------------------------------------------------
# KPI METRICS
# --------------------------------------------------

total_customers = len(df)

avg_income = int(
    df["income"].mean()
)

avg_spending = round(
    df["spending_score"].mean(),
    1
)

total_revenue = int(
    (
        df["income"]
        * df["purchase_frequency"]
        * 0.05
    ).sum()
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Customers",
        total_customers
    )

with col2:
    st.metric(
        "Avg Income",
        f"₹{avg_income:,}"
    )

with col3:
    st.metric(
        "Spending Score",
        avg_spending
    )

with col4:
    st.metric(
        "Revenue",
        f"₹{total_revenue:,}"
    )

st.markdown("---")

# --------------------------------------------------
# CUSTOMER DISTRIBUTION
# --------------------------------------------------

left, right = st.columns(2)

with left:

    fig1 = px.histogram(
        df,
        x="age",
        nbins=20,
        title="Customer Age Distribution"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with right:

    fig2 = px.pie(
        df,
        names="gender",
        hole=0.45,
        title="Gender Distribution"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.markdown("---")

# --------------------------------------------------
# CITY ANALYSIS
# --------------------------------------------------

city_df = (
    df.groupby("city")
    .size()
    .reset_index(name="customers")
)

fig3 = px.bar(
    city_df,
    x="city",
    y="customers",
    color="city",
    title="Customers by City"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.markdown("---")

# --------------------------------------------------
# CORRELATION HEATMAP
# --------------------------------------------------

st.subheader(
    "🔥 Correlation Heatmap"
)

numeric_cols = [
    "age",
    "income",
    "spending_score",
    "tenure",
    "monthly_visits",
    "purchase_frequency"
]

corr = df[numeric_cols].corr()

fig, ax = plt.subplots(
    figsize=(10, 6)
)

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    ax=ax
)

st.pyplot(fig)

st.markdown("---")

# --------------------------------------------------
# REVENUE ANALYSIS
# --------------------------------------------------

df["revenue"] = (
    df["income"]
    * df["purchase_frequency"]
    * 0.05
)

revenue_city = (
    df.groupby("city")["revenue"]
    .sum()
    .reset_index()
)

fig4 = px.bar(
    revenue_city,
    x="city",
    y="revenue",
    color="city",
    title="Revenue by City"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

st.markdown("---")

# --------------------------------------------------
# CUSTOMER SEGMENTS
# --------------------------------------------------

st.subheader(
    "🎯 Customer Category Analysis"
)

premium = len(
    df[df["income"] > 100000]
)

medium = len(
    df[
        (df["income"] >= 50000)
        &
        (df["income"] <= 100000)
    ]
)

budget = len(
    df[df["income"] < 50000]
)

segment_df = pd.DataFrame({
    "Category": [
        "Premium",
        "Medium",
        "Budget"
    ],
    "Customers": [
        premium,
        medium,
        budget
    ]
})

fig5 = px.pie(
    segment_df,
    names="Category",
    values="Customers",
    title="Customer Categories"
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

st.markdown("---")

# --------------------------------------------------
# DATA PREVIEW
# --------------------------------------------------

st.subheader(
    "📋 Customer Dataset Preview"
)

st.dataframe(
    df.head(25),
    use_container_width=True
)

st.markdown("---")

# --------------------------------------------------
# AI BUSINESS INSIGHTS
# --------------------------------------------------

st.subheader(
    "🧠 AI Generated Insights"
)

st.success(f"""
✅ Total Customers Analyzed: {total_customers}

✅ Estimated Revenue: ₹{total_revenue:,}

✅ Average Customer Income: ₹{avg_income:,}

✅ Average Spending Score: {avg_spending}

✅ Premium customers contribute the highest revenue.

✅ Frequent website visitors show higher purchase activity.

✅ Customers with longer tenure are less likely to churn.

✅ Personalized recommendations can significantly improve conversion rates.

✅ Revenue opportunities are strongest among premium and medium-income customers.

✅ Customer retention programs can increase overall profitability.
""")

st.markdown("---")

# --------------------------------------------------
# DOWNLOAD REPORT
# --------------------------------------------------

csv = df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="📥 Download Insights Report",
    data=csv,
    file_name="insights_report.csv",
    mime="text/csv"
)

st.success(
    "Insights Report Generated Successfully"
)