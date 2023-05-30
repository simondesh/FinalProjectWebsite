import streamlit as st
import pandas as pd

url_1 = 'https://raw.githubusercontent.com/simondesh/FinalProjectDS105/blob/main/data/cleaned/steam_clean.csv'
df_1 = pd.read_csv(url_1)

url_2 = 'https://raw.githubusercontent.com/simondesh/FinalProjectDS105/blob/main/data/cleaned/data_for_EDA.csv'
df_2 = pd.read_csv(url_2)

url_3 = 'https://raw.githubusercontent.com/simondesh/FinalProjectDS105/blob/main/data/cleaned/data_model.csv'
df_3 = pd.read_csv(url_3)

st.set_page_config(page_title="📊 Data Frame Display ", page_icon="📊")

st.markdown("# 📊 Data Frame Display")


st.write(
    """
    This division illustrates the data frames we use for the EDA and Topic Modelling.
        
    """   
)


st.subheader("1) Original Data Frame - steam_clean.csv")
st.write(
    """
    Besides, during the topic modelling, we use the `steam_clean.csv`, which is the original data frame we use for the EDA and Topic Modelling.
    """
)

st.dataframe(df_1, width=700, height=300)

st.markdown(
    """
    #### The unchanged columns are `appid`, `name`, `ccu`, `achievements`, `average_playtime`, `median_playtime`, `price`, `developer`, `publisher`, `ratings`, `genres`, `categories`, `steamspy_tags`.
    
    The collection, cleaning, preprocessing and cleaning will be dicussed futher in the Data Collection page.
    """
     )

st.subheader("2) Data Frame for EDA - data_for_EDA.csv")

st.write(
    """
    The first data frame is the data frame for EDA, which contains the data we use for the EDA. 
    
    We deleted some of the columns unused in EDA and also created few new columns for the EDA, such as rating. 
    
    Therefore, the differences between this `data_for_EDA.cs` and`steam_clean.csv` are quite obvious:
    
    1. `data_for_EDA.csv` has 13 columns, while `steam_clean.csv` has 18 columns.
    2. `release_year` is in the `data_for_EDA.csv`, derived from `release_date` in `steam_clean.csv`.
    3. `median_owners` is in the `data_for_EDA.csv`, derived from `owners` in `steam_clean.csv`, while `owners` is deleted in the `data_for_EDA.csv`.
    4. `languages` is deleted in the `data_for_EDA.csv`, because it is not used in the EDA.
    5. `english` and `platforms` are deleted in the `data_for_EDA.csv`, because we also select english games and games supporting windows playing on the data preprocessing stage.
    6. `genres`, `categories`, `steamspy_tags` are wrangled by pivoting the `steam_clean.csv`.
    7. `positive_ratings` and `negative_ratings` are deleted in the `data_for_EDA.csv`, because we use the `ratings` column to represent the rating of the game.

    Basically,`data_for_EDA.csv` is derived from `steam_clean.csv`, but it is more suitable for the EDA.
    
    Besides, during the topic modelling, we use the `steam_clean.csv`, which is the original data frame we use for the EDA. The specific data collection of this data frame will be presented later on the Data Collection page.
    """
)

st.dataframe(df_2, width=700, height=300)

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
- **achievements:** These are rewards the games receive. 
- **average_playtime:** The average amount of time players spend on the game.
- **median_playtime:** The median amount of time players spend on the game.

### 📊 Ownership and Rating Information

- **median_owners:** The median number of individuals who own the game. 
- **total_ratings:** Sum up of the number of positive and negative ratings.
- **ratings:** Detailed rating of the game, based on the algorithm that will be discussed in the methodology section.

### 💵 Price Information

- **price:** The cost to purchase the game.

### 🏷️ Genre and Tags Information

- **categories:** The classifications that apply to the game's features and mechanics.
- **genres:** The type of game, determined by its gameplay interaction.
- **steamspy_tags:** The tags of the game produced by SteamSpy, a third-party Steam analytics website.
""")

st.subheader("3) Data Frame for Topic Modelling - data_model.csv")

st.write(
    """

 """
)
