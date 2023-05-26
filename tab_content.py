from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
from make_figures import fig_indicator_1
from make_figures import fig_indicator_2
from make_figures import fig_indicator_3
from make_figures import fig_indicator_4
from make_figures import fig_indicator_5
from make_figures import fig_indicator_6
from make_figures import fig_treemap
from make_figures import fig_timeseries
from make_figures import fig_bars1
from make_figures import fig_bars2
from make_figures import fig_table

sales_tab = html.Div(
            [
                # INDICADORES
                # Empezamos con dos filas y tres columnas de indicadores
                
                # Primera fila de indicadores
                dbc.Row(
                    [
                        # Título de la sección
                        html.Div(
                            children=[html.H3(["Key Metrics"], style={'color': '#EF7000', 'font-style': 'italic'})]
                        ),

                        # Tres columnas
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(
                                        ['Organic Sessions']
                                    ),
                                    dbc.CardBody([
                                        dcc.Graph(figure=fig_indicator_1,
                                                  style={
                                                    'width': '100%',
                                                    'height': '100px',
                                                  })
                                    ])
                                ]),
                                style={'margin-bottom': '30px'}
                            ),
                            sm=12, md=4, lg=4, xl=4, xxl=4
                        ),
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Organic Transactions']),
                                    dbc.CardBody([
                                        dcc.Graph(figure=fig_indicator_2,
                                                  style={
                                                    'width': '100%',
                                                    'height': '100px'
                                                  })
                                    ])
                                ]),
                                style={'margin-bottom': '30px'}
                            ),
                            sm=12, md=4, lg=4, xl=4, xxl=4
                        ),
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Conversion Rate (%)']),
                                    dbc.CardBody([
                                        dcc.Graph(figure=fig_indicator_3,
                                                  style={
                                                    'width': '100%',
                                                    'height': '100px'
                                                  })
                                    ])
                                ]),
                                style={'margin-bottom': '30px'}
                            ),
                            sm=12, md=4, lg=4, xl=4, xxl=4
                        ),
                    ]
                ),
                
                # Segunda fila de indicadores
                dbc.Row(
                    [

                        # Tres columnas
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Paid Sessions']),
                                    dbc.CardBody([
                                        dcc.Graph(figure=fig_indicator_4,
                                                  style={
                                                    'width': '100%',
                                                    'height': '100px'
                                                  })
                                    ])
                                ]),
                                style={'margin-bottom': '30px'}
                            ),
                            sm=12, md=4, lg=4, xl=4, xxl=4
                        ),
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Paid Transactions']),
                                    dbc.CardBody([
                                        dcc.Graph(figure=fig_indicator_5,
                                                  style={
                                                    'width': '100%',
                                                    'height': '100px'
                                                  })
                                    ])
                                ]),
                                style={'margin-bottom': '30px'}
                            ),
                            sm=12, md=4, lg=4, xl=4, xxl=4
                        ),
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Paid Rate (%)']),
                                    dbc.CardBody([
                                        dcc.Graph(figure=fig_indicator_6,
                                                  style={
                                                    'width': '100%',
                                                    'height': '100px'
                                                  })
                                    ])
                                ]),
                                style={'margin-bottom': '30px'}
                            ),
                            sm=12, md=4, lg=4, xl=4, xxl=4
                        ),
                    ]
                ),

                # TREEMAP
                # Empezamos con un treemap
                
                dbc.Row(
                    [
                        # Título de la sección
                        html.Div(
                            children=[html.H3(["Visualizations"], style={'color': '#EF7000', 'font-style': 'italic'})]
                        ),

                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Campaigns by Channel Grouping']),
                                    dbc.CardBody([
                                        dcc.Graph(figure=fig_treemap,
                                                  style={
                                                    'width': '100%',
                                                    'height': '500px'
                                                  })
                                    ])
                                ])
                            ), width=12
                        ),
                    ], style={'margin-bottom': '30px'}
                ),

                # SERIES DE TIEMPO
                # Sigue una tarjeta donde seleccionas una serie de tiempo
                # para visualizarla

                # Una fila y una columna
                dbc.Row(
                    [

                        dbc.Col(
                            
                            # Tarjeta donde viven las series de tiempo
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Weekly Sessions: Organic vs INCOM']),
                                    dbc.CardBody([
                                        dbc.Row([
                                            dbc.Col([
                                                # Gráfica con la serie de tiempo
                                                dcc.Graph(figure=fig_timeseries,
                                                          style={
                                                            'width': '100%',
                                                            'height': '500px'
                                                        })
                                            ])
                                        ]) 
                                    ])
                                ])
                            )
                        )
                    ],
                    style={'margin-bottom': '30px'}
                ),

                # GRÁFICAS DE BARRAS
                # Sigue una fila y dos columnas con gráficas de barras

                dbc.Row(
                    [
                        # Primera gráfica de barras
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Sessions by Campaign Source']),
                                    dbc.CardBody([
                                        dcc.Graph(figure=fig_bars1,
                                                  style={
                                                    'width': '100%',
                                                    'height': '450px'
                                                  })
                                    ])
                                ]),
                                style={'margin-bottom': '30px'}
                            ), sm=1, md=6, lg=6, xl=6, xxl=6
                        ),
                        
                        # Segunda gráfica de barras
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Sessions by Campaign Type']),
                                    dbc.CardBody([
                                        dcc.Graph(figure=fig_bars2,
                                                  style={
                                                    'width': '100%',
                                                    'height': '450px'
                                                  })
                                    ])
                                ]),
                                style={'margin-bottom': '30px'}
                            ), sm=1, md=6, lg=6, xl=6, xxl=6
                        )
                    ]
                ),

                # TABLA
                # Cerramos con una tabla del rendimiento de cada campaña
                dbc.Row(
                    [
                        # Título de la sección
                        html.Div(
                            children=[html.H3(["Campaign Performance Details"], style={'color': '#EF7000', 'font-style': 'italic'})]
                        ),

                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        dcc.Graph(
                                            figure=fig_table,
                                            style = {
                                                'width': '100%',
                                                'height': '300px'
                                            }
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ],
            className="px-4 pt-0"
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