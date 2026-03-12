import streamlit as st
import pandas as pd

st.title("AI RLV Anomaly Detection")

data = pd.read_csv("data/telemetry.csv")

st.write(data.head())
