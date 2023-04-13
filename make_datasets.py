# Data manipulation
import pandas as pd
import json

# Viz
import plotly
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go

def make_indicator(data, data_delta, var, title, subset):
    # Figura
    trace = go.Indicator(value = data.loc[subset, var].sum(),
                         mode = 'number',
                         delta = {'reference': data_delta.loc[subset, var].sum()*1.03})
    fig = go.Figure(data = trace)
    
    # Dimensiones
    fig.update_layout(width = 400,height = 150)

#     # Estética
    fig.update_layout(plot_bgcolor='white',
                      paper_bgcolor='white',
                      #title = title,
                      title_x = .5)
    # Fonts
    fig.update_traces(title_font_size = 25,
                      title_font_family = 'Open Sans',
                      number_font_size = 50,
                      number_font_family = 'Open Sans',
                      delta_font_size = 25,
                      delta_font_family = 'Open Sans',)
    
    return fig

def make_double_timeseries(data, var, title):
    plot_data1 = data.resample(on = 'date', rule = 'w')['sessions'].sum()
    plot_data2 = data.resample(on = 'date', rule = 'w')['transactions'].sum()
    
    # Create subplots with 2 rows and 1 column
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03)

    # Add traces for the first time series on the top subplot
    fig.add_trace(go.Scatter(x=plot_data1.index, y=plot_data1.values, name='Sessions'), row=1, col=1)
    fig.update_yaxes(title_text='Sessions', row=1, col=1)

    # Add traces for the second time series on the bottom subplot
    fig.add_trace(go.Scatter(x=plot_data2.index, y=plot_data2.values, name='Transactions'), row=2, col=1)
    fig.update_yaxes(title_text='Transactions', row=2, col=1)

    # Update the layout of the figure to improve the overall appearance
    fig.update_layout(width = 1300, height = 500, title_text='Two Time Series with Separate Y-Axes')
    
    
    fig.update_layout(title = title,
                  title_x = .5,
                  yaxis_title =var,
                  plot_bgcolor='#F9F9F9',
                  paper_bgcolor='#F9F9F9',
                  showlegend = False,
                  hovermode = 'x unified')
    return fig

def make_hbar_search_engines(data, var, title):
    plot_data = data.sort_values(by = var, ascending = False).nlargest(5, var)
    # Manipulación de datos
    fig = go.Figure(go.Bar(
            y = plot_data['source'].values.tolist(),
            x = plot_data[var].values.tolist(),
            orientation='h'))

    
    # Dimensiones
    fig.update_layout(width = 620, height = 450)
    
    # Colores de línea y marcadores
    
    # Estilos
    fig.update_layout(#title = title,
                      #title_x = .5,
                      xaxis_title = 'Sesiones',
                      yaxis_title = 'Buscador',
                      plot_bgcolor='#F9F9F9',
                      paper_bgcolor='#F9F9F9',
                      showlegend = False)
    return fig

def make_hbar_social_network(data, var, title):
    plot_data = data[data['socialNetwork']!='(not set)'].sort_values(by = var, ascending = False).nlargest(7, var)
    # Manipulación de datos
    fig = go.Figure(go.Bar(
            y = plot_data['socialNetwork'].values.tolist(),
            x = plot_data[var].values.tolist(),
            orientation='h'))

    
    # Dimensiones
    fig.update_layout(width = 620, height = 450)
    
    # Colores de línea y marcadores
    
    # Estilos
    fig.update_layout(#title = title,
                      #title_x = .5,
                      xaxis_title = 'Sesiones',
                      yaxis_title = 'Red Social',
                      plot_bgcolor='#F9F9F9',
                      paper_bgcolor='#F9F9F9',
                      showlegend = False)
    return fig

