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
    data['source'] = data['source'].str.capitalize().str.replace('Paid_google', 'Google - Paid')
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
                    values = ['Campaign','Source','Medium','Sessions'],
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
                    values = [
                        'campaign',
                        'sessions',
                        'users',
                        'adCost',
                        'bounceRate',
                        'avgSessionDuration',
                        'transactions',
                        'transaction - order confirmation'
                    ],
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
                columnwidth = [300, 100, 100, 100, 100, 100, 100, 100]
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
indicadores_sheets_90 = pd.read_pickle('incom/datasets/indicadores_sheets_90.pkl')
indicadores_sheets_180 = pd.read_pickle('incom/datasets/indicadores_sheets_180.pkl')
indicadores_sheets_365 = pd.read_pickle('incom/datasets/indicadores_sheets_365.pkl')

organic_sessions_ts = pd.read_pickle('incom/datasets/organic_sessions_ts.pkl')
paid_sessions_ts = pd.read_pickle('incom/datasets/paid_sessions_ts.pkl')
campaign_detail = pd.read_pickle('incom/datasets/campaign_detail.pkl')
paid_groupings = pd.read_pickle('incom/datasets/paid_groupings.pkl')

organic_sessions_ts_90 = pd.read_pickle('incom/datasets/organic_sessions_ts_90.pkl')
paid_sessions_ts_90 = pd.read_pickle('incom/datasets/paid_sessions_ts_90.pkl')
campaign_detail_90 = pd.read_pickle('incom/datasets/campaign_detail_90.pkl')
paid_groupings_90 = pd.read_pickle('incom/datasets/paid_groupings_90.pkl')

organic_sessions_ts_180 = pd.read_pickle('incom/datasets/organic_sessions_ts_180.pkl')
paid_sessions_ts_180 = pd.read_pickle('incom/datasets/paid_sessions_ts_180.pkl')
campaign_detail_180 = pd.read_pickle('incom/datasets/campaign_detail_180.pkl')
paid_groupings_180 = pd.read_pickle('incom/datasets/paid_groupings_180.pkl')

organic_sessions_ts_365 = pd.read_pickle('incom/datasets/organic_sessions_ts_365.pkl')
paid_sessions_ts_365 = pd.read_pickle('incom/datasets/paid_sessions_ts_365.pkl')
campaign_detail_365 = pd.read_pickle('incom/datasets/campaign_detail_365.pkl')
paid_groupings_365 = pd.read_pickle('incom/datasets/paid_groupings_365.pkl')

#Pestaña 2
search_trends = pd.read_pickle('incom/datasets/search_trends.pkl')

paid_indicators = pd.read_pickle('incom/datasets/paid_indicators.pkl')
organic_indicators = pd.read_pickle('incom/datasets/organic_indicators.pkl')
paid_map = pd.read_pickle('incom/datasets/paid_map.pkl')
paid_hours = pd.read_pickle('incom/datasets/paid_hours.pkl')
summary_table = pd.read_pickle('incom/datasets/summary_table.pkl')

search_trends_365 = pd.read_pickle('incom/datasets/search_trends_365.pkl')

paid_indicators_90 = pd.read_pickle('incom/datasets/paid_indicators_90.pkl')
organic_indicators_90 = pd.read_pickle('incom/datasets/organic_indicators_90.pkl')
paid_map_90 = pd.read_pickle('incom/datasets/paid_map_90.pkl')
paid_hours_90 = pd.read_pickle('incom/datasets/paid_hours_90.pkl')
summary_table_90 = pd.read_pickle('incom/datasets/summary_table_90.pkl')

paid_indicators_180 = pd.read_pickle('incom/datasets/paid_indicators_180.pkl')
organic_indicators_180 = pd.read_pickle('incom/datasets/organic_indicators_180.pkl')
paid_map_180 = pd.read_pickle('incom/datasets/paid_map_180.pkl')
paid_hours_180 = pd.read_pickle('incom/datasets/paid_hours_180.pkl')
summary_table_180 = pd.read_pickle('incom/datasets/summary_table_180.pkl')

paid_indicators_365 = pd.read_pickle('incom/datasets/paid_indicators_365.pkl')
organic_indicators_365 = pd.read_pickle('incom/datasets/organic_indicators_365.pkl')
paid_map_365 = pd.read_pickle('incom/datasets/paid_map_365.pkl')
paid_hours_365 = pd.read_pickle('incom/datasets/paid_hours_365.pkl')
summary_table_365 = pd.read_pickle('incom/datasets/summary_table_365.pkl')

