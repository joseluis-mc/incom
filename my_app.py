# En este archivo vive la aplicación. Primero, importamos librerías.

# Dash para configurar y diseñar la aplicación:
from dash import Dash # Importamos Dash
from dash import Input, Output, html # Módulos adicionales para callbacks
from dash import html # Componentes básicos de HTML para layout
import dash_bootstrap_components as dbc # Componentes de Bootstrap

# Contenido de otros archivos
from tab_content import sales_tab, engagement_tab # Contenido de las pestañas
# Figuras Pestaña 1
from make_figures import nuevo_indicador1_90
from make_figures import nuevo_indicador1_180
from make_figures import nuevo_indicador1_365
from make_figures import nuevo_indicador2_90
from make_figures import nuevo_indicador2_180
from make_figures import nuevo_indicador2_365
from make_figures import nuevo_indicador3_90
from make_figures import nuevo_indicador3_180
from make_figures import nuevo_indicador3_365
from make_figures import nuevo_indicador4_90
from make_figures import nuevo_indicador4_180
from make_figures import nuevo_indicador4_365
from make_figures import nuevo_indicador5_90
from make_figures import nuevo_indicador5_180
from make_figures import nuevo_indicador5_365
from make_figures import nuevo_indicador6_90
from make_figures import nuevo_indicador6_180
from make_figures import nuevo_indicador6_365
from make_figures import fig_treemap
from make_figures import fig_treemap_90
from make_figures import fig_treemap_180
from make_figures import fig_treemap_365
from make_figures import fig_bars1
from make_figures import fig_bars2
from make_figures import fig_bars1_90
from make_figures import fig_bars2_90
from make_figures import fig_bars1_180
from make_figures import fig_bars2_180
from make_figures import fig_bars1_365
from make_figures import fig_bars2_365
from make_figures import fig_table
from make_figures import fig_table_90
from make_figures import fig_table_180
from make_figures import fig_table_365
from make_figures import fig_timeseries
from make_figures import fig_timeseries_90
from make_figures import fig_timeseries_180
from make_figures import fig_timeseries_365

# Figuras Pestaña 2
from make_figures import fig_indicator_1
from make_figures import fig_indicator_2
from make_figures import fig_indicator_3
from make_figures import fig_indicator_4
from make_figures import fig_indicator_5
from make_figures import fig_indicator_6
from make_figures import fig_indicator_1_90
from make_figures import fig_indicator_2_90
from make_figures import fig_indicator_3_90
from make_figures import fig_indicator_4_90
from make_figures import fig_indicator_5_90
from make_figures import fig_indicator_6_90
from make_figures import fig_indicator_1_180
from make_figures import fig_indicator_2_180
from make_figures import fig_indicator_3_180
from make_figures import fig_indicator_4_180
from make_figures import fig_indicator_5_180
from make_figures import fig_indicator_6_180
from make_figures import fig_indicator_1_365
from make_figures import fig_indicator_2_365
from make_figures import fig_indicator_3_365
from make_figures import fig_indicator_4_365
from make_figures import fig_indicator_5_365
from make_figures import fig_indicator_6_365
from make_figures import search_term1_365
from make_figures import search_term2_365
from make_figures import search_term3_365
from make_figures import search_term4_365
from make_figures import search_term5_365
from make_figures import fig_map
from make_figures import fig_map_90
from make_figures import fig_map_180
from make_figures import fig_map_365
from make_figures import fig_bars3
from make_figures import fig_bars4
from make_figures import fig_bars3_90
from make_figures import fig_bars4_90
from make_figures import fig_bars3_180   
from make_figures import fig_bars4_180
from make_figures import fig_bars3_365
from make_figures import fig_bars4_365
from make_figures import fig_tabla_pestana2
from make_figures import fig_tabla_pestana2_90
from make_figures import fig_tabla_pestana2_180
from make_figures import fig_tabla_pestana2_365

#------------------------------------------------------------------------------
# APLICACIÓN

# Inicializamos la aplicación
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP], # Integramos Bootstrap
    meta_tags=[
        {"name": "viewport",
         "content": "width=device-width, initial-scale=1"},
    ],
)

app.title = 'ETS Analytics Dashboard'

app.config.suppress_callback_exceptions=True

