This is the main entry point for the NBC Dashboard built using Dash and Plotly. It initializes the app, loads the dataset, sets up layout and callbacks, and controls the interaction between inputs and chart outputs. This file handles dynamic updates for KPIs such as sales, inventory, footfall, and loyalty metrics across selected cities and products.
'''
  import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from components import layout

# Load dataset
df = pd.read_csv('data/NBC_KPI_Data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# App initialization
app = dash.Dash(__name__, title='NBC Franchise Dashboard')
server = app.server

# Layout
app.layout = layout(df)

# Callbacks
@app.callback(
    [
        Output('sales-line', 'figure'),
        Output('inventory-bar', 'figure'),
        Output('footfall-trend', 'figure'),
        Output('service-efficiency', 'figure'),
        Output('return-rate', 'figure'),
        Output('loyalty-pie', 'figure'),
        Output('branch-table', 'data')
    ],
    [
        Input('city-dropdown', 'value'),
        Input('product-dropdown', 'value'),
        Input('loyalty-dropdown', 'value')
    ]
)
def update_dashboard(city, product, loyalty):
    filtered_df = df[(df['City'] == city) &
                     (df['Product'] == product) &
                     (df['LoyaltySegment'] == loyalty)]

    sales_fig = px.line(
        filtered_df.groupby('Date')['Sales'].sum().reset_index(),
        x='Date', y='Sales', title=f"📈 Sales Trend in {city} for {product}"
    )

    inventory_fig = px.bar(
        filtered_df.groupby('Branch')['InventoryLevel (%)'].mean().reset_index(),
        x='Branch', y='InventoryLevel (%)', color='InventoryLevel (%)',
        color_continuous_scale='viridis', title=f"📦 Inventory in {city}"
    )

    footfall_fig = px.area(
        filtered_df.groupby('Date')['CustomerFootfall'].sum().reset_index(),
        x='Date', y='CustomerFootfall', title="🚶 Customer Footfall Over Time"
    )

    service_fig = px.box(
        filtered_df, x='Branch', y='AvgServiceTime',
        title="⏱️ Service Time per Branch"
    )

    return_fig = px.histogram(
        filtered_df, x='ReturnRate', nbins=20,
        title="🔁 Return Rate Distribution"
    )

    loyalty_fig = px.pie(
        filtered_df.groupby('LoyaltySegment').size().reset_index(name='Count'),
        names='LoyaltySegment', values='Count', title="🎯 Loyalty Segments"
    )

    table_data = filtered_df.to_dict('records')
    return sales_fig, inventory_fig, footfall_fig, service_fig, return_fig, loyalty_fig, table_data

if __name__ == '__main__':
    app.run_server(debug=True)
  '''