#### Plots Pestaña 1
# Indicadores
nuevo_indicador1_90 = make_indicator(indicadores_sheets_90, indicadores_sheets_90, 'eREG Reached', 'eReg Reached')
nuevo_indicador2_90 = make_indicator(indicadores_sheets_90, indicadores_sheets_90, 'Account Creation Intent', 'Account Creation Intent')
nuevo_indicador3_90 = make_indicator(indicadores_sheets_90, indicadores_sheets_90, 'Account Creation Success', 'Account Creation Success')
nuevo_indicador4_90 = make_indicator(indicadores_sheets_90, indicadores_sheets_90, 'Register For a Test Intent', 'Register For a Test Intent')
nuevo_indicador5_90 = make_indicator(indicadores_sheets_90, indicadores_sheets_90, 'Order Confirmation', 'Order Confirmation')
nuevo_indicador6_90 = make_indicator_percentage2(indicadores_sheets_90, indicadores_sheets_90, 'ROI', 'ROI')

nuevo_indicador1_180 = make_indicator(indicadores_sheets_180, indicadores_sheets_180, 'eREG Reached', 'eReg Reached')
nuevo_indicador2_180 = make_indicator(indicadores_sheets_180, indicadores_sheets_180, 'Account Creation Intent', 'Account Creation Intent')
nuevo_indicador3_180 = make_indicator(indicadores_sheets_180, indicadores_sheets_180, 'Account Creation Success', 'Account Creation Success')
nuevo_indicador4_180 = make_indicator(indicadores_sheets_180, indicadores_sheets_180, 'Register For a Test Intent', 'Register For a Test Intent')
nuevo_indicador5_180 = make_indicator(indicadores_sheets_180, indicadores_sheets_180, 'Order Confirmation', 'Order Confirmation')
nuevo_indicador6_180 = make_indicator_percentage2(indicadores_sheets_180, indicadores_sheets_180, 'ROI', 'ROI')

nuevo_indicador1_365 = make_indicator(indicadores_sheets_365, indicadores_sheets_365, 'eREG Reached', 'eReg Reached')
nuevo_indicador2_365 = make_indicator(indicadores_sheets_365, indicadores_sheets_365, 'Account Creation Intent', 'Account Creation Intent')
nuevo_indicador3_365 = make_indicator(indicadores_sheets_365, indicadores_sheets_365, 'Account Creation Success', 'Account Creation Success')
nuevo_indicador4_365 = make_indicator(indicadores_sheets_365, indicadores_sheets_365, 'Register For a Test Intent', 'Register For a Test Intent')
nuevo_indicador5_365 = make_indicator(indicadores_sheets_365, indicadores_sheets_365, 'Order Confirmation', 'Order Confirmation')
nuevo_indicador6_365 = make_indicator_percentage2(indicadores_sheets_365, indicadores_sheets_365, 'ROI', 'ROI')

# Treemap
fig_treemap = make_tree_paid_sources(paid_groupings, 'Campaigns by Channel Grouping')
fig_treemap_90 = make_tree_paid_sources(paid_groupings_90, 'Campaigns by Channel Grouping')
fig_treemap_180 = make_tree_paid_sources(paid_groupings_180, 'Campaigns by Channel Grouping')
fig_treemap_365 = make_tree_paid_sources(paid_groupings_365, 'Campaigns by Channel Grouping')

# Bars
fig_bars1 = make_bars(campaign_detail)
fig_bars2 = make_bars2(campaign_detail)
fig_bars1_90 = make_bars(campaign_detail_90)
fig_bars2_90 = make_bars2(campaign_detail_90)
fig_bars1_180 = make_bars(campaign_detail_180)
fig_bars2_180 = make_bars2(campaign_detail_180)
fig_bars1_365 = make_bars(campaign_detail_365)
fig_bars2_365 = make_bars2(campaign_detail_365)

# Table
fig_table = make_table(campaign_detail[['campaign','source','medium','sessions']])
fig_table_90 = make_table(campaign_detail_90[['campaign','source','medium','sessions']])
fig_table_180 = make_table(campaign_detail_180[['campaign','source','medium','sessions']])
fig_table_365 = make_table(campaign_detail_365[['campaign','source','medium','sessions']])

# TimeSeries
fig_timeseries = make_double_timeseries(organic_sessions_ts, paid_sessions_ts, 'sessions', 'Weekly sessions')
fig_timeseries_90 = make_double_timeseries(organic_sessions_ts_90, paid_sessions_ts_90, 'sessions', 'Weekly sessions')
fig_timeseries_180 = make_double_timeseries(organic_sessions_ts_180, paid_sessions_ts_180, 'sessions', 'Weekly sessions')
fig_timeseries_365 = make_double_timeseries(organic_sessions_ts_365, paid_sessions_ts_365, 'sessions', 'Weekly sessions')

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

fig_indicator_1_90 = make_indicator(organic_indicators_90,
                                 organic_indicators_90,
                                 'sessions',
                                 'Organic sessions')
