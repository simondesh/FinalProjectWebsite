import streamlit as st


st.set_page_config(page_title="📈 EDA", page_icon="📈")

st.markdown("# 📈 Exploratory Data Analysis")

st.write("For further analysis, we focused on the influence of each factor, including release year, genres, developers and publishers, number of owners and pricing, on rating scores (which is calculated in wrangling section, and we define it as the indicator of successful game performance." )

st.header("📌 Data Preprocess and Overview")

markdown_text1 = """
Before stepping into the deeper analysis on each factor, we did a data preprocessing to reduce some side effects and variables for easier plots. Firstly, we only focused on English games that are played on Windows, since they take the majority of the steam games. What’s more, we converted `release_date` to `release_year`, as we found that most games released in the same year have similar rating scores, hence greater impact of year compared to dates. Finally, we added a data pivoting table of categories and genres to the dataframe by selecting the main categories and genres (which will be explained later). The the final dataframe for EDA use can be seen in “Data Frame Display” section.
        
Based on the processed dataframe, we first used `seadorn` to inspect kernel density estimation and scatter plots of each factors that we are interested in where we made our inital observations. Then we plotted a heatmap to discover the correlations between factors that are presented in numbers.
"""

st.markdown(markdown_text1)



data_overview = 'https://raw.githubusercontent.com/simondesh/FinalProjectWebsite/main/src/images/data_overview.png'
heatmap = 'https://raw.githubusercontent.com/simondesh/FinalProjectWebsite/main/src/images/heatmap.png'

col1, col2 = st.columns(2)

with col1:
    st.image(data_overview)

with col2:
    st.image(heatmap)


markdown_text2 = """
Initial observations we made:
    
- Ratings decreases overtime, suggesting that the newer the game is, the lower ratings it has.
- As price increases, ratings increase, suggesting that people are more likely to rate higher if they spend more money on that game.
- Higher ratings will be resulted from more owners, suggesting that games with more owners will gain higher ratings.

Based on the initial correlations we found, we then did a closer check of our assumptions.
"""

st.header("📆 Release Year")
st.write("From the data overview above, we can notice that rating scores seem to decrease overtime, but the number of releases has been increasing overtime. Thus, we examined the ratings distribution by release year here.")

release_year = 'https://raw.githubusercontent.com/simondesh/FinalProjectWebsite/main/src/images/release_year.png'
st.image(release_year)

markdown_text3 = """
#### Conclusions:

- Number of releases does increase overtime with a short drop between 2018 and 2019 which is not significant.
- The mean rating dropped approximately by 10% in total, while there is a dramatic decrease between 2013 and 2014.
- After 2013, under half of games are scored over 75, suggesting that high ratings are less likely to occur overtime.

Generally, older games tend to have higer rating scores, although more games are released recently.
"""
st.markdown(markdown_text3)


st.header("📥 Categories and Genres")
st.write("We first drawed a wordcloud to see which genres, categories or tags are more relevant.")


word_cloud = 'https://raw.githubusercontent.com/simondesh/FinalProjectWebsite/main/src/images/wordcloud.png'
st.image(word_cloud)


st.write('By observing the wordclouds we produced, we decided to focus on the “main” categories and genres as appeared on the plots. Also we wanted to remove the steamspy_tags column, since we found that most of the tags are exactly the same of categories and genres. Below shows the correlations between genres we focused on and their frequency, which we used for data pivoting mentioned above:')

genres_heatmap = 'https://raw.githubusercontent.com/simondesh/FinalProjectWebsite/main/src/images/genres_heatmap.png'
genres_barchart = 'https://raw.githubusercontent.com/simondesh/FinalProjectWebsite/main/src/images/genres_barchart.png'


col1, col2 = st.columns(2)

with col1:
    st.image(genres_heatmap)

with col2:
    st.image(genres_barchart)


