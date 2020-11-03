from forex_python.converter import CurrencyRates
from datetime import datetime, timedelta
import pandas as pd
import plotly
import plotly.graph_objs as go
import numpy as np
import json

c = CurrencyRates()

def get_current_rate(): 
    current_rate = c.get_rate('EUR', 'SEK')
    return current_rate

# get current date
def get_date(): 
    return datetime.now().date()

# get previous month's date
def get_start_date(): 
    end_date = get_date()
    start_date = (end_date-timedelta(days=30))
    return start_date

#get last 30 days dates, to access date = get_date_range()[0].date()
def get_date_range(): 
    start_date = get_start_date()
    end_date = get_date()
    return pd.date_range(start_date,end_date,freq='d')
    
#get array of past rates
def get_past_rates(date_range): 
    all_rates = []
    for date in date_range: 
        rate = c.get_rate('EUR', 'SEK', date.date())
        all_rates.append(rate)
    return all_rates

def create_plot():

    dates = get_date_range()
    rates = get_past_rates(date_range=dates)

    df = pd.DataFrame({'date': dates, 'rate': rates}) # creating a sample dataframe

    data = [
        go.Scatter(
            x=df['date'], # assign x as the dataframe column 'x'
            y=df['rate']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

