#### Importa librerías
# Data manipulation
import pandas as pd
import json

# Viz
import plotly
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go

#### Define funciones
def make_indicator(data, data_delta, var, title):
    #data['conversionRate'] = data['transactions'].sum() / data['sessions'].sum() * 100

    # Figura
    trace = go.Indicator(value = data.loc[:, var].sum(),
                         mode = 'number',
                         delta = {'reference': data_delta.loc[:, var].sum()*1.03}
                         )
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

def make_indicator_percentage(data, data_delta, var, title):
    data['conversionRate'] = data['transactions'].sum() / data['sessions'].sum() * 100

    # Figura
    trace = go.Indicator(value = data.loc[:, var].sum(),
                         mode = 'number',
                         delta = {'reference': data_delta.loc[:, var].sum()*1.03},
                         number = {'suffix': '%'}
                         )
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

def make_indicator_percentage2(data, data_delta, var, title):

    # Figura
    trace = go.Indicator(value = data.loc[:, var].sum(),
                         mode = 'number',
                         delta = {'reference': data_delta.loc[:, var].sum()*1.03},
                         number = {'suffix': '%'}
                         )
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
    fig.add_trace(go.Scatter(x=plot_data1.index, y=plot_data1.values, mode = 'lines', line = {'color': '#037E83'}, name='Organic Sessions'), row=1, col=1)
    fig.update_yaxes(title_text='Sessions', row=1, col=1)

    # Add traces for the second time series on the bottom subplot
    fig.add_trace(go.Scatter(x=plot_data2.index, y=plot_data2.values, mode = 'lines', line = {'color': '#EF7000'}, name='INCOM Sessions'), row=2, col=1)
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
                 barmode='group',
                 labels={
                     'sessions': 'Sessions',
                     'source': 'Source'
                 }
                 )


    # Update the layout of the figure to improve the overall appearance
    #fig.update_layout(width = 1000, height = 500)
    
    
    fig.update_layout(#title = 'Sessions by campaign source',
                      title_x = .5,
                      #plot_bgcolor='#F9F9F9',
                      #paper_bgcolor='#F9F9F9'
                      template = 'simple_white',
                      margin = dict(t=20, l=0, r=0, b=0)
                    )
    
    fig.update_traces(
        marker_color = '#037E83'
    )
    return fig

def try_parse(text):
    try:
        return text.split('in011-')[1][:3]
    except:
        return text

def make_bars2(data):
    data['type'] = data['campaign'].apply(lambda x: try_parse(x))
    plot_data = data.groupby(['type'])[['sessions']].sum().reset_index()
    plot_data = plot_data.sort_values(by = 'sessions')
    
    # Create plot
    fig = px.bar(plot_data,
                 y='type',
                 x='sessions',
                 orientation='h',
                 barmode='group',
                 labels={
                     'sessions': 'Sessions',
                     'type': 'Type'
                 }
                 )

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

    fig.update_yaxes(tickwidth=0.5)

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
                     color_discrete_sequence=['#037E83', '#EF7000', '#F7B524'],
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

def make_timeseries(data, col):
    title = f'Weekly search trend for: {col} from México'
    plot_data = data.resample(rule = 'w').sum()
    # Add traces for the first time series on the top subplot
    fig = px.line(data_frame=plot_data, y = col, labels={'date': ''})
    
    # Update the layout of the figure to improve the overall appearance
    #fig.update_layout(width = 1000, height = 500)
    
    fig.update_layout(title = title,
                  title_x = .5,
                  #plot_bgcolor='#F9F9F9',
                  #paper_bgcolor='#F9F9F9',
                  showlegend = True,
                  hovermode = 'x unified',
                  template = 'simple_white'
                )
    
    fig.update_layout(margin = dict(t=30, l=25, r=25, b=0))

    fig.update_traces(
        line_color = '#037E83'
    )
    
    return fig

def make_choropleth(data):
    open_file = open('incom/datasets/mexico_estados.json')

    polygon = json.load(open_file)

    fig = px.choropleth(data,
                        geojson=polygon,
                        locations='region',
                        featureidkey='properties.name',
                        color='sessions',
                        #title='Sessions by Region',
                        color_continuous_scale='Teal')

    fig.update_geos(showcountries=True,
                    showcoastlines=True,
                    #fitbounds='locations',
                    lataxis_range=[15,30], lonaxis_range=[-115, -90]
                )
    
    fig.update(layout_coloraxis_showscale=False)

    fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
    
    return fig

def make_bars3(data):
    plot_data = data.groupby(['region'])[['sessions']].sum().nlargest(5, columns = 'sessions').reset_index()
    plot_data = plot_data.sort_values(by = 'sessions')
    
    # Create plot
    fig = px.bar(plot_data,
                 y='region',
                 x='sessions',
                 orientation='h',
                 barmode='group',
                 labels = {
                     'sessions': 'Sessions',
                     'region': 'Region'
                 }
                 )

    # Update the layout of the figure to improve the overall appearance
    #fig.update_layout(width = 1000, height = 500)
    
    fig.update_layout(#title = 'Sessions by campaign source',
                      title_x = .5,
                      #plot_bgcolor='#F9F9F9',
                      #paper_bgcolor='#F9F9F9'
                      template = 'simple_white',
                      margin = dict(t=20, l=0, r=0, b=0)
                    )
    
    fig.update_traces(
        marker_color = '#037E83'
    )

    return fig

