import streamlit as st
import pandas as pd
import numpy as np




videoURLS = ["https://www.youtube.com/watch?v=5qap5aO4i9A", "https://www.youtube.com/watch?v=5qap5aO4i9A", "https://www.youtube.com/watch?v=5qap5aO4i9A"]


def videoDisplayer(videoURLs):
    columns = st.columns(len(videoURLS))
    for column, videoURL in zip(columns, videoURLS):
        column.video(videoURL)

def keywordSearch(input):
    ketwords = input.split(",")
    for k in ketwords:
        st.write('The current movie title is', k)


with st.container():

    title = st.text_input('Search for a word in videos')
    keywordSearch(title)

    videoDisplayer(videoURLS)
 

option = st.sidebar.selectbox(
    "Video Genre",
    ("Academic Lectures", "Government advertisement")
)
if option == "Academic Lectures":
    st.write("Academic Lectures")
if option == "Government advertisement":
    st.write("Government advertisement")
