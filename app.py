import streamlit as st
import sqlite3
import pandas as pd

st.title('Flow Dashboard')

connect = sqlite3.connect(r'C:\Users\mary saotome\Documents\database\financial.db')
cursor = connect.cursor()

def get_values():
    query = 'SELECT * FROM flow'
    df = pd.read_sql_query(query, connect)
    return df

st.subheader('Data info')
flow_df = get_values()

st.dataframe(flow_df)