def make_bars4(data):
    plot_data = data.set_index('hour').loc[['00','01','02',
                          '03','04','05',
                          '06','07','08',
                          '09','10','11',
                          '12','13','14',
                          '15','16','17',
                          '18','19','20',
                          '21','22','23'], :]
    
    # Create plot
    fig = px.bar(plot_data,
                 y='sessions',
                 barmode='group',
                 labels = {
                     'hour': 'Hour',
                     'sessions': 'Sessions'
                 }
                 )


    # Update the layout of the figure to improve the overall appearance
    #fig.update_layout(width = 1000, height = 500)
    
    
    fig.update_layout(#title = 'Sessions by campaign source',
                      title_x = .5,
                      #plot_bgcolor='#F9F9F9',
                      #paper_bgcolor='#F9F9F9'
                      template = 'simple_white',
                      margin = dict(t=20, l=0, r=0, b=0)
                    )
    
    fig.update_traces(
        marker_color = '#037E83'
    )

    return fig

def make_table2(data):
    fig = go.Figure(
        data = [
            go.Table(
                header = dict(
                    values = data.columns.tolist(),
                    line_color = '#EF7000',
                    fill_color = '#037E83',
                    font = dict(
                        color = 'white',
                        size = 12
                    ),
                    height = 40
                ),
                cells = dict(
                    values = [
                        data.campaign,
                        data.sessions,
                        data.users,
                        data.adCost,
                        data.bounceRate,
                        data.avgSessionDuration,
                        data.transactions,
                        data.transactionRevenue
                    ],
                    line_color = '#EF7000',
                    fill_color = 'white',
                    font = dict(
                        color = 'black',
                        size = 11.5
                    ),
                    align=['left','left','left','left',
                    'left','left','left','left'],
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

#### Carga datos
# Pestaña 1
indicadores_sheets = pd.read_pickle('incom/datasets/indicadores_sheets.pkl')
organic_sessions_ts = pd.read_pickle('incom/datasets/organic_sessions_ts.pkl')
paid_sessions_ts = pd.read_pickle('incom/datasets/paid_sessions_ts.pkl')
campaign_detail = pd.read_pickle('incom/datasets/campaign_detail.pkl')
paid_groupings = pd.read_pickle('incom/datasets/paid_groupings.pkl')

#Pestaña 2
paid_indicators = pd.read_pickle('incom/datasets/paid_indicators.pkl')
organic_indicators = pd.read_pickle('incom/datasets/organic_indicators.pkl')
search_trends = pd.read_pickle('incom/datasets/search_trends.pkl')
paid_map = pd.read_pickle('incom/datasets/paid_map.pkl')
paid_hours = pd.read_pickle('incom/datasets/paid_hours.pkl')
summary_table = pd.read_pickle('incom/datasets/summary_table.pkl')


#### Plots Pestaña 1
# Indicadores
nuevo_indicador1 = make_indicator(indicadores_sheets, indicadores_sheets, 'eReg Reached', 'eReg Reached')
nuevo_indicador2 = make_indicator(indicadores_sheets, indicadores_sheets, 'Account Creation Intent', 'Account Creation Intent')
nuevo_indicador3 = make_indicator(indicadores_sheets, indicadores_sheets, 'Account Creation Success', 'Account Creation Success')
nuevo_indicador4 = make_indicator(indicadores_sheets, indicadores_sheets, 'Register For a Test Intent', 'Register For a Test Intent')
nuevo_indicador5 = make_indicator(indicadores_sheets, indicadores_sheets, 'Order Confirmation', 'Order Confirmation')
nuevo_indicador6 = make_indicator_percentage2(indicadores_sheets, indicadores_sheets, 'ROI', 'ROI')

# Treemap
fig_treemap = make_tree_paid_sources(paid_groupings, 'Campaigns by Channel Grouping')

# Bars
fig_bars1 = make_bars(campaign_detail)
fig_bars2 = make_bars2(campaign_detail)

# Table
fig_table = make_table(campaign_detail[['campaign','source','medium','sessions']])

# TimeSeries
fig_timeseries = make_double_timeseries(organic_sessions_ts, paid_sessions_ts, 'sessions', 'Weekly sessions')




#### Plots Pestaña 2
# Indicadores
fig_indicator_1 = make_indicator(organic_indicators,
                                 organic_indicators,
                                 'sessions',
                                 'Organic sessions')
fig_indicator_2 = make_indicator(organic_indicators,
                                 organic_indicators,
                                 'transactions',
                                 'Organic transactions')
fig_indicator_3 = make_indicator_percentage(organic_indicators,
                                 organic_indicators,
                                 'conversionRate',
                                 'Conversion rate %')
fig_indicator_4 = make_indicator(paid_indicators,
                                 paid_indicators,
                                 'sessions',
                                 'Organic sessions')
fig_indicator_5 = make_indicator(paid_indicators,
                                 paid_indicators,
                                 'transactions',
                                 'Organic transactions')
fig_indicator_6 = make_indicator_percentage(paid_indicators,
                                 paid_indicators,
                                 'conversionRate',
                                 'Conversion rate %')

# TimeSeries
search_term1 =  make_timeseries(search_trends, 'TOEFL')
search_term2 =  make_timeseries(search_trends, 'TOEFL IBT MEXICO')
search_term3 =  make_timeseries(search_trends, 'MEXICO EXAMEN INGLES')
search_term4 =  make_timeseries(search_trends, 'CERTIFICACION DE INGLES')
search_term5 =  make_timeseries(search_trends, 'TOEFL ONLINE')
#fig_timeseries_pestana2 = make_timeseries(search_trends, 'Weekly search trend for: TOEFL IBT from México')

# Map
fig_map = make_choropleth(paid_map)

# Bars3
fig_bars3 = make_bars3(paid_map)

# Bars4
fig_bars4 = make_bars4(paid_hours)

# Bars4
fig_tabla_pestana2 = make_table2(summary_table)