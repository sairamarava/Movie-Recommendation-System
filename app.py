import streamlit as st
import pickle
import pandas as pd

# Load data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)


# Function to recommend movies
def recommend(movie):
    try:
        movies_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movies_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        for i in movies_list:
            recommended_movies.append(movies.iloc[i[0]].title)
        return recommended_movies
    except IndexError:
        st.error("Movie not found in the dataset.")
        return [], []

# Streamlit app title
st.header('Movie Recommender System :movie_camera:',divider="rainbow")

# Movie selection
selected_movie = st.selectbox('Which movie do you like?', movies['title'].values)

# Recommendation button
if st.button('Recommend'):
    names = recommend(selected_movie)
    for name,no in zip(names,[1,2,3,4,5]):
        st.header(str(no)+"."+name, divider="grey")
