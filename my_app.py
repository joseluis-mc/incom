from dash import Dash, dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

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

        html.Div(
            [
                # Indicadores
                dbc.Row(
                    [
                        html.Div(
                            children=[html.H1(["Indicadores"])]
                        ),
                        dbc.Col(
                            html.Div(
                                dbc.Card(
                                    dbc.CardBody("This is some text within a card body")
                                )
                            ),
                            width=3
                        ),
                        dbc.Col(
                            html.Div(
                                dbc.Card(
                                    dbc.CardBody("This is some text within a card body")
                                )
                            ),
                            width=3
                        ),
                        dbc.Col(
                            html.Div(
                                dbc.Card(
                                    dbc.CardBody("This is some text within a card body")
                                )
                            ),
                            width=3
                        ),
                        dbc.Col(
                            html.Div(
                                dbc.Card(
                                    dbc.CardBody("This is some text within a card body")
                                )
                            ),
                            width=3
                        )
                    ]
                ),
                html.Br(),
                # Más indicadores
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                dbc.Card(
                                    dbc.CardBody("This is some text within a card body")
                                )
                            ),
                            width=3
                        ),
                        dbc.Col(
                            html.Div(
                                dbc.Card(
                                    dbc.CardBody("This is some text within a card body")
                                )
                            ),
                            width=3
                        ),
                        dbc.Col(
                            html.Div(
                                dbc.Card(
                                    dbc.CardBody("This is some text within a card body")
                                )
                            ),
                            width=3
                        ),
                        dbc.Col(
                            html.Div(
                                dbc.Card(
                                    dbc.CardBody("This is some text within a card body")
                                )
                            ),
                            width=3
                        )
                    ]
                )
            ],
            className="px-4 pt-4"
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)