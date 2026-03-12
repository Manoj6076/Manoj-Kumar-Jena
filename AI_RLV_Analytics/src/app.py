import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

st.title("🚀 RLV Telemetry Anomaly Analytics Dashboard")

# Load dataset
data = pd.read_csv("data/telemetry.csv")

st.subheader("Telemetry Dataset")
st.dataframe(data.head())

# Train anomaly detection model
model = IsolationForest(contamination=0.05)
model.fit(data)

if st.button("Run Anomaly Detection"):
    
    prediction = model.predict(data)
    data["Anomaly"] = prediction
    
    st.subheader("Anomaly Detection Result")
    st.write(data)

    # Graph visualization
    st.subheader("Altitude vs Velocity")

    fig, ax = plt.subplots()
    
    normal = data[data["Anomaly"] == 1]
    anomaly = data[data["Anomaly"] == -1]

    ax.scatter(normal["Altitude"], normal["Velocity"], label="Normal")
    ax.scatter(anomaly["Altitude"], anomaly["Velocity"], label="Anomaly")

    ax.set_xlabel("Altitude")
    ax.set_ylabel("Velocity")
    ax.legend()

    st.pyplot(fig)
