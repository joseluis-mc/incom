# En este archivo vive la aplicación. Primero, importamos librerías.

# Dash para configurar y diseñar la aplicación:
from dash import Dash # Importamos Dash
from dash import Input, Output, html # Módulos adicionales para callbacks
from dash import html # Componentes básicos de HTML para layout
import dash_bootstrap_components as dbc # Componentes de Bootstrap

# Contenido de otros archivos
from tab_content import sales_tab, engagement_tab # Contenido de las pestañas
from tab_content import search_term1
from tab_content import search_term2
from tab_content import search_term3
from tab_content import search_term4
from tab_content import search_term5

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
        return search_term1
    if value=='TOEFL IBT MEXICO':
        return search_term2
    if value=='MEXICO EXAMEN INGLES':
        return search_term3
    if value=='CERTIFICACION DE INGLES':
        return search_term4
    if value=='TOEFL ONLINE':
        return search_term5

#------------------------------------------------------------------------------
# Corremos la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)