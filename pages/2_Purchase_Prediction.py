import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Purchase Prediction",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Purchase Prediction")

st.markdown("""
Predict customer purchasing behavior using AI-driven analytics.

This module estimates purchase probability and suggests products.
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    age = st.slider(
        "Customer Age",
        min_value=18,
        max_value=70,
        value=30
    )

    income = st.slider(
        "Customer Income",
        min_value=20000,
        max_value=150000,
        value=50000,
        step=1000
    )

with col2:

    spending = st.slider(
        "Spending Score",
        min_value=1,
        max_value=100,
        value=50
    )

    visits = st.slider(
        "Monthly Visits",
        min_value=1,
        max_value=50,
        value=10
    )

st.markdown("---")

if st.button(
    "🚀 Generate Purchase Prediction",
    use_container_width=True
):

    probability = (
        (income / 150000) * 40
        + (spending / 100) * 40
        + (visits / 50) * 20
    )

    probability = round(probability, 2)

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=probability,
            title={
                "text": "Purchase Probability (%)"
            },
            gauge={
                "axis": {
                    "range": [0, 100]
                }
            }
        )
    )

    fig.update_layout(height=400)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.metric(
        "Predicted Purchase Probability",
        f"{probability}%"
    )

    st.markdown("---")

    if probability >= 80:

        st.success("""
### 🌟 Premium Customer

Recommended Products

• MacBook Pro

• iPhone 16

• Apple Watch

• Premium Membership

Expected Conversion Rate: 90%
""")

    elif probability >= 60:

        st.info("""
### 🚀 Growth Customer

Recommended Products

• Android Flagship Phone

• Smart Watch

• Backpack

• Fitness Subscription

Expected Conversion Rate: 75%
""")

    elif probability >= 40:

        st.warning("""
### 🎯 Moderate Customer

Recommended Products

• Headphones

• Shoes

• Wallet

• Discount Bundle

Expected Conversion Rate: 60%
""")

    else:

        st.error("""
### 💡 Budget Customer

Recommended Products

• Earphones

• T-Shirts

• Coupons

• Cashback Offers

Expected Conversion Rate: 40%
""")

    st.markdown("---")

    summary_df = pd.DataFrame({
        "Feature": [
            "Age",
            "Income",
            "Spending Score",
            "Monthly Visits"
        ],
        "Value": [
            age,
            income,
            spending,
            visits
        ]
    })

    st.subheader("📋 Customer Analysis Summary")

    st.dataframe(
        summary_df,
        use_container_width=True
    )

    st.success(
        "Purchase Prediction Generated Successfully"
    )