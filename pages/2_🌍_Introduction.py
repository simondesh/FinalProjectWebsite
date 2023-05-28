import streamlit as st


st.set_page_config(page_title="🌍 Introduction", page_icon="🌍")

st.markdown("# 🌍 Introduction")
st.sidebar.header("🌍 Introduction")

url = 'https://raw.githubusercontent.com/simondesh/FinalProjectWebsite/main/src/images/steam.png'

st.image(url, width=500)


st.write(
    """
    Steam, which provides access to thousands of games, is one of the biggest platforms for game players, publishers and developers. New games released by the Steam always become the hot titles online, and millions of players are playing games via Steam every day. Until now, there are around games on Steam. The number of games just came out as of Septermber in 2022 reaches to 50,000. Apart from new games, many old games such as CSGO have made a legend in the computer game history. 
    
    Among all the games, some are popular while others are not purchased by many. Game creation indeed is a great industry. Successfully creating a popular game can always make a fortune to the developers, which motivates many to join the market. Thus, our team is curious about what makes games popular. We would like to provide suggestions to creators, investors and publishers about how to produce a popular game from the dimension of genre, price, release year, and etc.
    
    """
)
