import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="Churn Analytics",
    page_icon="⚠️",
    layout="wide"
)

st.title("⚠️ Customer Churn Analytics")

st.write(
    "Predict whether a customer is likely to churn."
)

# Load Model
try:
    model = joblib.load("models/churn_model.pkl")
except Exception as e:
    st.error(f"Unable to load model: {e}")
    st.stop()

# Inputs
col1, col2 = st.columns(2)

with col1:
    income = st.number_input(
        "Income",
        min_value=0,
        value=50000
    )

    spending = st.slider(
        "Spending Score",
        1,
        100,
        50
    )

with col2:
    tenure = st.slider(
        "Tenure",
        1,
        10,
        5
    )

    visits = st.slider(
        "Monthly Visits",
        1,
        50,
        10
    )

purchase_frequency = st.slider(
    "Purchase Frequency",
    1,
    30,
    10
)

if st.button("Analyze Churn"):

    features = np.array([
        [
            income,
            spending,
            tenure,
            visits,
            purchase_frequency
        ]
    ])

    prediction = model.predict(features)[0]

    probability = model.predict_proba(features)[0][1]

    churn_score = round(
        probability * 100,
        2
    )

    st.metric(
        "Churn Probability",
        f"{churn_score}%"
    )

    if prediction == 1:
        st.error("High Churn Risk")
    else:
        st.success("Low Churn Risk")

    summary = pd.DataFrame({
        "Feature": [
            "Income",
            "Spending Score",
            "Tenure",
            "Monthly Visits",
            "Purchase Frequency"
        ],
        "Value": [
            income,
            spending,
            tenure,
            visits,
            purchase_frequency
        ]
    })

    st.dataframe(
        summary,
        use_container_width=True
    )