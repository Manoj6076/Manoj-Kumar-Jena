import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# Page config
st.set_page_config(
    page_title="RLV Anomaly Analytics",
    layout="wide",
)

# -----------------------------
# Sidebar (Settings Panel)
# -----------------------------
st.sidebar.title("⚙️ Settings")

uploaded_file = st.sidebar.file_uploader(
    "Upload Telemetry CSV",
    type=["csv"]
)

# -----------------------------
# Main Title
# -----------------------------
st.markdown(
    "<h1 style='text-align: center;'>🚀 RLV Telemetry Anomaly Dashboard</h1>",
    unsafe_allow_html=True
)

st.markdown("---")

# -----------------------------
# Main Logic
# -----------------------------
if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    # Sidebar Feature Selection
    st.sidebar.subheader("Select Telemetry Features")
    selected_features = st.sidebar.multiselect(
        "",
        df.columns.tolist()
    )

    run_model = st.sidebar.button("🚀 Run Model")

    # Data Preview Section
    st.subheader("📊 Telemetry Data Preview")
    st.dataframe(df.head())

    # -----------------------------
    # Run ML Model
    # -----------------------------
    if run_model and len(selected_features) > 0:

        X = df[selected_features]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        model = IsolationForest(
            contamination=0.05,
            random_state=42
        )

        df["Anomaly"] = model.fit_predict(X_scaled)

        anomalies = df[df["Anomaly"] == -1]

        total_points = len(df)
        total_anomalies = len(anomalies)
        anomaly_rate = (total_anomalies / total_points) * 100

        st.markdown("---")
        st.subheader("📈 Anomaly Detection Results")

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Data Points", total_points)
        col2.metric("Total Anomalies", total_anomalies)
        col3.metric("Anomaly Rate (%)", f"{anomaly_rate:.2f}%")

        st.markdown("---")

        # Flight Decision
        st.subheader("🛰 Flight Requalification Status")

        if anomaly_rate < 3:
            st.success("SAFE FOR REUSE")
        elif anomaly_rate < 8:
            st.warning("REQUIRES INSPECTION")
        else:
            st.error("NOT SAFE FOR REUSE")

        # Visualization
        st.markdown("---")
        st.subheader("📉 Anomaly Visualization")

        feature_to_plot = selected_features[0]

        fig, ax = plt.subplots()
        ax.plot(df[feature_to_plot])
        ax.scatter(
            anomalies.index,
            anomalies[feature_to_plot],
            color="red"
        )
        ax.set_title(f"{feature_to_plot} with Anomalies")
        st.pyplot(fig)

        # Anomaly Table
        st.markdown("---")
        st.subheader("🚨 Detected Anomalies")
        st.dataframe(anomalies)

else:
    st.info("Upload a CSV file from the sidebar to begin.")