# Configuramos el diseño de la aplicación
app.layout=html.Div(
    [
        # Logo
        html.Div(
            [
                html.Img(src = '/assets/ets_toefl_logo.jpeg', style = {'width': '100%'}),
            ],
            style = {
                'width': '20%',
                'margin-top': '20px',
                'margin-left': '20px'
            }
        ),

        dbc.Row(
            dbc.Col(
                [
                    html.Div(
                        [
                            html.H1(
                                [
                                    'Analytics Dashboard'
                                ],
                                style = {
                                    'color': '#037E83',
                                    'font-weight': 'bold',
                                    'textAlign': 'center',
                                    'font-style': 'italic'
                                }
                            )
                        ]
                    ),
                ],
                #sm=3
            ),
            justify='center'
        ),

        dbc.Row(
            dbc.Col(
                [
                    html.Div(
                        html.P('Select a timeframe to view your data:'), style = {'margin-left': '20px'}
                    ),
                    html.Div(
                        [
                            dbc.RadioItems(
                                id="radios",
                                className="btn-group",
                                inputClassName="btn-check",
                                labelClassName="btn btn-outline-primary",
                                labelCheckedClassName="active",
                                options=[
                                    {"label": "Last 90 days", "value": 90},
                                    {"label": "Last 180 days", "value": 180},
                                    {"label": "Last 365 days", "value": 365},
                                ],
                                value=90
                            )
                        ], className="radio-group", style = {'margin-left': '20px'}
                    ),
                ]
            )
        ),
        
        # Tarjeta donde vive el contenido de la aplicación
        dbc.Card(
            [
                # Header con pestañas
                dbc.CardHeader(
                    dbc.Tabs(
                        [
                            # Pestaña de ventas
                            dbc.Tab(label='Sales',
                                    tab_id='tab-1',
                                    #label_style = {'borderColor': 'white'}
                                ),

                            # Pestaña de "engagement"
                            dbc.Tab(label='Engagement',
                                    tab_id='tab-2',
                                    disabled=False,
                                    #label_style = {'borderColor': 'white'}
                                ),
                        ],
                        id='card-tabs',
                        active_tab='tab-1'
                    ),
                    style = {
                        'backgroundColor': 'white'
                    }
                ),
                dbc.CardBody(id='card-content')
            ],
            style = {
                'border': 0
            }
        )  
    ]
)

#------------------------------------------------------------------------------
# CALLBACKS

# Cambio de pestaña
@app.callback(
    Output("card-content", "children"),
    [Input("card-tabs", "active_tab")]
)
def tab_content(active_tab):
    if active_tab=='tab-1':
        return sales_tab
    elif active_tab=='tab-2':
        return engagement_tab

# Selección de figura en serie de tiempo
@app.callback(
    Output('series_de_tiempo', 'figure'),
    [Input('my_dropdown', 'value')]
)
def time_series(value):
    if value=='TOEFL':
        return search_term1_365
    if value=='TOEFL IBT MEXICO':
        return search_term2_365
    if value=='MEXICO EXAMEN INGLES':
        return search_term3_365
    if value=='CERTIFICACION DE INGLES':
        return search_term4_365
    if value=='TOEFL ONLINE':
        return search_term5_365
    
# Actualizar figuras
@app.callback(
    Output("sheets1", "figure"),
    [Input("radios", "value")]
)
def sheets_1(value):
    if value==90:
        return nuevo_indicador1_90
    if value==180:
        return nuevo_indicador1_180
    if value==365:
        return nuevo_indicador1_365
    
@app.callback(
    Output("sheets2", "figure"),
    [Input("radios", "value")]
)
def sheets_2(value):
    if value==90:
        return nuevo_indicador2_90
    if value==180:
        return nuevo_indicador2_180
    if value==365:
        return nuevo_indicador2_365

@app.callback(
    Output("sheets3", "figure"),
    [Input("radios", "value")]
)
def sheets_3(value):
    if value==90:
        return nuevo_indicador3_90
    if value==180:
        return nuevo_indicador3_180
    if value==365:
        return nuevo_indicador3_365

@app.callback(
    Output("sheets4", "figure"),
    [Input("radios", "value")]
)
def sheets_4(value):
    if value==90:
        return nuevo_indicador4_90
    if value==180:
        return nuevo_indicador4_180
    if value==365:
        return nuevo_indicador4_365

@app.callback(
    Output("sheets5", "figure"),
    [Input("radios", "value")]
)
def sheets_5(value):
    if value==90:
        return nuevo_indicador5_90
    if value==180:
        return nuevo_indicador5_180
    if value==365:
        return nuevo_indicador5_365

