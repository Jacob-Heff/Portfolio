import streamlit as st
import yfinance as finance
from datetime import date
 
def get_ticker(name):
    company = finance.Ticker(name)  # google
    return company
 
TODAY = date.today()
START = f'{TODAY.year - 5}-01-01'
END = f'{TODAY.year + 5}-01-01'

# Project Details
st.title("Build and Deploy Stock Market App Using Streamlit")
st.header("A Basic Data Science Web Application")
st.sidebar.header("Geeksforgeeks \n TrueGeeks")
 
company1 = get_ticker("GOOGL")
company2 = get_ticker("MSFT")
 
# fetches the data: Open, Close, High, Low and Volume
google = finance.download("GOOGL", start=START, end=END)
microsoft = finance.download("MSFT", start=START, end=END)
 
# Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
data1 = company1.history(period="3mo")
data2 = company2.history(period="3mo")
 
# markdown syntax
st.write("""
### Google
""")
 
# detailed summary on Google
st.write(company1.info['longBusinessSummary'])  
st.write(google)
 
# plots the graph
st.line_chart(data1.values)  
 
st.write("""
### Microsoft
""")
st.write(company2.info['longBusinessSummary'], "\n", microsoft)
st.line_chart(data2.values)