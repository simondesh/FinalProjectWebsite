import streamlit as st
import pandas as pd

df = pd.read_csv('data_for_EDA.csv')

st.set_page_config(page_title="Data Frame Display 📊", page_icon="📊")

st.markdown("# Data Frame Display")
st.sidebar.header("Data Frame Display")
st.write(
    """This division illustrates the data frame we use for the EDA and Topic Modelling."""
)

st.dataframe(df, width=700, height=300)

st.markdown("""
## 🎮 Columns 🎮

The following columns represent key attributes of steam game data.

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
