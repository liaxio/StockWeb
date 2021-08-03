# description : this is a stock market dashboard that I have been researching to show the charts and data

# Import the lib
from typing import Any, Union

import streamlit as st
import pandas as pd
import yfinance as yf
from PIL import Image




# adding title and image
from pandas import Series, DataFrame
from pandas.core.generic import NDFrame
from pandas.io.parsers import TextFileReader

st.write("""
# Stock Market Web Application
**Visually** show data on stock by Sanjida Firdaws, Data range from Feb 3, 2020 - June 30, 2020
""")

image = Image.open("C:/Users/sanji/PycharmProjects\pythonProject/venv/stock-exchanges.jpg")
st.image(image, use_column_width=True)

# create a sidebar header
st.sidebar.header('User Input')
#data = yf.download("FB NELX FOX TMUS VZ", start="2020-02-01", end="2020-06-30")

# create a function to get users input
def get_input():
    start_date = st.sidebar.text_input("Start Date", "2020-02-03")
    end_date = st.sidebar.text_input("End Date", "2020-06-29")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "FB")
    return start_date, end_date, stock_symbol


# create a function to get the company name
def get_company_name(symbol):
    if symbol == 'FB':
        return 'FaceBook'
    elif symbol == 'NELX':
        return 'Netflix'
    elif symbol == 'FOX':
        return 'FOX'
    elif symbol == 'TMUS':
        return 'T-Mobile'
    elif symbol == 'VZ':
        return 'Verizon'
    else:
        'None'

# create a function to get the proper company data and the proper timeframe from the user start dat to teh end date
def get_data(symbol, start, end):

    #load the data
    if symbol.upper() == 'FB':
        #FB = yf.Ticker("FB")
        df = pd.read_csv("C:/Users/sanji/PycharmProjects/pythonProject/Stock/FB (1).csv")

    elif symbol.upper() == 'NELX':
        #NELX = yf.Ticker("NELX")
        df = pd.read_csv("C:/Users/sanji/PycharmProjects/pythonProject/Stock/NFLX.csv")

    elif symbol.upper() == 'FOX':
      # FOX = yf.Ticker("FOX")
        df = pd.read_csv("C:/Users/sanji/PycharmProjects/pythonProject/Stock/FOX.csv")

    elif symbol.upper() == 'TMUS':
        #TMUS = yf.Ticker("TMUS")
        df = pd.read_csv("C:/Users/sanji/PycharmProjects/pythonProject/Stock/TMUS.csv")

    elif symbol.upper() == 'VZ':
        #VZ = yf.Ticker("VZ")
        df = pd.read_csv("C:/Users/sanji/PycharmProjects/pythonProject/Stock/VZ (1).csv")

    else:
        df = pd.DataFrame(columns=['Date', 'Close', 'Open', 'Volume', 'Abj Close', 'High', 'Low'])

    # get the date range
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    # set the start and end index rows both to 0
    start_row = 0
    end_row = 0

    # start the date from the top of the data set and go down to see if the users start date is less than or equal to the date set
    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row = i
            break

    # start from the bottom of the data set and go up to see if the users end date is greater than or equal to the date in the data set
    for j in range(0, len(df)):
        if end >= pd.to_datetime(df['Date'][len(df) - 1 - j]):
            end_row = len(df) - 1 - j
            break

    # set the index to be the date
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.iloc[start_row:end_row + 1, :]


# get the users input
start, end, symbol = get_input()
# get the data
df = get_data(symbol, start, end)
# ge the company name
company_name = get_company_name(symbol.upper())

# display the close price
st.header(company_name + "Close Price \n")
st.line_chart(df['Close'])

# display the volume price
st.header(company_name + "Volume \n")
st.line_chart(df['Volume'])

# get statistics on the data
st.header('Data Statistics')
st.write(df.describe())
