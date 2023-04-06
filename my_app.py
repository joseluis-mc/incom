from dash import Dash, dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash import Input, Output, html
from tab_content import sales_tab, engagement_tab, tab_3

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = html.Div(
    [
        # Barra de navegación
        dbc.NavbarSimple(
            brand="ETS Dashboard",
            brand_href="#",
            color="dark",
            dark=True,
        ),

        dbc.Card(
            [
                dbc.CardHeader(
                    dbc.Tabs(
                        [
                            dbc.Tab(label = 'Sales', tab_id = 'tab-1'),
                            dbc.Tab(label = 'Engagement', tab_id = 'tab-2'),
                            dbc.Tab(label = 'Tab 3', tab_id = 'tab-3')
                        ],
                        id = 'card-tabs',
                        active_tab = 'tab-1'
                    )
                ),
                dbc.CardBody(id = 'card-content')
            ]
        )  
    ]
)

@app.callback(
    Output("card-content", "children"), [Input("card-tabs", "active_tab")]
)
def tab_content(active_tab):
    if active_tab == 'tab-1':
        return sales_tab
    elif active_tab == 'tab-2':
        return engagement_tab
    elif active_tab == 'tab-3':
        return tab_3

if __name__ == '__main__':
    app.run_server(debug=True)