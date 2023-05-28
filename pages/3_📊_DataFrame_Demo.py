import streamlit as st
import pandas as pd


st.set_page_config(page_title="Our Dataframe", page_icon="📊")

st.markdown("# Our DataFrame")
st.sidebar.header("Our DataFrame")
st.write(
    """This demo shows how to use `st.write` to visualize Pandas DataFrames.
(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)"""
)
