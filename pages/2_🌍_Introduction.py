import streamlit as st


st.set_page_config(page_title="🌍 Introduction", page_icon="🌍")
st.markdown("# 🌍 Introduction")


url = 'https://cdn.cloudflare.steamstatic.com/store/home/store_home_share.jpg'

st.image(url, width=750)

st.subheader("1) Project Introduction")
st.write(
    """
    Steam is one of the biggest platforms for game players, publishers and developers. Game creation indeed is a great industry. Our team is curious about what makes games popular.
    
    To begin with, we identify the popularity of game by rating, which was produced with negative and positive reviews by ourselves.
    
    We first conducted a correlation analysis to observe what variables might have an influence on the popularity of the game, and also discover the strong and positive relation between ratings and median number of owners to prove that these two variables can all represent the popularity.

    After the correlation analysis, we selected release year; genres, categories and steam_spy_tags; price, and studied their influence on the popularity of the game. We also conducted a topic modelling on the effects of achievements, price, ratings, and required age.

    """
)

st.markdown("---")

st.subheader("2) Website Structure")

st.write(
    """
    As shown in the home page, we have many side views on the left for you to browse. 
        
    **0. Data Frame Display**
    
    In this part, you will see what data frame we produce from the data collection - `steam_clean.csv`. We will then show you the `data_for_EDA.csv` which has gone through data preprocessing by removing non-english and non-windows games. This df is used for the EDA.
    
    We will also show you the `data_model.csv` which is used for the topic modelling.
    
    
    **1. Introduction** 
    
    In this part, you will see what is the project about and the website's structure.
    
    **2. Data Collection, Cleaning, Pre-Processing, and Wrangling**
    
    In this part, you will get to know how we collect the data, clean the data, pre-process the data, and wrangle the data.
    
    **3. Exploratory Data Analysis**
    
    In this part, you will see the EDA on the effects of release year, game type, pricing, developers and publishers.
    
    **4. Topic Modelling**
    
    In this part, you will observe the topic modelling on the effects of achievements, price, ratings, and required age.
    
    **5. Limitations and Future Work**
    
    **6. Conclusion**
    
    I summarise all the findings in this part.
    """
)

