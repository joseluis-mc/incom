from dash import dcc
import dash_bootstrap_components as dbc
from dash import html

from make_figures import search_term1_365

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
                                        ['Ereg Reached']
                                    ),
                                    dbc.CardBody([
                                        dcc.Graph(figure={},
                                                  id = 'sheets1',
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
                                    dbc.CardHeader(['Acc. Creation Intent']),
                                    dbc.CardBody([
                                        dcc.Graph(figure={},
                                                  id = 'sheets2',
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
                                    dbc.CardHeader(['Acc. Creation Success']),
                                    dbc.CardBody([
                                        dcc.Graph(figure={},
                                                  id = 'sheets3',
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
                                    dbc.CardHeader(['Register for a Test Intent']),
                                    dbc.CardBody([
                                        dcc.Graph(figure={},
                                                  id = 'sheets4',
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
                                    dbc.CardHeader(['Order Confirmations (Paid)']),
                                    dbc.CardBody([
                                        dcc.Graph(figure={},
                                                  id = 'sheets5',
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
                                    dbc.CardHeader(['Average ROI'], id = 'tooltip-target'),
                                    dbc.Tooltip(
                                        '=Total Spend/transactionRevenue',
                                        target = 'tooltip-target',
                                        placement = 'auto-start'
                                    ),
                                    dbc.CardBody([
                                        dcc.Graph(figure={},
                                                  id = 'sheets6',
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
                            children=[html.H3(["Campaign Performance Details"], style={'color': '#EF7000', 'font-style': 'italic'})]
                        ),

                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Sessions by Campaign - Channel Grouping']),
                                    dbc.CardBody([
                                        dcc.Graph(figure={},
                                                  id = 'treemap',
                                                  style={
                                                    'width': '100%',
                                                    'height': '500px'
                                                  })
                                    ])
                                ])
                            ), width=12
                        ),
                    ], style={'margin-bottom': '10px'}
                ),

                # TABLA
                # Cerramos con una tabla del rendimiento de cada campaña
                dbc.Row(
                    [   
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        dcc.Graph(
                                            figure={},
                                            id = "table",
                                            style = {
                                                'width': '100%',
                                                'height': '225px'
                                            }
                                        )
                                    ]
                                )
                            ]
                        )
                    ], style={'margin-bottom': '40px'}
                ),

                # SERIES DE TIEMPO
                # Sigue una tarjeta donde seleccionas una serie de tiempo
                # para visualizarla

                # Una fila y una columna
                dbc.Row(
                    [
                        # Título de la sección
                        # html.Div(
                        #     children=[html.H3(["Sessions and Campaigns"], style={'color': '#EF7000', 'font-style': 'italic'})]
                        # ),

                        dbc.Col(
                            
                            # Tarjeta donde viven las series de tiempo
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Weekly Sessions: Organic vs generated by INCOM']),
                                    dbc.CardBody([
                                        dbc.Row([
                                            dbc.Col([
                                                # Gráfica con la serie de tiempo
                                                dcc.Graph(figure={},
                                                          id = 'timeseries',
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
                                        dcc.Graph(figure={},
                                                  id = 'bars1',
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
                                    dbc.CardHeader(['Sessions by Campaign']),
                                    dbc.CardBody([
                                        dcc.Graph(figure={},
                                                  id = 'bars2',
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

            ],
            className="px-4 pt-0"
    )

engagement_tab = html.Div(
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
                                        dcc.Graph(figure={},
                                                  id = 'indicator_1',
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
                                    dbc.CardHeader(['Organic order confirmations']),
                                    dbc.CardBody([
                                        dcc.Graph(figure={},
                                                  id = 'indicator_2',
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
                                    dbc.CardHeader(['Organic Conversion Rate']),
                                    dbc.CardBody([
                                        dcc.Graph(figure={},
                                                  id = 'indicator_3',
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
                                        dcc.Graph(figure={},
                                                  id = 'indicator_4',
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
                                    dbc.CardHeader(['Paid order confirmations']),
                                    dbc.CardBody([
                                        dcc.Graph(figure={},
                                                  id = 'indicator_5',
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
                                    dbc.CardHeader(['Paid Conversion Rate']),
                                    dbc.CardBody([
                                        dcc.Graph(figure={},
                                                  id = 'indicator_6',
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

                # Serie de Tiempo
                # Empezamos con una serie de tiempo
                dbc.Row(
                    [
                        # Título de la sección
                        html.Div(
                            children=[html.H3(["Visualizations"], style={'color': '#EF7000', 'font-style': 'italic'})]
                        ),

                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Google Trend Search Hits']),
                                    dbc.CardBody([
                                        # Dropdown para seleccionar la serie a visualizar
                                        html.Div(
                                            [
                                                # Etiqueta
                                                dbc.Label('Search Term'),

                                                # Dropdown
                                                dcc.Dropdown(
                                                    id = 'my_dropdown',
                                                    options=[
                                                        {'label': 'TOEFL', 'value': 'TOEFL'},
                                                        {'label': 'TOEFL iBT México', 'value': 'TOEFL IBT MEXICO'},
                                                        {'label': 'México examen inglés', 'value': 'MEXICO EXAMEN INGLES'},
                                                        {'label': 'Certificación de inglés', 'value': 'CERTIFICACION DE INGLES'},
                                                        {'label': 'TOEFL online', 'value': 'TOEFL ONLINE'}
                                                    ],
                                                    value='TOEFL',
                                                    searchable=False,
                                                    clearable=False
                                                ),
                                            ], style={'width': '25%'}
                                        ),

                                        html.Br(),

                                        dcc.Graph(
                                            id = 'series_de_tiempo',
                                            figure = search_term1_365,
                                            style={
                                                'width': '100%',
                                                'height': '500px'
                                            }
                                        )
                                    ])
                                ])
                            ), width=12
                        ),
                    ], style={'margin-bottom': '30px'}
                ),

                # GRÁFICAS DE BARRAS
                # Sigue una fila y dos columnas con gráficas de barras
                dbc.Row(
                    [
                        # Primera gráfica de barras
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Sessions by Region (Top 5)']),
                                    dbc.CardBody([
                                        dcc.Graph(figure={},
                                                  id = 'bars_3',
                                                  style={
                                                    'width': '100%',
                                                    'height': '450px'
                                                  })
                                    ])
                                ]),
                                style={'margin-bottom': '30px'}
                            ), sm=1, md=6, lg=6, xl=6, xxl=6
                        ),
                        
                        # Mapa
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Sessions by Region (Map)']),
                                    dbc.CardBody([
                                        dcc.Graph(figure={},
                                                  id = 'map',
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
                                    dbc.CardHeader(['Sessions by Hour of Day']),
                                    dbc.CardBody([
                                        dbc.Row([
                                            dbc.Col([
                                                # Gráfica con la serie de tiempo
                                                dcc.Graph(figure={},
                                                        id = 'bars_4',
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
                                            figure={},
                                                  id = 'tabla_pestana_2',
                                            style = {
                                                'width': '100%',
                                                'height': '200px'
                                            }
                                        )
                                    ]
                                )
                            ]
                        )
                    ], style={'margin-bottom': '30px'}
                )
            ],
            className="px-4 pt-0"
    )