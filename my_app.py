from dash import Dash, dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash import Input, Output, html
from tab_content import sales_tab, engagement_tab, tab_3
from tab_content import fig_time_paid, fig_time_direct, fig_time_organic

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = html.Div(
    [
        # Barra de navegación
        dbc.NavbarSimple(
            brand="ETS-INCOM Dashboard",
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
                            dbc.Tab(label = 'Engagement', tab_id = 'tab-2', disabled=True),
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

#@app.callback(
#    Output('series_de_tiempo', 'figure'), [Input('dropdown', 'value')]
#)
#def time_series(value):
#    if value == 'fig_time_direct':
#        return fig_time_direct
#    if value == 'fig_time_organic':
#        return fig_time_direct
#    if value == 'fig_time_paid':
#        return fig_time_direct

if __name__ == '__main__':
    app.run_server(debug=True)