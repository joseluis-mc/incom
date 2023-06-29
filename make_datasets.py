##### Importa librerías
# Data manipulation
import pandas as pd
# Google Auth
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
# Google Trends
from pytrends.request import TrendReq

##### Define Funciones básicas
def initialize_analytics_reporting():
    """Instatiate GA UA Reporting API V4 client"""
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        KEY_FILE_LOCATION, SCOPES)
    # Build the service object.
    service = build("analyticsreporting", "v4", credentials=credentials)
    return service

def metrics_dimensions_to_df(res):
    """Convert a non-empty response with metrics and dimensions to a dataframe."""
    report = res["reports"][0]
    dimensions = report["columnHeader"]["dimensions"]
    metrics = [
        m["name"] for m in report["columnHeader"]["metricHeader"]["metricHeaderEntries"]
    ]
    headers = [*dimensions, *metrics]

    data_rows = report["data"]["rows"]
    data = []
    for row in data_rows:
        data.append([*row["dimensions"], *row["metrics"][0]["values"]])

    return pd.DataFrame(data=data, columns=headers)

#####Define funciones de queries
def query_organica(query_metrics, query_dimensions, start, end, filename):
    # Define Query
    query = {'viewId':VIEW_ID,
             'samplingLevel': 'large',
             'pageSize': 1000,
             'dateRanges':[{'startDate':start, 'endDate':end}],
             'metrics':[{'expression':metric} for metric in query_metrics],
             'dimensions':[{'name': dimension} for dimension in query_dimensions],
             'filtersExpression': f'ga:medium==organic',
             'orderBys':[{'fieldName':'ga:sessions', 'sortOrder':'DESCENDING'}]
        }
    
    try:
        # Realiza Query
        response = service.reports().batchGet(body={'reportRequests':[query]}).execute()
        # Parsea respuesta DataFrame
        df = metrics_dimensions_to_df(response)
        # Corrige data types
        for i in query_metrics:
            df[i] = pd.to_numeric(df[i])
        
        for i in query_dimensions:
            if i == 'ga:date':
                df['ga:date'] = pd.to_datetime(df['ga:date'])
            else:
                pass
        # Corrige nombres de columnas
        new_cols = [x.split(':')[1] for x in df.columns]
        df.columns = new_cols
        # Guarda
        df.to_pickle(f'incom/datasets/{filename}')
    except Exception as e:
        print(e)
        print(f'Algo se rompió en {filename}. Volviendo a intentar query.')
        try:
            # Realiza Query
            response = service.reports().batchGet(body={'reportRequests':[query]}).execute()
            # Parsea respuesta DataFrame
            df = metrics_dimensions_to_df(response)
            # Corrige data types
            for i in query_metrics:
                df[i] = pd.to_numeric(df[i])
            
            for i in query_dimensions:
                if i == 'ga:date':
                    df['ga:date'] = pd.to_datetime(df['ga:date'])
                else:
                    pass
            # Corrige nombres de columnas
            new_cols = [x.split(':')[1] for x in df.columns]
            df.columns = new_cols
            # Guarda
            df.to_pickle(f'incom/datasets/{filename}')
        except Exception as e2:
            print(e2)
            print(f'Algo se rompió de nuevo en {filename}. Terminando query.')

def query_incom(query_metrics, query_dimensions, start, end, filename):
    # Define Query
    query = {'viewId':VIEW_ID,
            'samplingLevel': 'large',
            'pageSize': 1000,
            'dateRanges':[{'startDate':start, 'endDate':end}],
            'metrics':[{'expression':metric} for metric in query_metrics],
            'dimensions':[{'name': dimension} for dimension in query_dimensions],
            'orderBys':[{'fieldName':'ga:sessions', 'sortOrder':'DESCENDING'}],
            'dimensionFilterClauses': [
                {'operator': 'OR',
                'filters': [
                            {'dimensionName': 'ga:campaign',
                            'operator': 'REGEXP',
                            'expressions': ['in011']},
                            {'dimensionName': 'ga:campaign',
                            'operator': 'EXACT',
                            'expressions': ['Mexico | TOEFL iBT']},
                            {'dimensionName': 'ga:campaign',
                            'operator': 'EXACT',
                            'expressions': ['TOEFL iBT | Retargeting']},
                            {'dimensionName': 'ga:campaign',
                            'operator': 'EXACT',
                            'expressions': ['TOEFL iBT | General | En Línea']},
                            {'dimensionName': 'ga:campaign',
                            'operator': 'EXACT',
                            'expressions': ['Mexico | TOEFL iBT | Paper Edition Dates']}]}]}
    
    try:
        # Realiza Query
        response = service.reports().batchGet(body={'reportRequests':[query]}).execute()
        # Parsea respuesta DataFrame
        df = metrics_dimensions_to_df(response)
        # Corrige data types
        for i in query_metrics:
            df[i] = pd.to_numeric(df[i])
        
        for i in query_dimensions:
            if i == 'ga:date':
                df['ga:date'] = pd.to_datetime(df['ga:date'])
            else:
                pass
        # Corrige nombres de columnas
        new_cols = [x.split(':')[1] for x in df.columns]
        df.columns = new_cols
        # Guarda
        df.to_pickle(f'incom/datasets/{filename}')
    except Exception as e:
        print(e)
        print(f'Algo se rompió en {filename}. Volviendo a intentar query.')
        try:
            # Realiza Query
            response = service.reports().batchGet(body={'reportRequests':[query]}).execute()
            # Parsea respuesta DataFrame
            df = metrics_dimensions_to_df(response)
        # Corrige data types
            for i in query_metrics:
                df[i] = pd.to_numeric(df[i])
            
            for i in query_dimensions:
                if i == 'ga:date':
                    df['ga:date'] = pd.to_datetime(df['ga:date'])
                else:
                    pass
            # Corrige nombres de columnas
            new_cols = [x.split(':')[1] for x in df.columns]
            df.columns = new_cols
            # Guarda
            df.to_pickle(f'incom/datasets/{filename}')
        except Exception as e2:
            print(e2)
            print(f'Algo se rompió de nuevo en {filename}. Terminando query.')

