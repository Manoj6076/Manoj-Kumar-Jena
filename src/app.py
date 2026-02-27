import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest

# Page Config
st.set_page_config(
    page_title="RLV Anomaly Analytics",
    page_icon="🚀",
    layout="wide"
)

# Header
st.markdown("<h1 style='text-align: center;'>🚀 RLV Telemetry Anomaly Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar
st.sidebar.title("⚙ Settings")

uploaded_file = st.sidebar.file_uploader("Upload Telemetry CSV", type=["csv"])

# Generate default data if no upload
if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    np.random.seed(42)
    n = 500
    df = pd.DataFrame({
        "Temperature": np.random.normal(75, 5, n),
        "Pressure": np.random.normal(30, 2, n),
        "Vibration": np.random.normal(0.5, 0.1, n)
    })
    anomaly_indices = np.random.choice(n, 20)
    df.loc[anomaly_indices, "Temperature"] += 25

# Show Data
st.subheader("📊 Telemetry Data Preview")
st.dataframe(df.head(), use_container_width=True)

numeric_columns = df.select_dtypes(include=np.number).columns.tolist()

selected_features = st.sidebar.multiselect(
    "Select Telemetry Features",
    numeric_columns,
    default=numeric_columns
)

run_model = st.sidebar.button("🚀 Run Model")

if run_model:

    if len(selected_features) == 0:
        st.error("Please select at least one feature.")
    else:

        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(df[selected_features])

        model = IsolationForest(contamination=0.05, random_state=42)
        df["Anomaly"] = model.fit_predict(scaled_data)
        df["Anomaly"] = df["Anomaly"].map({1: 0, -1: 1})

        anomalies = df[df["Anomaly"] == 1]
        anomaly_rate = len(anomalies) / len(df)

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Records", len(df))
        col2.metric("Anomalies Detected", len(anomalies))
        col3.metric("Anomaly Rate", round(anomaly_rate, 4))

        st.markdown("---")

        st.subheader("🛰 Safety Decision")

        if anomaly_rate < 0.03:
            st.success("Vehicle Safe for Reuse")
        else:
            st.error("Further Inspection Required")

        st.markdown("---")

        st.subheader("📈 Telemetry Trend")

        fig, ax = plt.subplots()
        ax.plot(df[selected_features[0]])
        ax.scatter(anomalies.index, anomalies[selected_features[0]], color="red")
        st.pyplot(fig)

        st.subheader("📋 Anomaly Records")
        st.dataframe(anomalies, use_container_width=True)

        csv = anomalies.to_csv(index=False).encode("utf-8")
        st.download_button("⬇ Download Report", csv, "rlv_anomalies.csv", "text/csv")