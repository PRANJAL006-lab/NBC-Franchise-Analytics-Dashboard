# 📊 Franchise Intelligence & Operational Dashboard for Nothing Before Coffee (NBC)

Welcome to the **Franchise Intelligence & Operational Dashboard** project repository, developed for **Nothing Before Coffee (NBC)**. This full-stack business intelligence solution is part of a final-year MCA project by Pranjal Gurjar. It demonstrates how real-time operational data and KPIs can be centralized into an actionable dashboard using Python, Dash, and Power BI.

---

## 🧭 Table of Contents

* [Project Overview](#project-overview)
* [Tech Stack](#tech-stack)
* [Repository Structure](#repository-structure)
* [Features](#features)
* [Full Dashboard Code](#full-dashboard-code)
* [Data Sample](#data-sample)
* [Screenshots](#screenshots)
* [Deployment](#deployment)
* [Business Value](#business-value)
* [Author & Contact](#author--contact)
* [License](#license)

---

## 📌 Project Overview

In today's data-driven business environment, franchise chains like Nothing Before Coffee (NBC) face challenges managing decentralized data across locations. From real-time sales reporting to staff efficiency, centralized intelligence becomes critical for consistency, quality control, and strategic expansion. This project delivers a unified dashboard system designed to equip NBC with complete operational visibility across its rapidly growing footprint.

The dashboard integrates key functional areas:

* **Sales Intelligence:** Empower leadership with daily sales visibility and growth tracking.
* **Customer Experience Metrics:** Gauge satisfaction and turn feedback into measurable actions.
* **Inventory Monitoring:** Automate replenishment alerts and track consumption trends to minimize waste.
* **Staff Performance:** Monitor service metrics and correlate with operational performance.
* **Comparative Branch Benchmarking:** Enable fair evaluation of branch KPIs and drive localized strategy.

By simulating data for 500+ daily transactions across global cities, this solution models a realistic foundation for a franchise-wide BI deployment. It also demonstrates the future scalability of the platform to include predictive forecasting, integrated CRM hooks, and AI-driven decision support.

This implementation bridges the gap between raw operational data and strategic executive decisions—transforming franchise management from reactive to proactive.
NBC is a franchise-based coffee brand operating in over 15 cities globally. Managing sales, staffing, customer experience, and inventory required a unified, data-driven approach. This project delivers a centralized dashboard to:

* Monitor daily revenue by location
* Track barista efficiency shift-wise
* Visualize real-time CSAT feedback
* Alert managers for low inventory
* Analyze order flow and optimize staff planning

---

## 🛠️ Tech Stack

* **Backend:** Python (Pandas, NumPy, Random)
* **Frontend:** Dash by Plotly, HTML
* **Visualization:** Plotly Express (bar, line, scatter, funnel)
* **Database (simulated):** CSV/Excel
* **Extras:** Power BI, exportable filters

---

## 📁 Repository Structure

```
📦 NBC-Franchise-Analytics-Dashboard
├── data/
│   └── NBC_KPI_Data.csv
├── dashboard/
│   ├── app.py
│   └── components.py
├── visualizations/
│   └── powerbi_dashboard.pbix
├── docs/
│   ├── screenshots/
│   └── NBC_Brochure_GROT2025.pdf
└── README.md
```

---

## 🌟 Features

* ✅ Live simulated KPI updates
* 🏢 Multi-branch dashboard filters
* 📉 Visual insights: sales, CSAT, inventory, staff
* 📊 Clean, exportable dashboards (PDF/Excel)
* 🧩 Scalable structure for API & POS integration

---

## 💻 Full Dashboard Code

Below is the complete code used to build and launch the NBC Franchise Dashboard using Dash and Plotly. Each component is annotated for clarity.

```python
# app.py

# Import libraries
import pandas as pd
import random
import dash
from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output

# -----------------------------
# 1. DATA SIMULATION FUNCTION
# -----------------------------
# Generate a realistic dataset with 500 records across 10 global branches

def generate_simulated_kpi_data(num_rows=500):
    branches = ['Mumbai', 'Delhi', 'Dubai', 'London', 'Paris', 'Chennai', 'Bangalore', 'New York', 'Singapore', 'Riyadh']
    data = {
        'Branch': [],
        'BaristaEfficiency (%)': [],
        'CustomerSatisfaction (1–5)': [],
        'DailySales (INR)': [],
        'InventoryLevel (%)': [],
        'OrdersPerHour': []
    }
    for _ in range(num_rows):
        b = random.choice(branches)
        data['Branch'].append(b)
        data['BaristaEfficiency (%)'].append(random.randint(75, 95))
        data['CustomerSatisfaction (1–5)'].append(round(random.uniform(4.0, 4.9), 1))
        data['DailySales (INR)'].append(random.randint(9000, 20000))
        data['InventoryLevel (%)'].append(random.randint(40, 100))
        data['OrdersPerHour'].append(random.randint(40, 75))
    return pd.DataFrame(data)

# -------------------
# 2. INITIALIZE APP
# -------------------
app = dash.Dash(__name__)
app.title = "NBC Franchise Dashboard"

# Load data into DataFrame
df = generate_simulated_kpi_data()

# -----------------------------
# 3. DASHBOARD UI LAYOUT
# -----------------------------
app.layout = html.Div([
    html.H1("☕ NBC Franchise Intelligence Dashboard", style={'textAlign': 'center'}),

    # Dropdown to filter by branch
    dcc.Dropdown(
        id='branch-selector',
        options=[{'label': b, 'value': b} for b in sorted(df['Branch'].unique())],
        value='Mumbai',
        clearable=False,
        style={'width': '40%', 'margin': 'auto'}
    ),

    # Graphs
    dcc.Graph(id='sales-bar'),
    dcc.Graph(id='efficiency-line'),
    dcc.Graph(id='csat-scatter'),
    dcc.Graph(id='inventory-funnel')
])

# -----------------------------
# 4. CALLBACKS FOR INTERACTIVITY
# -----------------------------
@app.callback(
    [Output('sales-bar', 'figure'),
     Output('efficiency-line', 'figure'),
     Output('csat-scatter', 'figure'),
     Output('inventory-funnel', 'figure')],
    [Input('branch-selector', 'value')]
)
def update_graphs(branch):
    f = df[df['Branch'] == branch]  # Filter data for selected branch

    # Sales: Daily revenue
    sales_fig = px.bar(f, y="DailySales (INR)", title=f"Sales - {branch}")

    # Efficiency: Line chart of barista performance
    efficiency_fig = px.line(f, y="BaristaEfficiency (%)", title=f"Efficiency - {branch}")

    # CSAT: Customer satisfaction correlated with sales
    csat_fig = px.scatter(f, x="DailySales (INR)", y="CustomerSatisfaction (1–5)", title=f"CSAT vs Sales")

    # Inventory: Visualize depletion trends
    inventory_fig = px.funnel(f, x="InventoryLevel (%)", y=f.index, title=f"Inventory - {branch}")

    return sales_fig, efficiency_fig, csat_fig, inventory_fig

# -----------------------------
# 5. LAUNCH SERVER
# -----------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
```

```python
# app.py
import pandas as pd
import random
import dash
from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output

# Data simulation
def generate_simulated_kpi_data(num_rows=500):
    branches = ['Mumbai', 'Delhi', 'Dubai', 'London', 'Paris', 'Chennai', 'Bangalore', 'New York', 'Singapore', 'Riyadh']
    data = {
        'Branch': [], 'BaristaEfficiency (%)': [], 'CustomerSatisfaction (1–5)': [],
        'DailySales (INR)': [], 'InventoryLevel (%)': [], 'OrdersPerHour': []
    }
    for _ in range(num_rows):
        b = random.choice(branches)
        data['Branch'].append(b)
        data['BaristaEfficiency (%)'].append(random.randint(75, 95))
        data['CustomerSatisfaction (1–5)'].append(round(random.uniform(4.0, 4.9), 1))
        data['DailySales (INR)'].append(random.randint(9000, 20000))
        data['InventoryLevel (%)'].append(random.randint(40, 100))
        data['OrdersPerHour'].append(random.randint(40, 75))
    return pd.DataFrame(data)

# Dash App
app = dash.Dash(__name__)
df = generate_simulated_kpi_data()

app.layout = html.Div([
    html.H1("☕ NBC Franchise Intelligence Dashboard", style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='branch-selector',
        options=[{'label': b, 'value': b} for b in sorted(df['Branch'].unique())],
        value='Mumbai', clearable=False, style={'width': '40%', 'margin': 'auto'}),
    dcc.Graph(id='sales-bar'), dcc.Graph(id='efficiency-line'),
    dcc.Graph(id='csat-scatter'), dcc.Graph(id='inventory-funnel')
])

@app.callback(
    [Output('sales-bar', 'figure'), Output('efficiency-line', 'figure'),
     Output('csat-scatter', 'figure'), Output('inventory-funnel', 'figure')],
    [Input('branch-selector', 'value')])
def update_graphs(branch):
    f = df[df['Branch'] == branch]
    return (
        px.bar(f, y="DailySales (INR)", title=f"Sales - {branch}"),
        px.line(f, y="BaristaEfficiency (%)", title=f"Efficiency - {branch}"),
        px.scatter(f, x="DailySales (INR)", y="CustomerSatisfaction (1–5)", title=f"CSAT vs Sales"),
        px.funnel(f, x="InventoryLevel (%)", y=f.index, title=f"Inventory - {branch}")
    )

if __name__ == '__main__':
    app.run_server(debug=True)
```

---

## 🧾 Sample Data Output

The dashboard operates on a dynamically simulated dataset of 500+ entries across 10 global cities. Each entry represents a branch transaction day, including key performance indicators like efficiency, satisfaction, sales, inventory, and order rate. The simulation ensures a realistic distribution by incorporating random variances and realistic operational thresholds observed in actual franchise scenarios.

Sample (first 5 of 500+ rows):

| Branch   | BaristaEfficiency (%) | CustomerSatisfaction (1–5) | DailySales (INR) | InventoryLevel (%) | OrdersPerHour |
| -------- | --------------------- | -------------------------- | ---------------- | ------------------ | ------------- |
| Mumbai   | 92                    | 4.8                        | 15000            | 85                 | 60            |
| London   | 88                    | 4.5                        | 12400            | 65                 | 55            |
| Paris    | 91                    | 4.6                        | 13400            | 70                 | 57            |
| Delhi    | 85                    | 4.4                        | 14500            | 60                 | 52            |
| New York | 90                    | 4.7                        | 17200            | 77                 | 63            |

For the full dataset, see [`data/NBC_KPI_Data.csv`](data/NBC_KPI_Data.csv).

| Branch | BaristaEfficiency (%) | CSAT | DailySales | Inventory | Orders/hr |
| ------ | --------------------- | ---- | ---------- | --------- | --------- |
| Mumbai | 92                    | 4.8  | 15000      | 85        | 60        |
| London | 88                    | 4.5  | 12400      | 65        | 55        |
| Paris  | 91                    | 4.6  | 13400      | 70        | 57        |

---

## 🖼️ Screenshots

> Add screenshots in `/docs/screenshots/` and display them here with markdown:

```md
![Dashboard UI](docs/screenshots/dashboard_view.png)
```

---

## 🚀 Deployment

### 🔧 Run Locally

To run the dashboard on your local machine:

```bash
pip install dash pandas plotly
python app.py
```

### ☁️ Deploy to Heroku

1. Install Heroku CLI and login: `heroku login`
2. Create `Procfile`:

```
web: python app.py
```

3. Commit to GitHub and deploy via Heroku dashboard or CLI.

### ☁️ Deploy to AWS EC2 (Ubuntu Example)

1. Launch EC2 instance
2. SSH into the instance
3. Install Python and required packages
4. Clone the GitHub repo and run `python app.py`
5. Configure security groups to allow traffic on port 8050

### 🌐 Deploy with Streamlit Cloud *(optional rewrite)*

If converting to Streamlit format:

1. Replace Dash app with Streamlit UI
2. Upload to GitHub and deploy via [streamlit.io](https://streamlit.io/)

### 📦 Docker Setup (Optional)

```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install dash pandas plotly
CMD ["python", "app.py"]
```

Build and run:

```bash
docker build -t nbc-dashboard .
docker run -p 8050:8050 nbc-dashboard
```

---

## 📈 Business Value

* 📊 Sales uplift tracking by city
* 📦 Inventory waste reduction (alerts)
* 😊 CSAT improvements by staff/team
* 🧑‍🤝‍🧑 Workforce scheduling optimization
* 🏆 Campaign insights prepared for GrafanCon 2025 GROT Award

---

## 👨‍💻 Author & Contact

**Pranjal Gurjar**
MCA Final Year Student
📧 [gurjarpranjal.work@gmail.com](mailto:gurjarpranjal.work@gmail.com)
🔗 [LinkedIn](https://linkedin.com/in/pranjalgurjar)


---

## 📄 License

This project is intended for educational and portfolio purposes. Contact for commercial use.
