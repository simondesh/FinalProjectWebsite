import streamlit as st


st.set_page_config(page_title="🌍 Introduction", page_icon="🌍")

st.markdown("# 🌍 Introduction")
st.sidebar.header("🌍 Introduction")

url = 'https://raw.githubusercontent.com/simondesh/FinalProjectWebsite/main/src/images/steam.png'

st.image(url, width=750)


st.write(
    """
    Steam, which provides access to thousands of games, is one of the biggest platforms for game players, publishers and developers. New games released by the Steam always become the hot titles online, and millions of players are playing games via Steam every day. Until now, there are around games on Steam. The number of games just came out as of Septermber in 2022 reaches to 50,000. Apart from new games, many old games such as CSGO have made a legend in the computer game history. 
    
    Among all the games, some are popular while others are not purchased by many. Game creation indeed is a great industry. Successfully creating a popular game can always make a fortune to the developers, which motivates many to join the market. Thus, our team is curious about what makes games popular. We would like to provide suggestions to creators, investors and publishers about how to produce a popular game from the dimension of genre, price, release year, and etc.
    
    To begin with, we identify the popularity of game by rating, which was produced with negative and positive reviews by ourselves. The laster methodology part will further illustrate how we made it. 

    For the project, we first conducted a correlation analysis to observe what variables might have an influence on the popularity of the game, and also discover the positive relation between rating scores and number of owners to prove that these two variables can all represent the popularity.

    After the correlation analysis, we selected the categorical and numeric features that we would like to explore further  - genres, categories, steam_spy_tags, price, release day month..., 

    The full analysis is divided into two parts. First part goes to the exploratory data analysis on the effects of game type and pricing. Then, we use the XGBoost to build up a model to analyse the influence of the variables stated beforehand, on the purpose of creating a model to predict the popularity of games by forcasting their number of owners. 
    """
)
