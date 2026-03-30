# 🚀 RLV Telemetry Anomaly Analytics

### 🛰️ Reusable Launch Vehicle Safety Monitoring Dashboard

An interactive **Machine Learning–powered anomaly detection system** built using **Streamlit** to analyze Reusable Launch Vehicle (RLV) telemetry data and assist in post-flight safety decisions.

---

## 🌐 Live Application

👉 **Access the Dashboard:**
🔗 https://rlv-anomaly-dashboard.streamlit.app/

---

## 📌 Project Overview

Reusable Launch Vehicles generate large volumes of telemetry data such as:

* 🌡️ Temperature
* ⚙️ Pressure
* 📳 Vibration

### 🔍 This project provides:

* 📂 Telemetry CSV upload
* 🤖 Isolation Forest anomaly detection
* 📊 Interactive visualization dashboard
* 🧠 Safety decision engine
* ⬇️ Downloadable anomaly report

---

## 🏗️ System Architecture

### 🔄 Runtime Flow

```
👤 User (Browser)
        ↓
🌐 Streamlit Web App
        ↓
🖥️ Streamlit Server (app.py)
        ↓
📊 Data Processing Layer
(Pandas, NumPy, StandardScaler)
        ↓
🤖 Machine Learning Model
(Isolation Forest)
        ↓
📈 Visualization Layer
(Metrics, Graphs, Reports)
        ↓
📤 Output to User
```

---

## 🧠 Architecture Explanation

1. 👤 User accesses dashboard via browser
2. 🖥️ Streamlit handles UI & interactions
3. 📊 Data processed using Pandas & NumPy
4. ⚖️ Features scaled using StandardScaler
5. 🤖 Isolation Forest detects anomalies
6. 📈 Results visualized in dashboard
7. 🧠 Safety decision generated
8. 📤 Output returned dynamically

---

## 🤖 Machine Learning Model

### 🔍 Isolation Forest (Unsupervised Learning)

### ✅ Why Isolation Forest?

* ❌ No labeled data required
* ⚡ Efficient for large datasets
* 🎯 Detects rare anomalies
* 🚀 Ideal for telemetry monitoring

---

## 🧠 Safety Decision Logic

```
If anomaly_rate < 0.03
    ✅ Vehicle SAFE for Reuse
Else
    ⚠️ Further Inspection Required
```

---

## ⚙️ How to Run the Project

### 📥 Clone Repository

```bash
git clone https://github.com/Manoj6076/Manoj-Kumar-Jena
cd AI_RLV_Analytics
```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Run Application

```bash
streamlit run src/app.py
```

---

## 📦 Requirements

```
streamlit
pandas
numpy
matplotlib
scikit-learn
```

---

## 📸 Demo

🚀 Live Demo Available:
https://rlv-anomaly-dashboard.streamlit.app/

---

## 🌍 Applications

* 🛰️ Aerospace vehicle health monitoring
* 🚀 Launch vehicle reuse assessment
* 🔧 Predictive maintenance
* 🌐 Industrial IoT anomaly detection

---

## 👨‍💻 Author

**Manoj Kumar Jena**
🎓 Advanced School Of Advanced Computing (2025–27)

---

## 📜 License

This project is developed for **academic and educational purposes**.

---

## 🎯 Final Project Highlights

✔ End-to-end Machine Learning pipeline
✔ Real-time anomaly detection
✔ Interactive Streamlit dashboard
✔ Aerospace-inspired safety system
✔ Fully GitHub + Deployment ready

---

💡 *Built with ❤️ using Python, Machine Learning & Streamlit*
