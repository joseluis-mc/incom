from dash import Dash, dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash import Input, Output, html
import plotly.graph_objects as go

indicador = go.Figure(go.Indicator(
    mode = "number+delta",
    value = 400,
    number = {"font":{"size":35}},
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

indicador.update_layout(
    paper_bgcolor="lightgray",
    height=150
)