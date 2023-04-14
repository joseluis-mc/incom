# En este archivo vive la aplicación. Primero, importamos librerías.

# Dash para configurar y diseñar la aplicación:
from dash import Dash # Importamos Dash
from dash import Input, Output, html # Módulos adicionales para callbacks
import dash_html_components as html # Componentes básicos de HTML para layout
import dash_bootstrap_components as dbc # Componentes de Bootstrap

# Contenido de otros archivos
from tab_content import sales_tab, engagement_tab # Contenido de las pestañas

# Y algunas gráficas que integran un callback
from make_datasets import fig_time_paid, fig_time_direct, fig_time_organic

#------------------------------------------------------------------------------
# APLICACIÓN

# Inicializamos la aplicación
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP] # Integramos Bootstrap
)

app.config.suppress_callback_exceptions=True

# Configuramos el diseño de la aplicación
app.layout=html.Div(
    [
        # Barra de navegación
        dbc.NavbarSimple(
            brand="ETS-INCOM Dashboard",
            brand_href="#",
            color="dark",
            dark=True,
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
                                    tab_id='tab-1'),

                            # Pestaña de "engagement"
                            dbc.Tab(label='Engagement',
                                    tab_id='tab-2',
                                    disabled=True),
                        ],
                        id='card-tabs',
                        active_tab='tab-1'
                    )
                ),
                dbc.CardBody(id='card-content')
            ]
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
    if value=='fig_time_direct':
        return fig_time_direct
    if value=='fig_time_organic':
        return fig_time_organic
    if value=='fig_time_paid':
        return fig_time_paid

#------------------------------------------------------------------------------
# Corremos la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)