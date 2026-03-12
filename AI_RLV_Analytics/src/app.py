import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

st.title("🚀 RLV Telemetry Anomaly Analytics Dashboard")

# Upload dataset instead of fixed path
uploaded_file = st.file_uploader("Upload Telemetry Dataset", type=["csv"])

if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)

    st.subheader("Telemetry Dataset Preview")
    st.dataframe(data.head())

    model = IsolationForest(contamination=0.05)
    model.fit(data)

    if st.button("Run Anomaly Detection"):

        prediction = model.predict(data)
        data["Anomaly"] = prediction

        st.subheader("Prediction Result")
        st.write(data)

        st.subheader("Altitude vs Velocity Graph")

        normal = data[data["Anomaly"] == 1]
        anomaly = data[data["Anomaly"] == -1]

        fig, ax = plt.subplots()

        ax.scatter(normal["Altitude"], normal["Velocity"], label="Normal")
        ax.scatter(anomaly["Altitude"], anomaly["Velocity"], label="Anomaly")

        ax.set_xlabel("Altitude")
        ax.set_ylabel("Velocity")
        ax.legend()

        st.pyplot(fig)
