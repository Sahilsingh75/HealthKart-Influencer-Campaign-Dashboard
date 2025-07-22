# 💼 HealthKart Influencer Campaign Dashboard

The goal is to build a working dashboard that tracks influencer campaign performance, computes ROAS (Return on Ad Spend), tracks payouts, and provides actionable insights.

---

## 📊 Features

- Influencer performance by revenue, orders, and ROAS
- Payout analysis and ROAS summary
- Filtering by platform and gender
- Download filtered report as CSV
- Uses simulated campaign data

---

## 🧱 Project Structure

Healthkart_Dashboard/
├── app.py # Streamlit dashboard code
├── data_simulation.py # Script to generate simulated CSV data
├── influencers.csv # Simulated influencer data
├── posts.csv # Simulated post data
├── tracking_data.csv # Simulated campaign tracking
├── payouts.csv # Simulated payouts
└── README.md # This file



---

## ⚙️ How to Run Locally

### Step 1: Clone or Download This Repository

```
git clone https://github.com/yourusername/HealthKart-Influencer-Campaign-Dashboard.git
cd HealthKart-Influencer-Campaign-Dashboard
```

Step 2: Set Up Python Environment
Make sure you have Python 3.8+ and pip installed.

Install dependencies:
```
pip install streamlit pandas numpy
```

Step 3: Generate the Data
Run the simulation script once to generate the .csv files:
```
python data_simulation.py
```

Step 4: Run the Streamlit App
```
streamlit run app.py
```
Open your browser at http://localhost:8501/ to view the dashboard.

The dashboard is deployed on https://healthkart-dashboard.streamlit.app/ 
