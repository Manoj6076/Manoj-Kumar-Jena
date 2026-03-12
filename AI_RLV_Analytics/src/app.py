import streamlit as st
import pandas as pd
import joblib

st.title("RLV Telemetry Anomaly Analytics")

# Load dataset
data = pd.read_csv("data/telemetry.csv")

st.subheader("Telemetry Data")
st.dataframe(data.head())

# Load ML model
model = joblib.load("model/anomaly_model.pkl")

# Run prediction
if st.button("Run Anomaly Detection"):
    prediction = model.predict(data)
    data["Anomaly"] = prediction
    st.subheader("Prediction Result")
    st.write(data)