def query_incom_map(query_metrics, query_dimensions, start, end, filename):
    # Define Query
    query = {'viewId':VIEW_ID,
            'samplingLevel': 'large',
            'pageSize': 1000,
            'dateRanges':[{'startDate':start, 'endDate':end}],
            'metrics':[{'expression':metric} for metric in query_metrics],
            'dimensions':[{'name': dimension} for dimension in query_dimensions],
            'orderBys':[{'fieldName':'ga:sessions', 'sortOrder':'DESCENDING'}],
            'dimensionFilterClauses': [
                {'operator': 'OR',
                'filters': [
                            {'dimensionName': 'ga:campaign',
                            'operator': 'REGEXP',
                            'expressions': ['in011']},
                            {'dimensionName': 'ga:campaign',
                            'operator': 'EXACT',
                            'expressions': ['Mexico | TOEFL iBT']},
                            {'dimensionName': 'ga:campaign',
                            'operator': 'EXACT',
                            'expressions': ['TOEFL iBT | Retargeting']},
                            {'dimensionName': 'ga:campaign',
                            'operator': 'EXACT',
                            'expressions': ['TOEFL iBT | General | En Línea']},
                            {'dimensionName': 'ga:campaign',
                            'operator': 'EXACT',
                            'expressions': ['Mexico | TOEFL iBT | Paper Edition Dates']}]}]}
    
    try:
        # Realiza Query
        response = service.reports().batchGet(body={'reportRequests':[query]}).execute()
        # Parsea respuesta DataFrame
        df = metrics_dimensions_to_df(response)
        # Corrige data types
        for i in query_metrics:
            df[i] = pd.to_numeric(df[i])
        
        for i in query_dimensions:
            if i == 'ga:date':
                df['ga:date'] = pd.to_datetime(df['ga:date'])
            else:
                pass
        # Corrige nombres de columnas
        new_cols = [x.split(':')[1] for x in df.columns]
        df.columns = new_cols
        df = df[df['country']=='Mexico'].reset_index(drop = True)
        df = df[df['region']!='(not set)'].reset_index(drop = True)
        mapa = {
            'Nuevo Leon': 'Nuevo León',
            'Michoacan': 'Michoacán',
            'San Luis Potosi': 'San Luis Potosí',
            'Mexico City': 'Ciudad de México',
            'State of Mexico': 'México',
            'Queretaro': 'Querétaro',
            'Yucatan': 'Yucatán'}

        df['region'] = df['region'].replace(mapa)
        # Guarda
        df.to_pickle(f'incom/datasets/{filename}')
    except Exception as e:
        print(e)
        print(f'Algo se rompió en {filename}. Volviendo a intentar query.')
        try:
            # Realiza Query
            response = service.reports().batchGet(body={'reportRequests':[query]}).execute()
            # Parsea respuesta DataFrame
            df = metrics_dimensions_to_df(response)
        # Corrige data types
            for i in query_metrics:
                df[i] = pd.to_numeric(df[i])
            
            for i in query_dimensions:
                if i == 'ga:date':
                    df['ga:date'] = pd.to_datetime(df['ga:date'])
                else:
                    pass
            # Corrige nombres de columnas
            new_cols = [x.split(':')[1] for x in df.columns]
            df.columns = new_cols
            df = df[df['country']=='Mexico'].reset_index(drop = True)
            df = df[df['region']!='(not set)'].reset_index(drop = True)
            mapa = {
                'Nuevo Leon': 'Nuevo León',
                'Michoacan': 'Michoacán',
                'San Luis Potosi': 'San Luis Potosí',
                'Mexico City': 'Ciudad de México',
                'State of Mexico': 'México',
                'Queretaro': 'Querétaro',
                'Yucatan': 'Yucatán'}

            df['region'] = df['region'].replace(mapa)
            # Guarda
            df.to_pickle(f'incom/datasets/{filename}')
        except Exception as e2:
            print(e2)
            print(f'Algo se rompió de nuevo en {filename}. Terminando query.')