markdown_text4 = """
We can see that there is correlation between different genres, which means one game can have several genres. It suggests that the high rating of a game may not depend on single genre or category, but here for simple analysis, we assume that the performance of each genres is independent.
What’s more, We found that most games are categorised as 'single-player', and the genre of 'indie' takes the most percentage of all games. Also, 'massively_multiplayer', 'racing' and 'sports' games are the least.

Then we stepped into the impact of genres on rating scores by using seaborn
"""
st.markdown(markdown_text4)


rating_distribution_genres = 'https://raw.githubusercontent.com/simondesh/FinalProjectWebsite/main/src/images/rating_distribution_by_genre.png'
st.image(rating_distribution_genres)

markdown_text5 = """
we can see that Massively Multiplayer games tend to have much lower ratings than any other genre and RPG games have slightly better ratings than most.

#### Conclusions:

- More games are categorised as single-player, but its correlation with rating is not examined here.
- High frequency does not mean higher ratings. Indie genre take the highest frequency, but it doesn't seem to contribute to a higher rating.
- Massively Multiplayer games take the least proportion, and it contributes to lower ratings as well.

But lower frequency does not mean lower ratings. Although RPG games only take a small proportion of all games, it has a slightly higher rating than others.
"""
st.markdown(markdown_text5)

st.header("💶 Owners and Pricing")
st.write("By observing the information of top ten successful games in terms of rating scores, we found that all of these games have achieved a significant milestone of having at least two million owners and the price varies from the lowest 3.99 to the highest 58.99. Continuing our analysis, we narrowed our focus to paid games with 20,000 or more owners. We first examined the distribution of ratings among these games.")


rating_distribution_paid_games = 'https://raw.githubusercontent.com/simondesh/FinalProjectWebsite/main/src/images/rating_distribution_paid_games.png'
st.image(rating_distribution_paid_games)


markdown_text6 = """
According to the plot, we could find the distribution of ratings is left-skewed with approximately half of the ratings falling within the 60% to 80% range, which indicates games generally receive a higher proportion of positive ratings compared to negative ratings. 

Then we used seaborn to find the relationships between owners, pricing, ratings, log number of owners and log number of ratings as shown below:
"""
st.markdown(markdown_text6)


owners_and_pricing = 'https://raw.githubusercontent.com/simondesh/FinalProjectWebsite/main/src/images/owners_and_pricing.png'
st.image(owners_and_pricing)


markdown_text7 = """
#### Conclusions:

Upon the two plots on the left, they show that

- The more owners of a game, the more times that game is likely to have been rated 
- the rating score will be higher with a larger number of owners
  
This relationship is quite intuitive, as it is expected that better games would gain more popularity and consequently receive more positive ratings. There are also a few exceptions that deviate from the observed trend. 

For the two plots on the right, comparing the price of a game to the number of ratings and the rating score, we could not clearly identify the relationship between price and ratings. It is probably because the rating of a game typically reflects the overall quality, gameplay experience and other factors that contribute to the enjoyment of players. While price can be a factor that affects owners' expectations and initial interest in a game, it does not necessarily determine the actual quality or the rating it receives.
"""
st.markdown(markdown_text7)

st.header("🛠 Developers and Publishers")
st.write("Firstly, it is noticeable that most games are published by their developers, in other words, the publisher column is highly overlapped with the developer column. Thus, at this stage, we only focused on the developers and narrowed the dataset to top 30 developers. Below shows the distribution of average rating scores for top 30 developers.")


avg_ratings_developers = 'https://raw.githubusercontent.com/simondesh/FinalProjectWebsite/main/src/images/average_ratings_by_developers.png'
st.image(avg_ratings_developers)


st.write("It is surprising to find that there is nearly no correlations between developer and ratings. It can be explained as one developer tends to develop many different genres of games, where genres seem to have greater influence on ratings. However, since we only examined the performances of 30 developers, we cannot conclude that developers have no impact on rating scores. A further analysis on the reputation of developers would be mentioned in model prediction section.")







