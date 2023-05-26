#!/usr/bin/env python
# coding: utf-8

# # Trae librerías

# In[1]:


# Data manipulation
import pandas as pd
import numpy as np
import json

# Viz
import plotly
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go


# # Define funciones

# In[2]:


def make_indicator(data, data_delta, var, title):
    data['conversionRate'] = data['transactions'].sum() / data['sessions'].sum() * 100  
    # Figura
    trace = go.Indicator(value = data.loc[:, var].sum(),
                         mode = 'number',
                         delta = {'reference': data_delta.loc[:, var].sum()*1.03})
    fig = go.Figure(data = trace)
    
    if var == 'conversionRate':
        trace = go.Indicator(value = data['transactions'].sum() / data['sessions'].sum() * 100,
                         mode = 'number',
                         delta = {'reference': data_delta.loc[:, var].sum()*1.03})
        fig = go.Figure(data = trace)
    
    # Dimensiones
    #fig.update_layout(width = 200,height = 200)

    # Estética
    fig.update_layout(plot_bgcolor='white',
                      paper_bgcolor='white',
                      #title = title,
                      title_x = .5)
    # Fonts
    fig.update_traces(title_font_size = 25,
                      title_font_family = 'Open Sans',
                      number_font_size = 50,
                      number_font_family = 'Open Sans',
                      number_font_color = 'black',
                      delta_font_size = 25,
                      delta_font_family = 'Open Sans',)
    
    return fig

def make_double_timeseries(data, data2, var, title):
    plot_data1 = data.resample(on = 'date', rule = 'w')[var].sum()
    plot_data2 = data2.resample(on = 'date', rule = 'w')[var].sum()
    
    # Create subplots with 2 rows and 1 column
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03)

    # Add traces for the first time series on the top subplot
    fig.add_trace(go.Scatter(x=plot_data1.index, y=plot_data1.values, mode = 'lines', line = {'color': '#EF7000'}, name='Organic Sessions'), row=1, col=1)
    fig.update_yaxes(title_text='Sessions', row=1, col=1)

    # Add traces for the second time series on the bottom subplot
    fig.add_trace(go.Scatter(x=plot_data2.index, y=plot_data2.values, mode = 'lines', line = {'color': '#F7B524'}, name='INCOM Sessions'), row=2, col=1)
    fig.update_yaxes(title_text='Sessions', row=2, col=1)

    # Update the layout of the figure to improve the overall appearance
    #fig.update_layout(width = 1000, height = 500)
    
    
    fig.update_layout(#title = title,
                  title_x = .5,
                  #plot_bgcolor='#F9F9F9',
                  #paper_bgcolor='#F9F9F9',
                  showlegend = True,
                  hovermode = 'x unified',
                  template = 'simple_white'
                )
    
    fig.update_layout(margin = dict(t=30, l=25, r=25, b=0))

    return fig

def make_bars(data):
    plot_data = data.groupby(['source'])[['sessions']].sum().reset_index()
    plot_data = plot_data.sort_values(by = 'sessions')
    
    # Create plot
    fig = px.bar(plot_data,
                 y='source',
                 x='sessions',
                 orientation='h',
                 barmode='group')


    # Update the layout of the figure to improve the overall appearance
    #fig.update_layout(width = 1000, height = 500)
    
    
    fig.update_layout(#title = 'Sessions by campaign source',
                      title_x = .5,
                      #plot_bgcolor='#F9F9F9',
                      #paper_bgcolor='#F9F9F9',
                      template = 'simple_white',
                      margin = dict(t=20, l=0, r=0, b=0)
                    )
    
    fig.update_traces(
        marker_color = '#037E83'
    )

    return fig

def make_bars2(data):
    data['type'] = data['campaign'].apply(lambda x: x.split('in011-')[1][:3])
    plot_data = data.groupby(['type'])[['sessions']].sum().reset_index()
    plot_data = plot_data.sort_values(by = 'sessions')
    
    # Create plot
    fig = px.bar(plot_data,
                 y='type',
                 x='sessions',
                 orientation='h',
                 barmode='group')


    # Update the layout of the figure to improve the overall appearance
    #fig.update_layout(width = 1000, height = 500)
    
    
    fig.update_layout(#title = 'Sessions by campaign type',
                      title_x = .5,
                      #plot_bgcolor='#F9F9F9',
                      #paper_bgcolor='#F9F9F9',
                      template = 'simple_white',
                      margin = dict(t=20, l=0, r=0, b=0)
                    )
    
    fig.update_traces(
        marker_color = '#037E83'
    )

    return fig

