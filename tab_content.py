from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
from make_figures import nuevo_indicador1
from make_figures import nuevo_indicador2
from make_figures import nuevo_indicador3
from make_figures import nuevo_indicador4
from make_figures import nuevo_indicador5
from make_figures import nuevo_indicador6
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
from make_figures import search_term1
from make_figures import search_term2
from make_figures import search_term3
from make_figures import search_term4
from make_figures import search_term5
from make_figures import fig_map
from make_figures import fig_bars3
from make_figures import fig_bars4
from make_figures import fig_tabla_pestana2

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
                                        ['eReg Reached']
                                    ),
                                    dbc.CardBody([
                                        dcc.Graph(figure=nuevo_indicador1,
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
                                    dbc.CardHeader(['Account Creation Intent']),
                                    dbc.CardBody([
                                        dcc.Graph(figure=nuevo_indicador2,
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
                                    dbc.CardHeader(['Account Creation Success']),
                                    dbc.CardBody([
                                        dcc.Graph(figure=nuevo_indicador3,
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
                                    dbc.CardHeader(['Register For a Test Intent']),
                                    dbc.CardBody([
                                        dcc.Graph(figure=nuevo_indicador4,
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
                                    dbc.CardHeader(['Order Confirmation']),
                                    dbc.CardBody([
                                        dcc.Graph(figure=nuevo_indicador5,
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
                                    dbc.CardHeader(['ROI']),
                                    dbc.CardBody([
                                        dcc.Graph(figure=nuevo_indicador6,
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
                                                'height': '400px'
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
                                    dbc.CardHeader(['Order Confirmations (Organic)']),
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
                                    dbc.CardHeader(['Organic Conversion Rate']),
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
                                    dbc.CardHeader(['Order Confirmations (Paid)']),
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
                                    dbc.CardHeader(['Paid Conversion Rate']),
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
                                            figure = search_term1,
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
                                        dcc.Graph(figure=fig_bars3,
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
                                    dbc.CardHeader(['Sessions by Region (Map)']),
                                    dbc.CardBody([
                                        dcc.Graph(figure=fig_map,
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
                                                dcc.Graph(figure=fig_bars4,
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
                                            figure=fig_tabla_pestana2,
                                            style = {
                                                'width': '100%',
                                                'height': '550px'
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