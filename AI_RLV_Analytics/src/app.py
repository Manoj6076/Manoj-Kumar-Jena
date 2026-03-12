import streamlit as st
import pandas as pd

st.title("RLV Telemetry Anomaly Analytics")

data = pd.read_csv("AI_RLV_Analytics/data/rlv_telemetry.csv")

st.write(data.head())


