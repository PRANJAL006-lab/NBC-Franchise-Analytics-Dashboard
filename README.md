# NBC-Franchise-Analytics-Dashboard
# 📊 Franchise Intelligence & Operational Dashboard for Nothing Before Coffee (NBC)

Welcome to the repository for the **Franchise Intelligence & Operational Dashboard** project built for **Nothing Before Coffee (NBC)**, a fast-growing international coffee franchise. This project was developed as a **final-year MCA submission** to demonstrate real-world data analytics, business intelligence, and dashboard deployment across a multi-branch retail environment.

---

## 📌 Project Overview

This dashboard provides NBC’s leadership with real-time insights into:

* Daily sales and branch-wise performance
* Staff (barista) efficiency metrics
* Customer satisfaction analytics (CSAT/NPS)
* Inventory levels and restock alerts
* Order flow and hourly transaction heatmaps

The platform is designed to support strategic decisions through visual, interactive analytics built with Python, Plotly Dash, and Power BI.

---

## 🛠️ Tech Stack

* **Python** – Data simulation, ETL, backend logic
* **Pandas/NumPy** – KPI generation & manipulation
* **Plotly Dash** – Frontend dashboard interface
* **Power BI** – Business layer visualizations (optional enhancement)
* **Excel/CSV** – Sample data simulation inputs

---

## 📁 Repository Structure

```
NBC-Dashboard/
│
├── 📂 data/
│   └── NBC_KPI_Data.csv            # Simulated dataset with KPIs across branches
│
├── 📂 dashboard/
│   ├── app.py                      # Main Dash app logic
│   └── components.py              # Layout & visuals
│
├── 📂 visualizations/
│   └── powerbi_dashboard.pbix     # Optional Power BI visuals (exported)
│
├── 📂 docs/
│   ├── screenshots/               # UI screenshots and PDF exports
│   └── NBC_Brochure_GROT2025.pdf  # GROT Award brochure (GrafanCon)
│
└── README.md                      # This file
```

---

## 🧪 Sample Data Simulation Code (Python)

```python
import pandas as pd
import random

def generate_simulated_kpi_data():
    branches = ['Mumbai', 'Delhi', 'Dubai', 'London', 'Paris']
    data = {
        'Branch': [],
        'BaristaEfficiency (%)': [],
        'CustomerSatisfaction (1–5)': [],
        'DailySales (INR)': [],
        'InventoryLevel (%)': [],
        'OrdersPerHour': []
    }
    for i in range(100):
        branch = random.choice(branches)
        data['Branch'].append(branch)
        data['BaristaEfficiency (%)'].append(random.randint(75, 95))
        data['CustomerSatisfaction (1–5)'].append(round(random.uniform(4.0, 4.9), 1))
        data['DailySales (INR)'].append(random.randint(9000, 18000))
        data['InventoryLevel (%)'].append(random.randint(50, 90))
        data['OrdersPerHour'].append(random.randint(45, 70))
    return pd.DataFrame(data)
```

---

## 📈 Dashboard Features

* ✅ Real-time data updates (simulated refresh)
* 📍 Multi-branch tracking across 10+ locations
* 📊 Dynamic charts: bar, scatter, funnel, line
* 📦 Inventory thresholds with restock alerts
* 🎯 Visual KPIs: revenue, efficiency, CSAT

---

## 🎖️ Recognition

This project has been shortlisted for the **GROT Award 2025 at GrafanCon** for its innovative dashboard strategy and brand-aligned execution.

---

## 👨‍💻 Author & Contact

**Pranjal Gurjar** – MCA Student, Data Analyst & Developer
📧 [gurjarpranjal.work@gmail.com](mailto:gurjarpranjal.work@gmail.com)
🔗 [LinkedIn](https://linkedin.com/in/pranjalgurjar)

Project supervised by **Prof. Seema Sharma**, Department of MCA

---

## 📄 License

This project is for academic and demonstrative purposes. For any commercial use or adaptation, please contact the author.

