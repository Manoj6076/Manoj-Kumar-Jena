import streamlit as st
import pandas as pd

st.title("AI RLV Anomaly Detection System")

st.write("Telemetry Data Analysis")

data = pd.read_csv("data/telemetry.csv")

st.write(data.head())
