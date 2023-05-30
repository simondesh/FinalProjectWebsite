import streamlit as st

st.set_page_config(page_title="🔍 Data Collection, Cleaning, Preprocessing & Wrangling", page_icon="🔍")
st.title("🔍 Data Collection, Cleaning, Preprocessing & Wrangling ")

st.header("⭐️ Data Collection")

st.subheader("Our Goals")
st.markdown("""
Our primary objective is to analyze the features that contribute to a game's success on Steam. To achieve this, we will utilize the Steam and SteamSpy APIs to gather relevant data on games sold on Steam. 
""")

st.subheader("1) Generating a List of AppIDs")
st.markdown("""
To gather data for our analysis, we will need a list of AppIDs for games on Steam. However, the Steam API provides a large number of games, many of which may not be relevant to our study.  To overcome this, we will leverage the SteamSpy API, which provides genre information to curate a list of games that are relevant to our analysis. This is especially true because it allows all our data to have SteamSpy genres. ( + The Steam API has a lot of empty information and the SteamSpy is a curated subset of it organised by popularity without the invalid data. )
""")
            
st.subheader("2) API Request Logic")
st.markdown("""
**1. API call handler**

To handle API calls to both the Steam and SteamSpy APIs, we will develop a function that can effectively manage the different API requests. This function will handle the parsing and processing of responses from the APIs, ensuring smooth data retrieval. This means that for a given GameID we can obtain either the Steam or SteamSpy response through this method.

**2. Request Handling**

Making multiple API requests requires careful handling to manage potential errors and server limitations. We implement an error-handling wrapper and incorporate rate-limiting strategies to ensure reliable data retrieval. 

""")

st.subheader("3) Downloading Logic")
st.markdown("""
We created a function to download the data from the APIs and save it to a CSV file. This function will keep track of the progress and handle errors and interruptions, allowing us to resume the data collection process seamlessly. It is in other words the main brain of the data collection process. 

We have a saving mechanism that saves every batch so that even in case of network disconnecting we have the saved-up data. It also creates an index to know where to start from in case of restart. This makes the code perfect to run on a server using CRON. 
""")

st.subheader("4) Gathering the Data")

st.markdown("""
Finally, here are examples of data gathering using our custom function. 
""")

st.code("""
create_csv("Steamspy",stop = 20, container_size = 3, pause = 0.5)

create_csv("Steam",stop = 20, container_size = 3, pause = 1)
# The pause is the time between each API call.
# The container size is the number of API calls per batch.
# The stop is the index to stop at.
""")

st.markdown("""
SteamSpy API allows for a higher rate of API calls per minute compared to the Steam API. The data collection code took a few days to run. 
""")


st.header("⭐ ️Initial Data Cleaning")

st.write("Before making further analysis, we had to first clean and merge the two raw datasets to a tidy data frame. For cleaning, we had two initial focuses including missing values and duplicated games, then we processed each column in the two datasets for data wrangling.")

st.subheader("1) Steam Data Cleaning")


markdown_text1 = """
We first removed unnecessary columns and rows by following criteria:

**1. Columns with more than 50% missing values.**

Here, we used `.isnull()` to define missing values. By using the threshold of 50%, we dropped columns with more than 29579 missing values including `controller_support`, `dlc`, `fullgame` and other seven columns.

**2.Missing values under `type` and `name` columns.**

Here, we also used `.isnull()` to define missing values. These two columns are really important to identify one specific game, so if this game has no type or name, we’d like to remove it. We removed 68 + 6 rows in total.

**3.Duplicated rows**

Here, we simply removed duplicated rows by using `.drop_duplicates()`. We dropped 5 duplicated rows in total.

**4.Unwanted information**

We dropped some columns that are not interesting to us and may not support our initial goal, including:

"""

st.markdown(markdown_text1)


python_code1 = '''
unwanted_col = ['detailed_description',
    'about_the_game', 'short_description', 'header_image', 'website',
    'pc_requirements', 'mac_requirements', 'linux_requirements', 
    'screenshots', 'movies', 'support_info', 'background']
'''

st.code(python_code1)

st.subheader("2) Steamspy Data Cleaning")

markdown_text2 = """
For the second dataset from Steamspy, we also dropped unwanted data based on following criteria:

**1. Columns with too many missing values.**

Again, here we used the same method mentioned above.

**2. Columns duplicated with Steam dataset.**

We define duplicated columns by observing the similar column names between two datasets.

**3. Temporary columns which only show the short-term game performance.**

In particular, there are two temporary columns - `average_2weeks` and `median_2weeks`- which only show the game performance in a specific period of time. Since we're only interested in the long-term performance of games not at a specific period of time, we removed these tow unrelevant columns as well.
"""

st.markdown(markdown_text2)


python_code2 = '''
drop_cols = [
    'score_rank','userscore', # too many missing values
    'genre', 'developer', 'publisher', 'price', 'initialprice', 'discount', # provided by Steam data
    'average_2weeks', 'median_2weeks' # not interested in temporary specific columns
]
'''

st.code(python_code2)


st.header("⭐️ Data Preprocessing & Wrangling")
st.subheader("1) Steam Data Wrangling")

markdown_text3 = """
There are 10 columns in total, and we wrangled each column by observing its data characteristics, such as 

- converting them into same data type (e.g. `required_age` column)
- splitting the dictionary and storing the value in a list (e.g. `platforms`, `price_overview`, `categories` and `supported_languages` columns)
- and converting Nan value to ‘0’ (e.g. `achievements` column)

**However**, there are some interesting wrangling processes we’d like to talk about in this section:
"""
st.markdown(markdown_text3)

