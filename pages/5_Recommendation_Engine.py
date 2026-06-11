import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Recommendation Engine",
    page_icon="🎁",
    layout="wide"
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🎁 AI Recommendation Engine")

st.markdown("""
Generate personalized product recommendations
based on customer profile and spending behavior.
""")

st.markdown("---")

# --------------------------------------------------
# INPUTS
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    age = st.slider(
        "Customer Age",
        18,
        70,
        30
    )

    income = st.slider(
        "Customer Income",
        20000,
        150000,
        50000,
        step=1000
    )

with col2:

    spending_score = st.slider(
        "Spending Score",
        1,
        100,
        50
    )

    monthly_visits = st.slider(
        "Monthly Visits",
        1,
        50,
        10
    )

st.markdown("---")

# --------------------------------------------------
# GENERATE RECOMMENDATIONS
# --------------------------------------------------

if st.button(
    "🎯 Generate Recommendations",
    use_container_width=True
):

    # VIP Customers

    if income > 100000 and spending_score > 70:

        recommendation_type = "VIP"

        products = [
            "MacBook Pro",
            "iPhone 16 Pro",
            "Apple Watch Ultra",
            "Premium Membership",
            "Travel Credit Card"
        ]

        st.success("""
### 🌟 VIP Customer

Recommended Products

• MacBook Pro

• iPhone 16 Pro

• Apple Watch Ultra

• Premium Membership

• Travel Credit Card

Expected Conversion Rate: 92%
""")

    # Premium Customers

    elif income > 70000:

        recommendation_type = "Premium"

        products = [
            "Samsung Galaxy Ultra",
            "Smart Watch",
            "Fitness Subscription",
            "Business Backpack",
            "Headphones"
        ]

        st.info("""
### 🚀 Premium Customer

Recommended Products

• Samsung Galaxy Ultra

• Smart Watch

• Fitness Subscription

• Business Backpack

• Headphones

Expected Conversion Rate: 78%
""")

    # Budget Customers

    else:

        recommendation_type = "Budget"

        products = [
            "Earphones",
            "Wallet",
            "T-Shirts",
            "Cashback Coupons",
            "Discount Bundles"
        ]

        st.warning("""
### 💡 Budget Customer

Recommended Products

• Earphones

• Wallet

• T-Shirts

• Cashback Coupons

• Discount Bundles

Expected Conversion Rate: 55%
""")

    st.markdown("---")

    # --------------------------------------------------
    # RECOMMENDATION TABLE
    # --------------------------------------------------

    st.subheader("📋 Recommended Products")

    recommendations_df = pd.DataFrame({
        "Product": products,
        "Priority": [1, 2, 3, 4, 5]
    })

    st.dataframe(
        recommendations_df,
        use_container_width=True
    )

    st.markdown("---")

    # --------------------------------------------------
    # CUSTOMER SUMMARY
    # --------------------------------------------------

    st.subheader("👤 Customer Summary")

    summary_df = pd.DataFrame({
        "Feature": [
            "Age",
            "Income",
            "Spending Score",
            "Monthly Visits",
            "Customer Type"
        ],
        "Value": [
            age,
            income,
            spending_score,
            monthly_visits,
            recommendation_type
        ]
    })

    st.dataframe(
        summary_df,
        use_container_width=True
    )

    st.markdown("---")

    # --------------------------------------------------
    # AI INSIGHTS
    # --------------------------------------------------

    st.subheader("🧠 AI Recommendation Insights")

    st.success(f"""
Customer Category: {recommendation_type}

• Product recommendations are generated using customer purchasing behavior.

• Customers with higher income and spending scores tend to purchase premium products.

• Personalized recommendations improve conversion rates and customer retention.

• AI-driven targeting helps businesses maximize revenue opportunities.

• Recommended products are prioritized based on customer profile.
""")

    st.markdown("---")

    # --------------------------------------------------
    # DOWNLOAD REPORT
    # --------------------------------------------------

    csv = recommendations_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="📥 Download Recommendation Report",
        data=csv,
        file_name="recommendation_report.csv",
        mime="text/csv"
    )

    st.success(
        "Recommendation Report Generated Successfully"
    )