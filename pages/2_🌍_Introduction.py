import streamlit as st


st.set_page_config(page_title="🌍 Introduction", page_icon="🌍")
st.markdown("# 🌍 Introduction")


url = 'https://cdn.cloudflare.steamstatic.com/store/home/store_home_share.jpg'

st.image(url, width=750)

st.subheader("1) Project Introduction")
st.write(
    """
    Steam, which provides access to thousands of games, is one of the biggest platforms for game players, publishers and developers. New games released by the Steam always become the hot titles online, and millions of players are playing games via Steam every day. Until now, there are around games on Steam. The number of games just came out as of Septermber in 2022 reaches to 50,000. Apart from new games, many old games such as CSGO have made a legend in the computer game history. 
    
    Among all the games, some are popular while others are not purchased by many. Game creation indeed is a great industry. Successfully creating a popular game can always make a fortune to the developers, which motivates many to join the market. Thus, our team is curious about what makes games popular. We would like to provide suggestions to creators, investors and publishers about how to produce a popular game from the dimension of genre, price, release year, and etc.
    
    To begin with, we identify the popularity of game by rating, which was produced with negative and positive reviews by ourselves. The laster methodology part will further illustrate how we made it. 

    For the project, we first conducted a correlation analysis to observe what variables might have an influence on the popularity of the game, and also discover the strong and positive relation between ratings and median number of owners to prove that these two variables can all represent the popularity.

    After the correlation analysis, we selected the categorical and numeric features that we would like to explore further  -  release year; genres, categories and steam_spy_tags; price. 

    The full analysis is divided into two parts. First part goes to the exploratory data analysis on the effects of release year, game type and pricing. In the second part, we use the XGBoost to build up a model to analyse the influence of the variables including achievements, price, ratings, and required age. The aim is to create a model to predict the popularity of games by forcasting their number of owners, with these varibles. You can see the small prediction application in the end of the topic modelling. Try to predict your games'popularity!
    """
)

st.markdown("---")

st.subheader("2) Website Structure")

st.write(
    """
    As shown in the home page, we have many side views on the left for you to browse. 
    
    Specifically, we would like to introduce the project in the following order:
    
    **0. Data Frame Display**
    
    In this part, you will see what data frame we produce from the data collection - `steam_clean.csv`. We will then show you the 'data_for_EDA.csv` which has gone through data preprocessing by removing non-english and non-windows games. This df is used for the EDA.
    
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

