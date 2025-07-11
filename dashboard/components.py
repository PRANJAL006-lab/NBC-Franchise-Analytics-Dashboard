📜 dashboard/components.py

This file defines the modular layout for the dashboard UI. It constructs dropdown menus for user selections and sets up all visual components like bar graphs, pie charts, and data tables.
It's designed for reusability and easy scalability to include additional filters or charts in the future.
                                                                                                                                                             import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd


def layout(df):
    cities = sorted(df['City'].unique())
    products = sorted(df['Product'].unique())
    loyalty_segments = sorted(df['LoyaltySegment'].unique())

    return html.Div([
        html.H1("Nothing Before Coffee - Franchise KPI Dashboard", style={'textAlign': 'center'}),

        html.Div([
            html.Div([
                html.Label("Select City:"),
                dcc.Dropdown(
                    id='city-dropdown',
                    options=[{'label': c, 'value': c} for c in cities],
                    value=cities[0], clearable=False
                )
            ], style={'width': '30%', 'display': 'inline-block'}),

            html.Div([
                html.Label("Select Product:"),
                dcc.Dropdown(
                    id='product-dropdown',
                    options=[{'label': p, 'value': p} for p in products],
                    value=products[0], clearable=False
                )
            ], style={'width': '30%', 'display': 'inline-block'}),

            html.Div([
                html.Label("Select Loyalty Segment:"),
                dcc.Dropdown(
                    id='loyalty-dropdown',
                    options=[{'label': l, 'value': l} for l in loyalty_segments],
                    value=loyalty_segments[0], clearable=False
                )
            ], style={'width': '30%', 'display': 'inline-block'})
        ], style={'padding': '20px'}),

        html.Div([
            dcc.Graph(id='sales-line'),
            dcc.Graph(id='inventory-bar'),
            dcc.Graph(id='footfall-trend'),
            dcc.Graph(id='service-efficiency'),
            dcc.Graph(id='return-rate'),
            dcc.Graph(id='loyalty-pie')
        ]),

        html.H3("🔍 Branch Performance Table"),
        dash_table.DataTable(
            id='branch-table',
            columns=[{'name': i, 'id': i} for i in df.columns],
            page_size=10, style_table={'overflowX': 'scroll'}
        )
    ])