##### Main
# Declara variables clave (quizá debamos esconder todo esto hehehe, las 3 variables son clave)
SCOPES = ["https://www.googleapis.com/auth/analytics.readonly"]
KEY_FILE_LOCATION = "KEY_FILE_LOCATION"
VIEW_ID = "VIEW_ID"

# Instacía conexión
service = initialize_analytics_reporting()

### Datasets para Pestaña 1
# Organic Indicators
for i in ['90', '180', '365']:
    query_organica(query_metrics = ['ga:sessions',
                                    'ga:transactions',
                                    'ga:transactionsPerSession'],
                    query_dimensions = ['ga:medium'],
                    start = f'{i}daysago',
                    end = 'yesterday',
                    filename = f'organic_indicators_{i}.pkl')

# Paid Indicators
for i in ['90', '180', '365']:
    query_incom(query_metrics = ['ga:sessions',
                                    'ga:transactions',
                                    'ga:transactionsPerSession'],
                query_dimensions = ['ga:medium'],
                start = f'{i}daysago',
                end = 'yesterday',
                filename = f'paid_indicators_{i}.pkl')

# Organic Sessions Ts
for i in ['90', '180', '365']:
    query_organica(query_metrics = ['ga:sessions'],
                   query_dimensions = ['ga:date'],
                   start = f'{i}daysago',
                   end = 'yesterday',
                   filename = f'organic_sessions_ts_{i}.pkl')

# Paid Sessions Ts
for i in ['90', '180', '365']:
    query_incom(query_metrics = ['ga:sessions'],
                query_dimensions = ['ga:date'],
                start = f'{i}daysago',
                end = 'yesterday',
                filename = f'paid_sessions_ts_{i}.pkl')

# Campaign Detail
for i in ['90', '180', '365']:
    query_incom(query_metrics = ['ga:sessions'],
                query_dimensions = ['ga:source',
                                    'ga:medium',
                                    'ga:campaign'],
                start = f'{i}daysago',
                end = 'yesterday',
                filename = f'campaign_detail_{i}.pkl')

# Paid Groupings
for i in ['90', '180', '365']:
    query_incom(query_metrics = ['ga:sessions'],
                query_dimensions = ['ga:campaign',
                                    'ga:channelGrouping'],
                start = f'{i}daysago',
                end = 'yesterday',
                filename = f'paid_groupings_{i}.pkl')

### Datasets para Pestaña 2
# Search Trends
pytrends = TrendReq(hl='sp-MX', geo='MX', tz=360)
search_term = ['TOEFL',
               'TOEFL IBT MEXICO',
               'MEXICO EXAMEN INGLES',
               'CERTIFICACION DE INGLES',
               'TOEFL ONLINE']

today = pd.to_datetime('today')
ayearago = today - pd.Timedelta(days=365)

today = today.strftime('%Y-%m-%d')
ayearago = ayearago.strftime('%Y-%m-%d')

time_window = ayearago + ' ' +today
pytrends.build_payload(kw_list=search_term, timeframe=time_window, geo = 'MX')
interest_over_time_df = pytrends.interest_over_time()
interest_over_time_df.to_pickle('incom/datasets/search_trends_365.pkl')

# Paid Map
for i in ['90', '180', '365']:
    query_incom_map(query_metrics = ['ga:sessions'],
                    query_dimensions = ['ga:country',
                                        'ga:region'],
                    start = f'{i}daysago',
                    end = 'yesterday',
                    filename = f'paid_map_{i}.pkl')
# Paid Hours
for i in ['90', '180', '365']:
    query_incom(query_metrics = ['ga:sessions'],
                query_dimensions = ['ga:hour'],
                start = f'{i}daysago',
                end = 'yesterday',
                filename = f'paid_hours_{i}.pkl')
# Summary Table
for i in ['90', '180', '365']:
    query_incom(query_metrics = ['ga:sessions',
                                'ga:users',
                                'ga:adCost',
                                'ga:bounceRate',
                                'ga:avgSessionDuration',
                                'ga:transactions',
                                'ga:transactionRevenue'],
                query_dimensions = ['ga:campaign'],
                start = f'{i}daysago',
                end = 'yesterday',
                filename = f'summary_table_{i}.pkl')