def make_table(data):
    fig = go.Figure(
        data = [
            go.Table(
                header = dict(
                    values = data.columns.tolist(),
                    line_color = '#EF7000',
                    fill_color = '#037E83',
                    font = dict(
                        color = 'white',
                        size = 16
                    ),
                    height = 40
                ),
                cells = dict(
                    values = [
                        data.campaign,
                        data.source,
                        data.medium,
                        data.sessions
                    ],
                    line_color = '#EF7000',
                    fill_color = 'white',
                    font = dict(
                        color = 'black',
                        size = 14
                    ),
                    align = ['left','left','left','center'],
                    height = 30
                ),
                columnwidth = [300,100,100]
            )
        ]
    )

    # Customize the layout
    fig.update_layout(title='Table Example')

    # Remove the title
    fig.update_layout(title=None)

    # Adjust the margin and autosize properties
    fig.update_layout(
        margin=dict(l=20, r=20, t=30, b=0),
        autosize=True
    )
    return fig

def make_tree_paid_sources(data, title):
    plot_data = data[~(data['channelGrouping'].isin(['Direct','Organic Search', 'Referral']))]
    fig = px.treemap(plot_data,
                     path=[px.Constant("all"), 'channelGrouping', 'campaign'],
                     color_discrete_sequence=['#037E83', '#F7B524'],
                     values='sessions',
                     #title = title
                    )
    
    fig.update_traces(root_color="lightgrey")
    fig.update_layout(#title = title,
                  #width = 950,
                  #height = 500,    
                  title_x = .5,
                  #plot_bgcolor='#F9F9F9',
                  #paper_bgcolor='#F9F9F9',
                  template = 'simple_white'
                )
    
    fig.update_layout(margin = dict(t=0, l=25, r=25, b=0))
    
    return fig


# # Carga sets

# In[3]:


organic_indicators = pd.read_pickle('incom/datasets/organic_indicators.pkl')
paid_indicators = pd.read_pickle('incom/datasets/paid_indicators.pkl')
organic_sessions_ts = pd.read_pickle('incom/datasets/organic_sessions_ts.pkl')
paid_sessions_ts = pd.read_pickle('incom/datasets/paid_sessions_ts.pkl')
campaign_detail = pd.read_pickle('incom/datasets/campaign_detail.pkl')
paid_groupings = pd.read_pickle('incom/datasets/paid_groupings.pkl')


# # Haz plots

# In[4]:


# Indicadores
fig_indicator_1 = make_indicator(organic_indicators,
                                 organic_indicators,
                                 'sessions',
                                 'Organic sessions')
fig_indicator_2 = make_indicator(organic_indicators,
                                 organic_indicators,
                                 'transactions',
                                 'Organic transactions')
fig_indicator_3 = make_indicator(organic_indicators,
                                 organic_indicators,
                                 'conversionRate',
                                 'Conversion rate %')
fig_indicator_4 = make_indicator(paid_indicators,
                                 paid_indicators,
                                 'sessions',
                                 'Paid sessions')
fig_indicator_5 = make_indicator(paid_indicators,
                                 paid_indicators,
                                 'transactions',
                                 'Paid transactions')
fig_indicator_6 = make_indicator(paid_indicators,
                                 paid_indicators,
                                 'conversionRate',
                                 'Paid rate %')

# Treemap
fig_treemap = make_tree_paid_sources(paid_groupings, 'Campaigns by Channel Grouping')

# Bars
fig_bars1 = make_bars(campaign_detail)
fig_bars2 = make_bars2(campaign_detail)

# Table
fig_table = make_table(campaign_detail[['campaign','source','medium','sessions']])

# TimeSeries
fig_timeseries = make_double_timeseries(organic_sessions_ts, paid_sessions_ts, 'sessions', 'Weekly sessions')


# In[ ]:




