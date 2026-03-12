import streamlit as st
import pandas as pd
import os

st.title("RLV Telemetry Anomaly Analytics")

# Get project root directory
BASE_DIR = os.getcwd()

# Dataset path
data_path = os.path.join(BASE_DIR, "data", "telemetry.csv")

# Read dataset
data = pd.read_csv(data_path)

st.dataframe(data.head())
