import streamlit as st
import pandas as pd

url_1 = 'https://raw.githubusercontent.com/simondesh/FinalProjectWebsite/main/src/data/data_for_EDA.csv'
df_1 = pd.read_csv(url_1)

url_2 = 'https://raw.githubusercontent.com/simondesh/FinalProjectWebsite/main/src/data/steam_clean.csv' 
df_2 = pd.read_csv(url_2)

st.set_page_config(page_title="📊 Data Frame Display ", page_icon="📊")

st.markdown("# 📊 Data Frame Display")


st.write(
    """
    This division illustrates the data frames we use for the EDA and Topic Modelling
        
    """   
)

st.subheader("1) Data Frame for EDA")

st.write(
    """
    The first data frame is the data frame for EDA, which contains the data we use for the EDA. 
    
    We deleted some of the columns unused in EDA and also created few new columns for the EDA, such as rating. 
    
    Therefore, the difference between this `data_for_EDA.cs` and`steam_clean.csv` is quite obvious that the columns such as xxx are missing, while rating xxx are newly created. 
    
    Basically,`data_for_EDA.csv` is derived from `steam_clean.csv`, but it is more suitable for the EDA.
    
    Besides, during the topic modelling, we use the `steam_clean.csv`, which is the original data frame we use for the EDA. The specific data collection of this data frame will be presented later on the Data Collection page.
    """
)

st.dataframe(df_1, width=700, height=300)

st.markdown("""
## 🎮 Columns 🎮

The following columns represent key attributes of steam game data in the `data_for_EDA.csv`.

---

### 🔑 Identifying Information

- **appid:** Unique identifier for each game. 
- **name:** Name of the game.

### 📅 Release Information

- **release_year:** The year in which the game was released. 
- **developer:** The individual or company that developed the game. 
- **publisher:** The individual or company that published the game.

### 🕹️ Gameplay Information

- **ccu:** The highest number of players simultaneously online.
- **achievements:** These are challenges or tasks within the game that a player can complete to receive rewards, such as badges or points. 
- **average_playtime:** The average amount of time players spend on the game.
- **median_playtime:** The median amount of time players spend on the game.

### 📊 Ownership and Rating Information

- **median_owners:** The median number of individuals who own the game. 
- **total_ratings:** The total number of ratings the game has received. 
- **ratings:** Detailed rating of the game.

### 💵 Price Information

- **price:** The cost to purchase the game.

### 🏷️ Genre and Tags Information

- **categories:** The classifications that apply to the game's features and mechanics.
- **genres:** The type of game, determined by its gameplay interaction.
- **steamspy_tags:** The tags of the game produced by SteamSpy, a third-party Steam analytics website.
""")


st.subheader("2) Steam Clean Data Frame - Topic Modelling")
st.write(
    """
    Besides, during the topic modelling, we use the `steam_clean.csv`, which is the original data frame we use for the EDA.
    """
)

st.dataframe(df_2, width=700, height=300)

st.markdown(
    """
    ### The same columns are explained below:
    
    
    """
     )

