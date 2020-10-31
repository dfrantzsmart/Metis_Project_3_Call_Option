import streamlit as st

st.title('Call Option Screener')

import pandas as pd
import numpy as np

@st.cache(allow_output_mutation=True)
def load_data():
    df = pd.read_pickle("./yes_execute_10_27.pkl")
    return df

df = load_data()

df_tickers = df['Ticker']

st.subheader('Suggestions for Today:')

def add_stream_url(ticker):
	return [f'https://finance.yahoo.com/quote/{t}' for t in df_tickers]

def make_clickable(url, text):
    return f'<a target="_blank" href="{url}">{text}</a>'

# show data
if st.checkbox('Include URLs'):
	df['Link'] = add_stream_url(df.Ticker)
	df['Link'] = df['Link'].apply(make_clickable, args = (f'Yahoo Finance',))
	st.write(df.to_html(escape = False), unsafe_allow_html = True)
else:
	st.write(df)