@app.callback(
    Output("sheets6", "figure"),
    [Input("radios", "value")]
)
def sheets_6(value):
    if value==90:
        return nuevo_indicador6_90
    if value==180:
        return nuevo_indicador6_180
    if value==365:
        return nuevo_indicador6_365

@app.callback(
    Output("treemap", "figure"),
    [Input("radios", "value")]
)
def treemap(value):
    if value==90:
        return fig_treemap_90
    if value==180:
        return fig_treemap_180
    if value==365:
        return fig_treemap_365
    
@app.callback(
    Output("bars1", "figure"),
    [Input("radios", "value")]
)
def bars1(value):
    if value==90:
        return fig_bars1_90
    if value==180:
        return fig_bars1_180
    if value==365:
        return fig_bars1_365

@app.callback(
    Output("bars2", "figure"),
    [Input("radios", "value")]
)
def bars2(value):
    if value==90:
        return fig_bars2_90
    if value==180:
        return fig_bars2_180
    if value==365:
        return fig_bars2_365
    
@app.callback(
    Output("table", "figure"),
    [Input("radios", "value")]
)
def table(value):
    if value==90:
        return fig_table_90
    if value==180:
        return fig_table_180
    if value==365:
        return fig_table_365
    
@app.callback(
    Output("timeseries", "figure"),
    [Input("radios", "value")]
)
def timeseries(value):
    if value==90:
        return fig_timeseries_90
    if value==180:
        return fig_timeseries_180
    if value==365:
        return fig_timeseries_365

@app.callback(
    Output("indicator_1", "figure"),
    [Input("radios", "value")]
)
def indicator1(value):
    if value==90:
        return fig_indicator_1_90
    if value==180:
        return fig_indicator_1_180
    if value==365:
        return fig_indicator_1_365
    
@app.callback(
    Output("indicator_2", "figure"),
    [Input("radios", "value")]
)
def indicator2(value):
    if value==90:
        return fig_indicator_2_90
    if value==180:
        return fig_indicator_2_180
    if value==365:
        return fig_indicator_2_365

@app.callback(
    Output("indicator_3", "figure"),
    [Input("radios", "value")]
)
def indicator3(value):
    if value==90:
        return fig_indicator_3_90
    if value==180:
        return fig_indicator_3_180
    if value==365:
        return fig_indicator_3_365

@app.callback(
    Output("indicator_4", "figure"),
    [Input("radios", "value")]
)
def indicator4(value):
    if value==90:
        return fig_indicator_4_90
    if value==180:
        return fig_indicator_4_180
    if value==365:
        return fig_indicator_4_365

@app.callback(
    Output("indicator_5", "figure"),
    [Input("radios", "value")]
)
def indicator5(value):
    if value==90:
        return fig_indicator_5_90
    if value==180:
        return fig_indicator_5_180
    if value==365:
        return fig_indicator_5_365

@app.callback(
    Output("indicator_6", "figure"),
    [Input("radios", "value")]
)
def indicator6(value):
    if value==90:
        return fig_indicator_6_90
    if value==180:
        return fig_indicator_6_180
    if value==365:
        return fig_indicator_6_365

@app.callback(
    Output("map", "figure"),
    [Input("radios", "value")]
)
def map(value):
    if value==90:
        return fig_map_90
    if value==180:
        return fig_map_180
    if value==365:
        return fig_map_365

@app.callback(
    Output("bars_3", "figure"),
    [Input("radios", "value")]
)
def bars3(value):
    if value==90:
        return fig_bars3_90
    if value==180:
        return fig_bars3_180
    if value==365:
        return fig_bars3_365

@app.callback(
    Output("bars_4", "figure"),
    [Input("radios", "value")]
)
def bars4(value):
    if value==90:
        return fig_bars4_90
    if value==180:
        return fig_bars4_180
    if value==365:
        return fig_bars4_365

@app.callback(
    Output("tabla_pestana_2", "figure"),
    [Input("radios", "value")]
)
def tabla_pestana_2(value):
    if value==90:
        return fig_tabla_pestana2_90
    if value==180:
        return fig_tabla_pestana2_180
    if value==365:
        return fig_tabla_pestana2_365


#------------------------------------------------------------------------------
# Corremos la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)