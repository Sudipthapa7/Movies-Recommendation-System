import streamlit as st
import pickle
import requests

def recommend(movie):
    movie_index = movie_df[movie_df['title'] == movie].index[0]
    movie_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie = []
    recommended_movie_poster = []
    for i in movie_list:
        recommended_movie.append(movie_df.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_poster(movie_df.iloc[i[0]].id))
    return recommended_movie, recommended_movie_poster


def fetch_poster(movie_id):
    responses = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'. format(movie_id))
    data = responses.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500"+data['poster_path']


st.title('Movie Recommendation System')

movie_df = pickle.load(open('movies.pkl','rb'))
movies = movie_df['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))

selected_movie_name = st.selectbox('search for movie...', movies)



if st.button('Recommend'):
    name, poster = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(name[0])
        st.image(poster[0])
    with col2:
        st.text(name[1])
        st.image(poster[1])
    with col3:
        st.text(name[2])
        st.image(poster[2])
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4])