import streamlit as st
from PIL import Image
import xgboost as xgb
import numpy as np

st.set_page_config(page_title="💡 Topic Modelling - XBGoost", page_icon="💡")


# Title
st.title("💡 Topic Modelling - XBGoost")

# Introduction
st.header("Introduction")
st.write("The goal of this report is to create a machine learning model that 'predicts' the popularity of games, measured by the number of owners. We will utilize the powerful XGBoost algorithm to capture the complex relationships between features and the target variable. XGBoost is particularly suitable for handling large datasets with skewed and partially missing data, as well as categorical variables. It excels at capturing non-linear relationships and provides insights into feature importance.")
st.write("XGBoost's ensemble of weak decision trees, combined with gradient boosting, allows it to model intricate patterns in the data. Additionally, XGBoost provides mechanisms to handle imbalanced datasets, which is valuable given the uneven distribution of owners in our dataset.")


# Model Creation
st.header("Model Creation")
st.write("Our approach involves two stages:")
st.write("1. Building a preliminary XGBoost model to identify the important features.")
st.write("2. Developing a second model that predicts the range of owners based on the important features.")

# Dataset Preparation
st.header("Dataset Preparation")
st.write("To prepare the dataset for modeling, we performed several steps:")
st.write("1. Owners Distribution: Due to the uneven distribution of owners, we regrouped the last four owner ranges into one category to predict a range of owners.")
col1, col2, col3 = st.columns([0.15,1,0.25])
with col1:
    pass
with col2:
    image1 = Image.open("./src/images/model/DistributionOfOwner.png")
    st.image(image1)
with col3:
    pass
st.write("2. Year Game Release: Considering that games released recently may not have reached their full potential, we only included games released before 2023.")
st.write("3. Drop Duplicates and Create Columns: Duplicates were removed, and additional columns for game categories, genre, and tags were created to enrich the feature set.")
st.write("4. Filter Platform: We filtered the dataset to focus on specific platforms of interest.")
st.write("5. Release Date: We added columns representing the day of the week to capture the impact of the release day. We excluded the year as it is not a choice made by the publisher or developer.")

# Model Training
st.header("Model Training")
st.write("Using the prepared features, we trained our XGBoost model. XGBoost's ability to handle complex relationships and its feature importance analysis make it a suitable choice for this task.")

# Performance Analysis
st.header("Performance Analysis")
st.write("To assess the accuracy of our model, we compared its performance with the highest correlation achieved by individual features. Despite no feature showing a strong correlation with median owners, our model achieved significantly better performance, with an accuracy of approximately 70%. The ROC curves for all classes were above 0.5 AUC, indicating that our model performs better than random guessing.")
image2 = Image.open("./src/images/model/RankingCorrelation.png")
image3 = Image.open("./src/images/model/ROCCurves.png")

col1, col2 = st.columns([1.5,1])
with col1:
    st.image(image2, use_column_width=True)
with col2:
    st.image(image3, use_column_width=True)

st.write("However, the model exhibited some limitations. It tends to over-predict games with low numbers of owners and under-predict those with higher numbers. This is due to the scarcity of data for popular games. The model also struggled to accurately predict games in the middle range of owners (20,000 to 200,000). Nevertheless, the model provides a good indication of the probability of failure for a game.")

col1, col2, col3 = st.columns([0.15,1,0.25])
with col1:
    pass
with col2:
    image4 = Image.open("./src/images/model/ClassificationReport.png")
    st.image(image4, use_column_width=True)
with col3:
    pass



# Error Analysis
st.header("Error Analysis")
st.write("The normalized confusion matrix confirmed the model's limitations in predicting the different owner classes. It tended to over-predict the 0-20k owners class while under-predicting the other classes.")
col1, col2, col3 = st.columns([0.15,1,0.25])
with col1:
    pass
with col2:
    image5 = Image.open("./src/images/model/NormalizedConfusionMatrix.png")
    st.image(image5)
with col3:
    pass

# Feature Importance
st.header("Feature Importance")
st.write("The feature importance analysis revealed that ratings, number of achievements, price, and release date had the most significant impact on the model's predictions. Ratings, although collected after release, can be estimated from beta testing and serve as an indicator of potential user response. The number of achievements reflects game quality and provides a sense of accomplishment for players. Price incentivizes players, especially for free-to-play games. The release date also plays a role in a game's success.")
col1, col2, col3 = st.columns([0.15,1,0.25])
with col1:
    pass
with col2:
    image6 = Image.open("./src/images/model/FeatureImportance.png")
    st.image(image6)
with col3:
    pass

# Conclusion
st.header("Conclusion")
st.write("The XGBoost-based machine learning model developed for predicting game owner numbers demonstrated promising results, outperforming the highest correlation achieved by individual features. We identified several key factors for game developers to consider, including positive ratings during inner testing, reasonable pricing, creating many achievements, and selecting favorable release dates.")
st.write("However, it's essential to recognize that our current model has limitations. It primarily focuses on external factors and does not incorporate elements related to game quality. Future work should aim to incorporate features related to animation, user experience, graphic design, and story development to further improve the predictive accuracy of the model.")
st.write("In summary, our XGBoost-based model provides valuable insights and guidance for game developers, helping them make informed decisions to maximize their game's success.")

# Predicting My Game success
st.header("Predicting My Game success")
st.write("To demonstrate the model's usefulness, we created a simple web app that allows users to input their game's features and predict its success. ")

model = xgb.Booster()
model.load_model('./src/0001.model')

col1, col2, col3, col4 = st.columns([1,1,1,1])
with col1:
    feature1 = st.number_input("Number of Achievements", min_value=0, max_value=10000, value=40)
with col2:
    feature2 = st.number_input("Price", min_value=0.0, max_value=100.0, value=6.99)
with col3:
    feature3 = st.number_input("Ratings(%)", min_value=0.0, max_value=100.0, value=97.80)
with col4:
    feature4 = st.number_input("Required Age", min_value=0.0, max_value=100.0, value=16.0)

genres = ['multi_player','action','adventure','casual','indie','massively_multiplayer','rpg','racing','simulation','sports','strategy']

genre = st.multiselect("Tag & Genres", genres,default=['casual','adventure','rpg'])


# Create a function to compare the selected tags with the tags in the dataset and return a list of 1s and 0s
def compare_lists(long_list, short_list):
    result = []
    for value in long_list:
        if value in short_list:
            result.append(1)
        else:
            result.append(0)
    return result

genre_list = compare_lists(genres, genre)

# Calendar input for selecting a date
selected_date = st.date_input('select day of release')

# Extract the day and month from the selected date
selected_day = selected_date.day
selected_month = selected_date.month

X = [feature1, feature2, feature3, feature4] + genre_list + [int(selected_day), int(selected_month)]

input_data = np.array([X])

# Convert input data to XGBoost's DMatrix format
dmatrix = xgb.DMatrix(input_data)

# Make predictions
predictions = model.predict(dmatrix)

classes = ['0-20 000', '20 000-50 000', '50 000-100 000', '100 000-200 000','200 000-500 000','500 000-1 000 000','1 000 000-2 000 000','2 000 000-5 000 000','5 000 000-10 000 000','10 000 000-200 000 000']

st.write("---")

st.write("Predicted number of owners: <span style='color:red'>{}<span>".format(classes[int(predictions[0])]), unsafe_allow_html=True)
