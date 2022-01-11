import streamlit as st
import pandas as pd
import numpy as np


data = pd.read_csv("PV_lemtaized.csv")
VP = data.set_index('File name')


videoURLS = [
    "https://www.youtube.com/watch?v=5qap5aO4i9A",
     "https://www.youtube.com/watch?v=5qap5aO4i9A", 
     "https://www.youtube.com/watch?v=5qap5aO4i9A", 
     "https://www.youtube.com/watch?v=5qap5aO4i9A", 
     "https://www.youtube.com/watch?v=5qap5aO4i9A"
         "https://www.youtube.com/watch?v=5qap5aO4i9A",
     "https://www.youtube.com/watch?v=5qap5aO4i9A", 
     "https://www.youtube.com/watch?v=5qap5aO4i9A", 
     "https://www.youtube.com/watch?v=5qap5aO4i9A", 
     "https://www.youtube.com/watch?v=5qap5aO4i9A"
         "https://www.youtube.com/watch?v=5qap5aO4i9A",
     "https://www.youtube.com/watch?v=5qap5aO4i9A", 
     "https://www.youtube.com/watch?v=5qap5aO4i9A", 
     "https://www.youtube.com/watch?v=5qap5aO4i9A", 
     "https://www.youtube.com/watch?v=5qap5aO4i9A"
         "https://www.youtube.com/watch?v=5qap5aO4i9A",
     "https://www.youtube.com/watch?v=5qap5aO4i9A", 
     "https://www.youtube.com/watch?v=5qap5aO4i9A", 
     "https://www.youtube.com/watch?v=5qap5aO4i9A", 
     "https://www.youtube.com/watch?v=5qap5aO4i9A"
         "https://www.youtube.com/watch?v=5qap5aO4i9A",
     "https://www.youtube.com/watch?v=5qap5aO4i9A", 
     "https://www.youtube.com/watch?v=5qap5aO4i9A", 
     "https://www.youtube.com/watch?v=5qap5aO4i9A", 
     "https://www.youtube.com/watch?v=5qap5aO4i9A"
         "https://www.youtube.com/watch?v=5qap5aO4i9A",
     "https://www.youtube.com/watch?v=5qap5aO4i9A", 
     "https://www.youtube.com/watch?v=5qap5aO4i9A", 
     "https://www.youtube.com/watch?v=5qap5aO4i9A", 
     "https://www.youtube.com/watch?v=5qap5aO4i9A"
     ]


def videoDisplayer(videoURLs):
    for col in range(0, len(videoURLS),4):
        columns = st.columns(3)
        for column, videoURL in zip(columns, videoURLS):
            column.video(videoURL)

def keywordSearch(input):
    ketwords = input.split(",")
    for x in ketwords + VP["PV_list_lemmtaized"]:
    
        X = x.replace(", ", ",")
        VP_list = X.split(",")
    
        if x in ketwords and x in VP_list:
            st.write(x)

            

 

title = st.text_input('Search for a word in videos')
keywordSearch(title)

# videoDisplayer(videoURLS)


option = st.sidebar.selectbox(
    "Video Genre",
    ("Academic Lectures", "Government advertisement")
)
if option == "Academic Lectures":
    st.write("Academic Lectures")
if option == "Government advertisement":
    st.write("Government advertisement")
