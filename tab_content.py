import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash import html
from make_datasets import fig_indicator_1
from make_datasets import fig_indicator_2
from make_datasets import fig_indicator_3
from make_datasets import fig_indicator_4
from make_datasets import fig_indicator_5
from make_datasets import fig_indicator_6
from make_datasets import fig_search_engines
from make_datasets import fig_social_networks
from make_datasets import fig_paid_sources

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
                                        ['Direct Sessions']
                                    ),
                                    dbc.CardBody([
                                        dcc.Graph(figure=fig_indicator_1,
                                                  style={
                                                    'width': '100%',
                                                    'height': '150px',
                                                  })
                                    ])
                                ])
                            ),
                            width=4
                        ),
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Paid Sessions']),
                                    dbc.CardBody([
                                        dcc.Graph(figure=fig_indicator_3,
                                                  style={
                                                    'width': '100%',
                                                    'height': '150px'
                                                  })
                                    ])
                                ])
                            ),
                            width=4
                        ),
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Organic Sessions']),
                                    dbc.CardBody([
                                        dcc.Graph(figure=fig_indicator_5,
                                                  style={
                                                    'width': '100%',
                                                    'height': '150px'
                                                  })
                                    ])
                                ])
                            ),
                            width=4
                        ),
                    ]
                ),
                
                html.Br(),
                
                # Segunda fila de indicadores
                dbc.Row(
                    [

                        # Tres columnas
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Direct Transactions']),
                                    dbc.CardBody([
                                        dcc.Graph(figure=fig_indicator_2,
                                                  style={
                                                    'width': '100%',
                                                    'height': '150px'
                                                  })
                                    ])
                                ])
                            ),
                            width=4
                        ),
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Paid Transactions']),
                                    dbc.CardBody([
                                        dcc.Graph(figure=fig_indicator_4,
                                                  style={
                                                    'width': '100%',
                                                    'height': '150px'
                                                  })
                                    ])
                                ])
                            ),
                            width=4
                        ),
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Organic Transactions']),
                                    dbc.CardBody([
                                        dcc.Graph(figure=fig_indicator_6,
                                                  style={
                                                    'width': '100%',
                                                    'height': '150px'
                                                  })
                                    ])
                                ])
                            ),
                            width=4
                        ),
                    ]
                ),

                html.Br(),

                # SERIES DE TIEMPO
                # Sigue una tarjeta donde seleccionas una serie de tiempo
                # para visualizarla

                # Una fila y una columna
                dbc.Row(
                    [
                        # Título de la sección
                        html.Div(
                            children=[html.H3(["Visualizations"], style={'color': '#EF7000', 'font-style': 'italic'})]
                        ),

                        dbc.Col(
                            
                            # Tarjeta donde viven las series de tiempo
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Sessions-Transactions Time Series']),
                                    dbc.CardBody([
                                        
                                        # Dropdown para seleccionar la serie
                                        # a visualizar
                                        html.Div([
                                            
                                            # Etiqueta
                                            dbc.Label("Session Type",
                                                      html_for="dropdown"),
                                            
                                            # Dropwdown
                                            dcc.Dropdown(
                                                id="my_dropdown",
                                                options=[
                                                    {"label": "Direct",
                                                     "value": 'fig_time_direct'},
                                                    {"label": "Organic",
                                                     "value": 'fig_time_organic'},
                                                    {"label": "Paid",
                                                     "value": 'fig_time_paid'},
                                                ],
                                                value='fig_time_direct',
                                                clearable=False,
                                                searchable=False,
                                            ),
                                        ],
                                        style={
                                            'width': '25%'
                                        }),
                                        html.Br(),
                                        
                                        # Gráfica con la serie de tiempo
                                        dcc.Graph(id='series_de_tiempo',
                                                  figure={},
                                                  style={
                                                    'width': '100%',
                                                    'height': '500px'
                                                  })
                                    ])
                                ])
                            )
                        )
                    ]
                ),

                html.Br(),

                # GRÁFICAS DE BARRAS
                # Sigue una fila y dos columnas con gráficas de barras

                dbc.Row(
                    [
                        # Primera gráfica de barras
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Organic Sessions by Search Engine']),
                                    dbc.CardBody([
                                        dcc.Graph(figure=fig_search_engines,
                                                  style={
                                                    'width': '100%',
                                                    'height': '450px'
                                                  })
                                    ])
                                ])
                            ), width=6
                        ),
                        
                        # Segunda gráfica de barras
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Paid Sessions by Social Network']),
                                    dbc.CardBody([
                                        dcc.Graph(figure=fig_social_networks,
                                                  style={
                                                    'width': '100%',
                                                    'height': '450px'
                                                  })
                                    ])
                                ])
                            ), width=6
                        )
                    ]
                ),

                html.Br(),

                # TREEMAP
                # Terminamos con un treemap
                
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                dbc.Card([
                                    dbc.CardHeader(['Paid Sources']),
                                    dbc.CardBody([
                                        dcc.Graph(figure=fig_paid_sources,
                                                  style={
                                                    'width': '100%',
                                                    'height': '500px'
                                                  })
                                    ])
                                ])
                            ), width=12
                        ),
                    ]
                ),
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