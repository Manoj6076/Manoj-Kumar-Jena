import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="RLV Anomaly Dashboard", layout="wide")

st.title("🚀 AI RLV Anomaly Detection Dashboard")
st.markdown("Reusable Launch Vehicle Telemetry Monitoring System")

# -----------------------------
# FILE UPLOAD
# -----------------------------
uploaded_file = st.file_uploader("Upload Telemetry CSV", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Raw Data")
    st.dataframe(df.head())

    # -----------------------------
    # DATA PREPROCESSING
    # -----------------------------
    numeric_cols = df.select_dtypes(include=np.number).columns

    if len(numeric_cols) == 0:
        st.error("No numeric data found!")
    else:
        X = df[numeric_cols]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # -----------------------------
        # MODEL (Isolation Forest)
        # -----------------------------
        model = IsolationForest(contamination=0.03, random_state=42)
        df['anomaly'] = model.fit_predict(X_scaled)

        df['anomaly'] = df['anomaly'].map({1: 0, -1: 1})

        # -----------------------------
        # METRICS
        # -----------------------------
        total = len(df)
        anomalies = df['anomaly'].sum()
        anomaly_rate = anomalies / total

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Records", total)
        col2.metric("Anomalies Detected", anomalies)
        col3.metric("Anomaly Rate", f"{anomaly_rate:.2%}")

        # -----------------------------
        # SAFETY DECISION
        # -----------------------------
        st.subheader("🧠 Safety Decision")

        if anomaly_rate < 0.03:
            st.success("✅ Vehicle SAFE for Reuse")
        else:
            st.error("⚠️ Further Inspection Required")

        # -----------------------------
        # VISUALIZATION
        # -----------------------------
        st.subheader("📈 Telemetry Visualization")

        selected_feature = st.selectbox("Select Feature", numeric_cols)

        fig, ax = plt.subplots()
        ax.plot(df[selected_feature], label="Normal")

        anomaly_points = df[df['anomaly'] == 1]
        ax.scatter(anomaly_points.index,
                   anomaly_points[selected_feature],
                   color='red', label="Anomaly")

        ax.legend()
        st.pyplot(fig)

        # -----------------------------
        # ANOMALY TABLE
        # -----------------------------
        st.subheader("🚨 Detected Anomalies")
        st.dataframe(df[df['anomaly'] == 1])

        # -----------------------------
        # DOWNLOAD REPORT
        # -----------------------------
        csv = df.to_csv(index=False).encode('utf-8')

        st.download_button(
            "⬇️ Download Anomaly Report",
            csv,
            "anomaly_report.csv",
            "text/csv"
        )
