import streamlit as st
import pandas as pd
import joblib

# Load model safely
try:
    model = joblib.load("churn_model.pkl")
except Exception as e:
    st.error("Model loading failed. Please upload correct model.")
    st.stop()

st.set_page_config(page_title="Customer Churn App", layout="centered")

st.title("🚀 Customer Churn Prediction App")

st.markdown("### Enter Customer Details")

# Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
total = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)

# Predict button
if st.button("Predict Churn"):

    input_data = pd.DataFrame({
        "gender": [gender],
        "SeniorCitizen": [senior],
        "Partner": [partner],
        "Dependents": [dependents],
        "tenure": [tenure],
        "MonthlyCharges": [monthly],
        "TotalCharges": [total]
    })

    try:
        prediction = model.predict(input_data)[0]

        if prediction == 1:
            st.error("⚠️ Customer is likely to churn")
        else:
            st.success("✅ Customer will stay")

    except Exception as e:
        st.error("Prediction failed. Model mismatch.")
