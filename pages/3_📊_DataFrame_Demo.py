import streamlit as st
import pandas as pd

df = pd.read_csv('df.csv')

st.set_page_config(page_title="Our Dataframe", page_icon="📊")

st.markdown("# Our DataFrame")
st.sidebar.header("Our DataFrame")
st.write(
    """This page displays the dataframe we use to conduct the EDA and also the topic modeling. The specific data collection, cleaning, preprocessing, and wrangling is explained in the other part"""
)
