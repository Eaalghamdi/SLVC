import streamlit as st
import pandas as pd
import numpy as np


df = pd.read_csv("PV_lemtaized.csv")
VP = df.set_index('File name')

def _max_width_(prcnt_width:int = 90):
    max_width_str = f"max-width: {prcnt_width}%;"
    st.markdown(f""" 
                <style> 
                .reportview-container .main .block-container{{{max_width_str}}}
                </style>    
                """, 
                unsafe_allow_html=True,
    )
_max_width_()


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
    keywords = input.split(",")
    videos = []

    # videos = df.loc[df['PV_list_lemmtaized'].isin(keywords)]
    for index, row in df.iterrows():
    
        X = row["PV_list_lemmtaized"].replace(", ", ",")
        VP_list = X.split(",")
    
    
        # if x in ketwords and x in VP_list:
        result =  any(elem in keywords for elem in VP_list)
        if result:
            videos.append(row['File name'])
    return videos
  
            

st.header("The Second Language Video Corpus")

title = st.text_input('Search for a word in videos')
selected_videos = keywordSearch(title)

videoDisplayer(selected_videos)

#### Sidebar ####

with st.sidebar.form("my_form"):

    st.subheader("Filter options")

    video_gnere_option = st.selectbox(
        "Select Video Genre",
        ("Academic Lectures", "Government advertisement")
    )
    if video_gnere_option  == "Academic Lectures":
        st.write("Academic Lectures")
    if video_gnere_option  == "Government advertisement":
        st.write("Government advertisement")



    values = st.slider(
        'Select a range of difficulty values',
        5.0, 25.0, (5.0, 20.0))

    values_list =list(values)
    Difficulty_df = df[df['Difficulty Score (5-25)'].between(values_list[0], values_list[1])]


    COCA_list_options  = st.radio(
      'Lexical coverage BNC/COCA',
     ('K1', 'K1-2', 'K1-3', 'K1-4'))

    slider_val = st.slider("Lexical coverage %", 0,100)
 

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("values", values_list)

