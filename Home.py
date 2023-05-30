import streamlit as st

st.set_page_config(
    page_title="Analysis of Popularity of Steam Games - DS105SuperStars' Version",
    page_icon="👋",
)

st.write("# Welcome to the Analysis of Popularity of Steam Games - DS105SuperStars' Version 👋")

st.sidebar.success("Select a section above.")

st.markdown(
    """
    This project analyses the popularity of Steam games. 
    It is divided into 7 sections:
    0. Data Frame Display
    1. Introduction
    2. Data Collection, Cleaning, Preprocessing and Wrangling
    3. Exploratory Data Analysis
    4. Topic Modelling
    5. Limitations and Future Work
    6. Conclusion
        
    **👈 You can select a division from the sidebar** to view our whole project parts by parts.
    
    Also, we welcome you all to go to our Github repositories:

    Link to backend repo: https://github.com/simondesh/FinalProjectDS105

    Link to website repo: https://github.com/simondesh/FinalProjectWebsite
    
    The producers of this project are: (in alphabetical order of last name)
    Shuyu Cao
    Simon Desh
    Siji He
    Yinyue Wang
    
    The prodcution allocation is as follows:
    ||Shuyu Cao|Simon Desh|Siji He|Cynthia Wang|
    |----|-----|----|----|---|
    |Data Collection|-|√|-|-|
    |Data Cleaning, Preprocessing and Wrangling|-|√|√|-|
    |EDA|-|-|√|√|
    |Topic Modeling|-|√|-|-|
    |Report|√|√|√|-| 
    |Web Creation|√|√|√|-| 
    |Github Maintenance|√|√|√|√| 
    """
)
