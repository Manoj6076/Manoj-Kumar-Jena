import streamlit as st
import pandas as pd
from pathlib import Path

st.title("RLV Telemetry Anomaly Analytics")

BASE_DIR = Path(__file__).resolve().parent.parent
data_path = BASE_DIR / "data" / "telemetry.csv"

data = pd.read_csv(data_path)

st.dataframe(data.head())



