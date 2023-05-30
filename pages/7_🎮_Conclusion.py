import streamlit as st

st.set_page_config(page_title="🎮 Conclusion", page_icon="🎮")

st.markdown("# 🎮 Conclusion")

st.write( """
         After the whole analysis, we have the following findings:
          1. Older games seem to be more popular than newer games. For a new game, the release day and month could be later to gain more owners from the model testing. It should reflect on two aspects that it is harder to produce popular games, and in the same year, it is important for a game producer to decide the specific day and month to release the game while there is a negative correlation between the day, month and populartiy(median of owners).
          2. The high rating of a game may not depend on single genre or category, but here for simple analysis. When assuming that the performance of each genres is independent, we found out that Massively Multiplayer games tend to have much lower ratings than any other genre and RPG games have slightly better ratings than most.
          3. There is a better pricing strategy for producers to but it is not a single determinant feature for the populartiy. It should be better for producers to predict the popularity by the model we created which also engages other features.
          4. There is nearly no correlations between developer and ratings, meaing that they do not determine the popularity.
          5. The optimal way to predict the popularity is to use the model that considers number of achievements of the games, price, ratings, required age, genres, and date of relase. 
            
             """)