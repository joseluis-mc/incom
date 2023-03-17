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
        dbc.NavbarSimple(
            brand="INCOM",
            brand_href="#",
            color="dark",
            dark=True,
        ),

        html.Br(),

        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                dbc.Card(
                                    dbc.CardBody("This is some text within a card body")
                                ),
                                className="bg-dark"
                            ),
                            width=6,
                            class_name="bg-primary"
                        ),
                        dbc.Col(
                            html.Div(
                                dbc.Card(
                                    dbc.CardBody("This is some text within a card body")
                                )
                            ),
                            width=6,
                            class_name="bg-secondary"
                        )
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                dbc.Card(
                                    dbc.CardBody("This is some text within a card body")
                                )
                            ),
                            width=6,
                            class_name="bg-success"
                        ),
                        dbc.Col(
                            html.Div(
                                dbc.Card(
                                    dbc.CardBody("This is some text within a card body")
                                )
                            ),
                            width=6,
                            class_name="bg-danger"
                        )
                    ]
                )
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)