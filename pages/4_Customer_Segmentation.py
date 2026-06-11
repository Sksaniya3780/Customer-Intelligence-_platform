import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="👥",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🎯 Customer Segmentation")

st.markdown(
    "Analyze customer groups using AI-powered clustering."
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
# SIDEBAR
# --------------------------------------------------

st.sidebar.header("Segmentation Settings")

segments = st.sidebar.slider(
    "Number of Segments",
    min_value=2,
    max_value=6,
    value=4
)

# --------------------------------------------------
# KMEANS CLUSTERING
# --------------------------------------------------

kmeans = KMeans(
    n_clusters=segments,
    random_state=42,
    n_init=10
)

df["segment"] = kmeans.fit_predict(
    df[["income", "spending_score"]]
)

segment_names = {
    0: "Premium",
    1: "Regular",
    2: "Budget",
    3: "VIP",
    4: "Elite",
    5: "New"
}

df["Customer Segment"] = df["segment"].map(
    lambda x: segment_names.get(x, f"Group {x}")
)

# --------------------------------------------------
# METRICS
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Customers",
        len(df)
    )

with col2:
    st.metric(
        "Segments",
        segments
    )

with col3:
    st.metric(
        "Average Income",
        f"₹{int(df['income'].mean()):,}"
    )

st.markdown("---")

# --------------------------------------------------
# VISUALIZATION
# --------------------------------------------------

fig = px.scatter(
    df,
    x="income",
    y="spending_score",
    color="Customer Segment",
    hover_data=[
        "name",
        "city",
        "age"
    ],
    title="Customer Segmentation Analysis"
)

fig.update_layout(
    height=550
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.success(
    "Customer Segments Generated Successfully"
)

st.markdown("---")

# --------------------------------------------------
# TABLE
# --------------------------------------------------

st.subheader("Segmented Customer Records")

display_df = df[
    [
        "customer_id",
        "name",
        "age",
        "gender",
        "city",
        "income",
        "spending_score",
        "Customer Segment"
    ]
]

st.dataframe(
    display_df,
    use_container_width=True,
    height=450
)

# --------------------------------------------------
# DOWNLOAD REPORT
# --------------------------------------------------

csv = display_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="📥 Download Segmentation Report",
    data=csv,
    file_name="segmentation_report.csv",
    mime="text/csv"
)