def make_tree_paid_sources(data, title):
    plot_data = data[~(data['channelGrouping'].isin(['Direct','Organic Search']))]
    fig = px.treemap(plot_data,
                     path=[px.Constant("all"), 'channelGrouping', 'medium'],
                     values='sessions',
                     title = title)
    
    fig.update_traces(root_color="lightgrey")
    fig.update_layout(title = title,
                  width = 1300,
                  height = 500,    
                  title_x = .5,
                  plot_bgcolor='#F9F9F9',
                  paper_bgcolor='#F9F9F9')
    
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    
    return fig

# Import data
data_indicators = pd.read_pickle('./datasets/data_indicators.pkl')
data_time_direct = pd.read_pickle('./datasets/data_time_direct.pkl')
data_time_organic = pd.read_pickle('./datasets/data_time_organic.pkl')
data_time_paid = pd.read_pickle('./datasets/data_time_paid.pkl')
data_search_engines = pd.read_pickle('./datasets/data_search_engines.pkl')
data_social_networks = pd.read_pickle('./datasets/data_social_networks.pkl')
data_paid_sources = pd.read_pickle('./datasets/data_paid_sources.pkl')

# KPIs
# Hard coded lists of mediums
paid_mediums = ['cpc', 'ppc', 'cpm',
                'cpv', 'cpp', 'cpt', 'paid_search',
                'dis', 'display', 'referral',
                'social', 'soc', 'sppc', 'vid',
                'youtubevideo', 'blog', 'paid_social',
                'sppc_native', 'default_ad', 'aud',
                'cnt', 'video', 'Video', 'blog', 'Blog',
                'email', 'Email', 'text_ad', 'banner',
                'Banner', 'banners', 'Banners', 'Display', 'reels']

organic_mediums = ['organic', 'Organic-Social-WW', 'Organic_Social']

direct_mediums = ['(none)']

unknown_mediums = paid_mediums.copy()
unknown_mediums.extend(organic_mediums)
unknown_mediums.extend(direct_mediums)

direct = data_indicators['medium']=='(none)'
organic = data_indicators['medium'].isin(organic_mediums) 
paid = data_indicators['medium'].isin(paid_mediums)
unknown = ~(data_indicators['medium'].isin(unknown_mediums))

fig_indicator_1 = make_indicator(data_indicators,
                                 data_indicators,
                                 'sessions',
                                 'Sesiones - Directas', 
                                 direct)
fig_indicator_2 = make_indicator(data_indicators,
                                 data_indicators,
                                 'transactions',
                                 'Transacciones - Directas', 
                                 direct)
fig_indicator_3 = make_indicator(data_indicators,
                                 data_indicators,
                                 'sessions',
                                 'Sesiones - Adquiridas', 
                                 paid)
fig_indicator_4 = make_indicator(data_indicators,
                                 data_indicators,
                                 'transactions',
                                 'Transacciones - Adquiridas', 
                                 paid)
fig_indicator_5 = make_indicator(data_indicators,
                                 data_indicators,
                                 'sessions',
                                 'Sesiones - Orgánicas', 
                                 organic)
fig_indicator_6 = make_indicator(data_indicators,
                                 data_indicators,
                                 'transactions',
                                 'Transacciones - Orgánicas', 
                                 organic)

# Time Series Explorer
fig_time_direct = make_double_timeseries(data_time_direct, 'sessions', 'Desempeño 120 días directas')
fig_time_organic = make_double_timeseries(data_time_organic, 'sessions', 'Desempeño 120 días orgánicas')
fig_time_paid = make_double_timeseries(data_time_paid, 'sessions', 'Desempeño 120 días adquiridas')

# Search Engines
fig_search_engines = make_hbar_search_engines(data_search_engines, 'sessions', 'Sesiones orgánicas por buscador')

# Social Network
fig_social_networks = make_hbar_social_network(data_social_networks, 'sessions', 'Sesiones adquiridas por red social')

# Paid Sources
fig_paid_sources = make_tree_paid_sources(data_paid_sources, 'Grouping/Medium')
