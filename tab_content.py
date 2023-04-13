from dash import Dash, dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash import Input, Output, html
from make_datasets import fig_indicator_1, fig_indicator_2, fig_indicator_3, fig_indicator_4, fig_indicator_5, fig_indicator_6, fig_time_direct, fig_time_organic, fig_time_paid, fig_search_engines, fig_social_networks, fig_paid_sources

sales_tab = html.Div(
            [
                # Indicadores
                dbc.Row(
                    [
                        html.Div(
                            children=[html.H3(["Indicadores"])]
                        ),
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Sesiones - Directas']),
                                    dbc.CardBody([
                                        dcc.Graph(figure = fig_indicator_1, style={'width': '100%', 'height': '150px'})
                                    ])
                                ])
                            ),
                            width=4
                        ),
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Transacciones - Directas']),
                                    dbc.CardBody([
                                        dcc.Graph(figure = fig_indicator_2, style={'width': '100%', 'height': '150px'})
                                    ])
                                ])
                            ),
                            width=4
                        ),
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Sesiones - Adquiridas']),
                                    dbc.CardBody([
                                        dcc.Graph(figure = fig_indicator_3, style={'width': '100%', 'height': '150px'})
                                    ])
                                ])
                            ),
                            width=4
                        ),
                    ]
                ),
                
                html.Br(),
                
                # Más indicadores
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Transacciones - Adquiridas']),
                                    dbc.CardBody([
                                        dcc.Graph(figure = fig_indicator_4, style={'width': '100%', 'height': '150px'})
                                    ])
                                ])
                            ),
                            width=4
                        ),
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Sesiones - Orgánicas']),
                                    dbc.CardBody([
                                        dcc.Graph(figure = fig_indicator_5, style={'width': '100%', 'height': '150px'})
                                    ])
                                ])
                            ),
                            width=4
                        ),
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Transacciones - Orgánicas']),
                                    dbc.CardBody([
                                        dcc.Graph(figure = fig_indicator_6, style={'width': '100%', 'height': '150px'})
                                    ])
                                ])
                            ),
                            width=4
                        ),
                    ]
                ),

                html.Br(),

                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Series de Tiempo']),
                                    dbc.CardBody([
                                        html.Div([
                                            dbc.Label("Tipo de Sesiones", html_for="dropdown"),
                                            dcc.Dropdown(
                                                id="dropdown",
                                                options=[
                                                    {"label": "Directas", "value": 'fig_time_direct'},
                                                    {"label": "Orgánicas", "value": 'fig_time_organic'},
                                                    {"label": "Pagadas", "value": 'fig_time_paid'},
                                                ],
                                                value = 'fig_time_direct',
                                                clearable = False,
                                                searchable = False,
                                            ),
                                        ],
                                        style = {
                                            'width': '25%'
                                        }),
                                        html.Br(),
                                        dcc.Graph(figure=fig_time_direct, style={'width': '100%', 'height': '500px'})
                                    ])
                                ])
                            )
                        )
                    ]
                ),

                html.Br(),

                # Adicionales
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Sesiones Orgánicas por Buscador']),
                                    dbc.CardBody([
                                        dcc.Graph(figure = fig_search_engines, style={'width': '100%', 'height': '450px'})
                                    ])
                                ])
                            ), width = 6
                        ),
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Sesiones Adquiridas por Red Social']),
                                    dbc.CardBody([
                                        dcc.Graph(figure = fig_social_networks, style={'width': '100%', 'height': '450px'})
                                    ])
                                ])
                            ), width = 6
                        )
                    ]
                ),

                html.Br(),

                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Paid Sources']),
                                    dbc.CardBody([
                                        dcc.Graph(figure = fig_paid_sources, style={'width': '100%', 'height': '500px'})
                                    ])
                                ])
                            ), width = 12
                        ),
                    ]
                ),
            ],
            className="px-4 pt-4"
    )

engagement_tab = html.Div(
            [
                # Indicadores
                dbc.Row(
                    [
                        html.Div(
                            children=[html.H1(["Indicadores 2"])]
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
                        )
                    ]
                )
            ],
            className="px-4 pt-4"
        )

tab_3 = html.Div(
            [
                # Indicadores
                dbc.Row(
                    [
                        html.Div(
                            children=[html.H1(["Indicadores 3"])]
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
                        )
                    ]
                )
            ],
            className="px-4 pt-4"
    )