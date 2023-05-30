import streamlit as st

st.set_page_config(page_title="💪🏼 Limitations and Future Work", page_icon="💪🏼")

st.markdown("# 💪🏼 Limitations")

url = 'https://raw.githubusercontent.com/simondesh/FinalProjectWebsite/main/src/images/limitation.png'

st.image(url, width=500)

st.write(
    """
    Now it is the time for some confesions for our limitations.
        
    Firstly, the data we grasped from the steam spy api has a sort of data loss issue. As the steam official website does not allow web scrapping and also limits non-authorised users to feach data by its API, we have to use steam_spy for more data, such as release year, positive and negative comments, and etc. The steam_spy api is created by nonofficial steam engineers, so that out of some unknown reasons, it has a data loss issue. 

    Secondly, the price of the games are not as same as when they were released. Steam often provides discount on the game, the price we get in the data frame is the current price as of the api calling date. There is no way to get track of their previous price one by one so that we cannot analyse the influence of discount or not and also are unable to use their original to produce the model. 

    Thirdly, out of privacy protection regulation, we cannot get some interesting data that could better for constructing the model. There is another website called SteamDB, which provides a more thorough data of the games, such as the price of the skins, xxx in the game. However, only academic scholars can apply for the authoried use for scraping the web. Our application is denied so we can only stick to the steam spy api. Also, steam official websites does not allow api call for private information of game players, developers and publishers. The meterial we can use is quite limited. 
    
   """
)
