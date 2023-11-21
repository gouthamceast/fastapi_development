import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
         # simple stock price app
         Shown Are The Stock Price & volume of Google

         """)

tickersymbol = 'GOOGL'

tickerdata = yf.Ticker(tickersymbol)

tickerDf = tickerdata.history(period='1d', start='2010-5-31', end='2020-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

