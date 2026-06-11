import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Customer Intelligence Platform",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 3rem;
    font-weight: bold;
    color: #00ff99;
}

.sub-title {
    text-align: center;
    font-size: 1.2rem;
    color: #cccccc;
    margin-bottom: 30px;
}

.feature-box {
    background-color: #1e1e1e;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<p class="main-title">🤖 AI Customer Intelligence Platform</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Customer Analytics • Churn Prediction • Segmentation • Recommendations • Business Insights</p>',
    unsafe_allow_html=True
)

st.markdown("---")

# --------------------------------------------------
# INTRODUCTION
# --------------------------------------------------

st.markdown("""
### Welcome

This platform helps businesses:

✅ Analyze Customer Behavior

✅ Predict Purchase Probability

✅ Detect Churn Risk

✅ Segment Customers

✅ Generate Product Recommendations

✅ Discover Business Insights

---
""")

# --------------------------------------------------
# MODULE BUTTONS
# --------------------------------------------------

st.subheader("🚀 Launch Modules")

col1, col2, col3 = st.columns(3)

# COLUMN 1

with col1:

    if st.button(
        "📊 Dashboard",
        use_container_width=True
    ):
        st.switch_page("pages/1_Dashboard.py")

    st.write("Customer Analytics Dashboard")

    if st.button(
        "🧠 Purchase Prediction",
        use_container_width=True
    ):
        st.switch_page("pages/2_Purchase_Prediction.py")

    st.write("AI Purchase Probability Analysis")

# COLUMN 2

with col2:

    if st.button(
        "⚠️ Churn Analytics",
        use_container_width=True
    ):
        st.switch_page("pages/3_Churn_Analytics.py")

    st.write("Customer Retention Prediction")

    if st.button(
        "👥 Customer Segmentation",
        use_container_width=True
    ):
        st.switch_page("pages/4_Customer_Segmentation.py")

    st.write("K-Means Customer Clustering")

# COLUMN 3

with col3:

    if st.button(
        "🎁 Recommendation Engine",
        use_container_width=True
    ):
        st.switch_page("pages/5_Recommendation_Engine.py")

    st.write("Personalized Product Suggestions")

    if st.button(
        "📈 Insights Dashboard",
        use_container_width=True
    ):
        st.switch_page("pages/6_Insights_Dashboard.py")

    st.write("Advanced Business Intelligence")

st.markdown("---")

# --------------------------------------------------
# PLATFORM FEATURES
# --------------------------------------------------

st.subheader("📌 Platform Features")

feature_col1, feature_col2 = st.columns(2)

with feature_col1:

    st.info("""
📊 Customer Analytics Dashboard

🧠 Purchase Prediction

⚠️ Churn Prediction

👥 Customer Segmentation
""")

with feature_col2:

    st.info("""
🎁 Recommendation Engine

📈 Business Insights

📥 Download Reports

🤖 AI Driven Analytics
""")

st.markdown("---")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.success(
    "Click any module button above to start exploring customer intelligence."
)