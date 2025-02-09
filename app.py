


import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data=response.json()
    return  "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movies_posters=[]

    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        #fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

movies_dict=pickle.load(open("movie_dict.pkl","rb"))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open("similarity.pkl","rb"))

st.title("Movie Recommender System")

select_movie_name =st.selectbox(
      "Select a movie to get recommendations",
movies['title'].values)

if st.button("Recommond"):
    names,posters= recommend(select_movie_name)

    col1,col2,col3,col4,col5= st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

# from http.client import responses
# import streamlit as st
# import pickle
# import pandas as pd
# import requests
# import time
#
#
# # Function to fetch movie poster from TMDb API
# def fetch_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
#
#     for _ in range(3):  # Retry up to 3 times
#         try:
#             response = requests.get(url, timeout=10)
#             response.raise_for_status()  # Raises HTTP errors (4xx, 5xx)
#             data = response.json()
#             if 'poster_path' in data and data['poster_path']:  # Check if poster exists
#                 return f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
#             else:
#                 return "https://via.placeholder.com/500x750?text=No+Image"
#         except requests.exceptions.RequestException as e:
#             print(f"Error fetching poster for movie ID {movie_id}: {e}")
#             time.sleep(3)  # Wait before retrying
#
#     return "https://via.placeholder.com/500x750?text=No+Image"  # Return a placeholder if all retries fail
#
#
# # Function to recommend movies
# def recommend(movie):
#     try:
#         movie_index = movies[movies['title'] == movie].index[0]
#         distances = similarity[movie_index]
#         movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#         recommended_movies = []
#         recommended_movies_posters = []
#         for i in movies_list:
#             movie_id = movies.iloc[i[0]].movie_id
#             recommended_movies.append(movies.iloc[i[0]].title)
#             recommended_movies_posters.append(fetch_poster(movie_id))
#
#         return recommended_movies, recommended_movies_posters
#     except Exception as e:
#         print(f"Error in recommendation system: {e}")
#         return [], []  # Return empty lists if an error occurs
#
#
# # Load movie data
# movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
# movies = pd.DataFrame(movies_dict)
# similarity = pickle.load(open("similarity.pkl", "rb"))
#
# # Streamlit UI
# st.title("Movie Recommender System")
#
# select_movie_name = st.selectbox(
#     "Select a movie to get recommendations:",
#     movies['title'].values
# )
#
# if st.button("Recommend"):  # Fixed typo
#     names, posters = recommend(select_movie_name)
#
#     if names:  # Check if recommendations exist
#         col1, col2, col3, col4, col5 = st.columns(5)
#
#         with col1:
#             st.text(names[0])
#             st.image(posters[0])
#         with col2:
#             st.text(names[1])
#             st.image(posters[1])
#         with col3:
#             st.text(names[2])
#             st.image(posters[2])
#         with col4:
#             st.text(names[3])
#             st.image(posters[3])
#         with col5:
#             st.text(names[4])
#             st.image(posters[4])
#     else:
#         st.error("Could not generate recommendations. Please try again.")
