import streamlit as st
import pandas as pd

st.title("AI RLV Anomaly Detection System")

uploaded_file = st.file_uploader("Upload Telemetry CSV", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write(data.head())
