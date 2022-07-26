import streamlit as st
import pandas as pd
import pickle
import requests
import ast
movie_info = pd.read_csv('movie_info.csv')
with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

def get_poster(index):
    url = f"https://api.themoviedb.org/3/movie/{index}?api_key=cef31bd96f97e41d6e34b3b03292fae5&language=en-US"
    resp = requests.get(url)
    data = resp.json()
    return data, "http://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    index = movie_info[movie_info['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])[1:11]
    movies = []
    posters = []
    for tup in distances:
        mv = movie_info.iloc[tup[0]].title
        movies.append(mv)
        _, url = get_poster(movie_info.iloc[tup[0]].movie_id)
        posters.append(url)
    return movies, posters

st.header("Movie Recommender System")
movie = st.selectbox('', movie_info.title.values)
if st.button("Recommend"):
    mvs, posters = recommend(movie)
    col1, col2 = st.columns(2)
    index = movie_info[movie_info['title'] == movie].index[0]
    data, url = get_poster(movie_info.iloc[index].movie_id)

    with col1:
        st.image(url, width=300)
    with col2:
        st.header('Details')
        st.subheader(movie)
        d = data
        print(type(d))
        overview = d['overview']
        print(overview)
        release_date = d['release_date']
        print(release_date)
        rating = d['vote_average']
        print(rating)
        genres = ', '.join([ge['name'] for ge in d['genres']])
        print(genres)
        st.write("Genres: "+ genres)
        st.write("Relase Date: "+ release_date)
        st.write("Rating: "+ str(rating))
        st.write("Overview:  "+ overview)
        #print(overview, release_date, rating, genres)

    st.subheader("Recommendations for you..!")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(mvs[0])
        st.image(posters[0])

    with col2:
        st.text(mvs[1])
        st.image(posters[1])
    
    with col3:
        st.text(mvs[2])
        st.image(posters[2])
    
    with col4:
        st.text(mvs[3])
        st.image(posters[3])
    
    with col5:
        st.text(mvs[4])
        st.image(posters[4])

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(mvs[5])
        st.image(posters[5])
    with col2:
        st.text(mvs[6])
        st.image(posters[6])
    with col3:
        st.text(mvs[7])
        st.image(posters[7])
    with col4:
        st.text(mvs[8])
        st.image(posters[8])
    with col5:
        st.text(mvs[9])
        st.image(posters[9])