fig_indicator_2_90 = make_indicator(organic_indicators_90,
                                 organic_indicators_90,
                                 'transactions',
                                 'Organic transactions')
fig_indicator_3_90 = make_indicator_percentage(organic_indicators_90,
                                 organic_indicators_90,
                                 'conversionRate',
                                 'Conversion rate %')
fig_indicator_4_90 = make_indicator(paid_indicators_90,
                                 paid_indicators_90,
                                 'sessions',
                                 'Organic sessions')
fig_indicator_5_90 = make_indicator(paid_indicators_90,
                                 paid_indicators_90,
                                 'transactions',
                                 'Organic transactions')
fig_indicator_6_90 = make_indicator_percentage(paid_indicators_90,
                                 paid_indicators_90,
                                 'conversionRate',
                                 'Conversion rate %')

fig_indicator_1_180 = make_indicator(organic_indicators_180,
                                 organic_indicators_180,
                                 'sessions',
                                 'Organic sessions')
fig_indicator_2_180 = make_indicator(organic_indicators_180,
                                 organic_indicators_180,
                                 'transactions',
                                 'Organic transactions')
fig_indicator_3_180 = make_indicator_percentage(organic_indicators_180,
                                 organic_indicators_180,
                                 'conversionRate',
                                 'Conversion rate %')
fig_indicator_4_180 = make_indicator(paid_indicators_180,
                                 paid_indicators_180,
                                 'sessions',
                                 'Organic sessions')
fig_indicator_5_180 = make_indicator(paid_indicators_180,
                                 paid_indicators_180,
                                 'transactions',
                                 'Organic transactions')
fig_indicator_6_180 = make_indicator_percentage(paid_indicators_180,
                                 paid_indicators_180,
                                 'conversionRate',
                                 'Conversion rate %')

fig_indicator_1_365 = make_indicator(organic_indicators_365,
                                 organic_indicators_365,
                                 'sessions',
                                 'Organic sessions')
fig_indicator_2_365 = make_indicator(organic_indicators_365,
                                 organic_indicators_365,
                                 'transactions',
                                 'Organic transactions')
fig_indicator_3_365 = make_indicator_percentage(organic_indicators_365,
                                 organic_indicators_365,
                                 'conversionRate',
                                 'Conversion rate %')
fig_indicator_4_365 = make_indicator(paid_indicators_365,
                                 paid_indicators_365,
                                 'sessions',
                                 'Organic sessions')
fig_indicator_5_365 = make_indicator(paid_indicators_365,
                                 paid_indicators_180,
                                 'transactions',
                                 'Organic transactions')
fig_indicator_6_365 = make_indicator_percentage(paid_indicators_365,
                                 paid_indicators_365,
                                 'conversionRate',
                                 'Conversion rate %')

# TimeSeries
search_term1 =  make_timeseries(search_trends, 'TOEFL')
search_term2 =  make_timeseries(search_trends, 'TOEFL IBT MEXICO')
search_term3 =  make_timeseries(search_trends, 'MEXICO EXAMEN INGLES')
search_term4 =  make_timeseries(search_trends, 'CERTIFICACION DE INGLES')
search_term5 =  make_timeseries(search_trends, 'TOEFL ONLINE')
#fig_timeseries_pestana2 = make_timeseries(search_trends, 'Weekly search trend for: TOEFL IBT from México')

search_term1_365 =  make_timeseries(search_trends_365, 'TOEFL')
search_term2_365 =  make_timeseries(search_trends_365, 'TOEFL IBT MEXICO')
search_term3_365 =  make_timeseries(search_trends_365, 'MEXICO EXAMEN INGLES')
search_term4_365 =  make_timeseries(search_trends_365, 'CERTIFICACION DE INGLES')
search_term5_365 =  make_timeseries(search_trends_365, 'TOEFL ONLINE')

# Map
fig_map = make_choropleth(paid_map)
fig_map_90 = make_choropleth(paid_map_90)
fig_map_180 = make_choropleth(paid_map_180)
fig_map_365 = make_choropleth(paid_map_365)

# Bars3
fig_bars3 = make_bars3(paid_map)
fig_bars3_90 = make_bars3(paid_map_90)
fig_bars3_180 = make_bars3(paid_map_180)
fig_bars3_365 = make_bars3(paid_map_365)

# Bars4
fig_bars4 = make_bars4(paid_hours)
fig_bars4_90 = make_bars4(paid_hours_90)
fig_bars4_180 = make_bars4(paid_hours_180)
fig_bars4_365 = make_bars4(paid_hours_365)

# Bars4
fig_tabla_pestana2 = make_table2(summary_table)
fig_tabla_pestana2_90 = make_table2(summary_table_90)
fig_tabla_pestana2_180 = make_table2(summary_table_180)
fig_tabla_pestana2_365 = make_table2(summary_table_365)