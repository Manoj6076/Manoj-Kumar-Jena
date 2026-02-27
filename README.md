# RLV Telemetry Anomaly Analytics

### Reusable Launch Vehicle Safety Monitoring Dashboard

An interactive Machine Learning--powered anomaly detection system built
using Streamlit to analyze Reusable Launch Vehicle (RLV) telemetry data
and assist in post-flight safety decisions.

------------------------------------------------------------------------

## Project Overview

Reusable Launch Vehicles generate large volumes of telemetry data such
as:

-   Temperature\
-   Pressure\
-   Vibration

This project provides:

-   Telemetry CSV upload\
-   Isolation Forest anomaly detection\
-   Interactive visualization dashboard\
-   Safety decision engine\
-   Downloadable anomaly report

------------------------------------------------------------------------

## Application Output

After running the application locally, access it at:

https://manoj-kumar-jena-cst6wcj4zhbfjpboychqgn.streamlit.app/

------------------------------------------------------------------------


#  Updated System Architecture


## Runtime Architecture Flow

User (Browser)
      ↓
Streamlit URL (http://localhost:8501)
      ↓
Streamlit Server (src/app.py)
      ↓
Data Processing Layer
(Pandas, NumPy, Feature Selection, StandardScaler)
      ↓
Machine Learning Model
(Isolation Forest - Anomaly Detection)
      ↓
Visualization & Results Layer
(Metrics, Graphs, Anomaly Table, Download Button)
      ↓
Response Sent Back to Browser
(https://manoj-kumar-jena-cst6wcj4zhbfjpboychqgn.streamlit.app/)
------------------------------------------------------------------------

## Architecture Explanation

1.  User accesses the dashboard through a browser.
2.  Streamlit server handles UI rendering and user interactions.
3.  Data is processed using Pandas and NumPy.
4.  Features are scaled using StandardScaler.
5.  Isolation Forest detects anomalies.
6.  Metrics and graphs are displayed.
7.  Safety decision is generated.
8.  Results are returned to the browser dynamically.

------------------------------------------------------------------------

# Machine Learning Model

Isolation Forest (Unsupervised Anomaly Detection)

Why Isolation Forest?

-   No labeled data required\
-   Efficient for high-dimensional datasets\
-   Detects rare abnormal observations\
-   Suitable for telemetry anomaly detection

------------------------------------------------------------------------

# Safety Decision Logic

If anomaly_rate \< 0.03\
Vehicle Safe for Reuse\
Else\
Further Inspection Required

------------------------------------------------------------------------

# How to Run the Project

## Clone Repository

git clone `<https://github.com/Manoj6076/Manoj-Kumar-Jena>`{=html}\
cd `<C:\Users\manoj\AI_RLV_Analytics>`{=html}

## Install Dependencies

pip install -r requirements.txt

## Run Streamlit Application

streamlit run src/app.py

Open browser:

https://manoj-kumar-jena-cst6wcj4zhbfjpboychqgn.streamlit.app/

------------------------------------------------------------------------

# requirements.txt

streamlit\
pandas\
numpy\
matplotlib\
scikit-learn

------------------------------------------------------------------------

# Demo



------------------------------------------------------------------------

# Applications

-   Aerospace vehicle health monitoring\
-   Launch vehicle reuse assessment\
-   Predictive maintenance\
-   Industrial IoT anomaly detection

------------------------------------------------------------------------

# Author

Manoj Kumar Jena\
Advanced School Of Advanced Computing\
2025-27

------------------------------------------------------------------------

# License

This project is developed for academic and educational purposes.

------------------------------------------------------------------------

# Final Project Summary

This project demonstrates:

-   End-to-end Machine Learning pipeline\
-   Real-time anomaly detection\
-   Interactive Streamlit dashboard\
-   Aerospace-inspired safety decision system\
-   Complete GitHub-ready structure