markdown_text4 = """
#### Processing `price`

For more accurate and consistent price information, we wanted to combine the `is_free` and `price_overview` columns and keep price’s unit and currency same. Therefore, we converted all price values to EUR with unit of 1 euro. For exchange rate, we used the rate on the mid-day of **13 April, 2023** as shown below.
"""

st.markdown(markdown_text4)

python_code3 = '''
currency_df = price_df.copy()
currency_df.loc[currency_df['currency'] == 'USD', 'price'] *= 0.91
currency_df.loc[currency_df['currency'] == 'SGD', 'price'] *= 0.68
currency_df.loc[currency_df['currency'] == 'BRL', 'price'] *= 0.18
currency_df.loc[currency_df['currency'] == 'AUD', 'price'] *= 0.61
currency_df.loc[currency_df['currency'] == 'JPY', 'price'] *= 0.0068

# now remove the currency column which no longer needed
currency_df = currency_df.drop(['currency'], axis=1)
'''

st.code(python_code3)

markdown_text5 = """
#### Parsing `release_date` format

We found 8 different formats of release date in the raw dataset, thus we used `.research()` function to find them all and parse them into a same format of “%d %b %Y” for further analysis. Below shows the function we defined to parse this column:
"""

st.markdown(markdown_text5)

python_code4 = '''
def parse_date(x):
    """
    Parse the date into "%d %b %Y" format.
    """
    if re.search(r'[\d]{1,2} [A-Za-z]{3}, [\d]{4}', x):
        return x.replace(',', '')
    
    elif re.search(r'[A-Za-z]{3} [\d]{4}', x):
        return '1 ' + x

    elif re.search(r'[A-Za-z]{3} [\d]{2}, [\d]{4}', x):
        day = x[4:6]
        month = x[:3]
        year = x[-4:]
        return day + ' ' + month + ' ' + year
    
    elif re.search(r'[A-Za-z]{3} [\d]{1}, [\d]{4}', x):
        day = x[4]
        month = x[:3]
        year = x[-4:]
        return day + ' ' + month + ' ' + year
    
    elif re.search(r'[\d]{2}. [A-Za-z]{3}. [\d]{4}', x):
        return x.replace('.', '')
    
    elif re.search(r'[\d]{4} 年 [\d]{1,2} 月 [\d]{1,2} 日', x):
        year, month, day = re.findall(r'[\d]+', x)
        month = calendar.month_name[int(month)][:3]
        return day + ' ' + month + ' ' + year
    
    elif re.search(r'[\d]{4}年[\d]{1,2}月[\d]{1,2}日', x):
        year, month, day = re.findall(r'[\d]+', x)
        month = calendar.month_name[int(month)][:3]
        return day + ' ' + month + ' ' + year

    elif x == '':
        return np.nan
'''

st.code(python_code4)

markdown_text6 = """
#### Parsing `negative_ratings` and `positive_ratings`

We used the [SteamDB](https://steamdb.info/blog/steamdb-rating/) method to generate the total and average rating for each game for the use of analysing their performance. And this average rating is the main indicator in our project to define the success of a game. The rating algorithm can be seen below:
"""

st.markdown(markdown_text6)

python_code5 = '''
def parse_rating(df):
    """
    Get the rating from positive and negative rating columns based on SteamDB method
    """
    pos = int(df['positive_ratings'])
    neg = int(df['negative_ratings'])
    
    total_rating = pos + neg
    if total_rating != 0:
        average = pos / total_rating
    else:
        average = 0
    
    score = average - (average*0.5) * 2 ** (-math.log10(total_rating + 1))
return score *100
'''

st.code(python_code5)


st.subheader("2) Steamspy Data Wrangling")

markdown_text7 = """
For Steamspy dataset, we only focused on the `owners` and `tags` columns, since other columns are overlapped with ones in Steam dataset.

Firstly, we calculated the median number of owners for each game by using the range of owners provided in the raw dataset, because we believe the median number can be a good central tendency indicator compared to upper or lower bounds. 

Secondly, there are two information under the tags column, including genres or categories the game belongs to and the evaluated values for each tag. We remained the genres and categories as `steamspy_tags` for data frame merging, but for their evaluated values, we created a new data pivoting table for further analysis (we didn’t examined this table at the end, since they are not relevant to success analysis).

| appid | name                     | 1980s | 1990s | 2.5d | 2d | 2d_fighter | 2d_platformer | 360_video | 3d | ... |
|-------|--------------------------|-------|-------|------|----|------------|---------------|------------|----|-----|
| 10    | Counter-Strike           | 274   | 1206  | 0    | 0  | 0          | 0             | 0          | 0  | ... |
| 20    | Team Fortress Classic    | 0     | 147   | 0    | 0  | 0          | 0             | 0          | 0  | ... |
| 30    | Day of Defeat            | 0     | 0     | 0    | 0  | 0          | 0             | 0          | 0  | ... |
| 40    | Deathmatch Classic       | 0     | 11    | 0    | 0  | 0          | 0             | 0          | 0  | ... |
| 50    | Half-Life: Opposing Force| 0     | 144   | 0    | 0  | 0          | 0             | 0          | 0  | ... |
| ...   | ...                      | ...   | ...   | ...  | ...| ...        | ...           | ...        | ...| ... |
"""

st.markdown(markdown_text7)

st.markdown("---")

st.subheader("⭐️ Merge Data: Using pd.merge()")
st.write("""
         Finally, we merged the steam-data and steamspy-data together and rename the columns for future analysis. And the resulted dataframe can be found in the "Data Frame Display" section named steam_clean.csv.
         """)

st.code('''
        merged = steam_data.merge(steamspy_data, left_on='steam_appid', right_on='appid', suffixes=('', '_steamspy'))
        ''')