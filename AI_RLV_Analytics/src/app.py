import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

st.title("🚀 RLV Telemetry Anomaly Analytics Dashboard")

# Load dataset
data = pd.read_csv("AI_RLV_Analytics/data/rlv_telemetry.csv")

# Dataset preview
st.subheader("Telemetry Dataset Preview")
st.dataframe(data.head())

# Train anomaly detection model
model = IsolationForest(contamination=0.05)
model.fit(data)

# Run detection button
if st.button("Run Anomaly Detection"):

    prediction = model.predict(data)
    data["Anomaly"] = prediction

    st.subheader("Prediction Results")
    st.write(data)

    # Count anomalies
    anomaly_count = (data["Anomaly"] == -1).sum()

    st.metric("Detected Anomalies", anomaly_count)

    # Altitude vs Velocity graph
    st.subheader("Altitude vs Velocity Anomaly Graph")

    normal = data[data["Anomaly"] == 1]
    anomaly = data[data["Anomaly"] == -1]

    fig, ax = plt.subplots()

    ax.scatter(normal["Altitude"], normal["Velocity"], label="Normal")
    ax.scatter(anomaly["Altitude"], anomaly["Velocity"], label="Anomaly")

    ax.set_xlabel("Altitude")
    ax.set_ylabel("Velocity")
    ax.legend()

    st.pyplot(fig)

    # Temperature chart
    st.subheader("Temperature Trend")
    st.line_chart(data["Temperature"])

    # Vibration chart
    st.subheader("Vibration Trend")
    st.line_chart(data["Vibration"])
    
