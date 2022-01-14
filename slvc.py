import streamlit as st
import pandas as pd
import numpy as np


### Laod the data ###

df = pd.read_csv("SLVC.csv")


### Utlities Functions ####

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


def videoDisplayer(videoURLs):
    if len(videoURLs) > 1:
        col1.write("Results " + str(len(videoURLs)))
    count = 0
    nCols = int(len(videoURLs)/4)
    while (count < len(videoURLs)):
        columns = col_full.columns(4)
        old_count = count 
        count +=4
        urls = videoURLs.iloc[old_count:count]
        for column, videoURL in zip(columns, urls):
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
            videos.append(row['File'])
    return videos
  
 ### Forntend ####           

st.header("The Second Language Video Corpus")
col1, col2 = st.columns([3, 1])


title = col1.text_input('Search videos')
search_option = col2.selectbox(
     'Choose what to search?',
     ('All', 'Phrasal Verbs'))
if search_option == 'Phrasal Verbs':
    selected_videos = keywordSearch(title)
    videoDisplayer(selected_videos)
if search_option == 'All':
    selected_videos = keywordSearch(title)
    videoDisplayer(selected_videos)


expander = st.expander("Explore Data")
col_full = st.container()

#### Sidebar ####

with st.sidebar.form("my_form"):

    st.subheader("Filter options")

    video_gnere_option = st.selectbox(
        "Select Video Genre",
        ("Academic Lectures", "Government advertisement")
    )
    video_gnere_option = list(video_gnere_option)
    selected_videos = df.loc[df['Genre'].isin(video_gnere_option)]


    accent_options = st.multiselect(
        "Speaker's Accent",
        ['American', 'Australian', 'Canadian', 'British'],
        ['American']
        )
    accent_options = list(accent_options)
    selected_videos = df.loc[df['Accent'].isin(accent_options)]

    CEFR_options = st.selectbox(
        "CEFR Levels",
        ('B1')
    )


    values = st.slider(
        'Select a range of difficulty values',
        5.0, 25.0, (10.0, 15.0))

    values_list =list(values)
    selected_videos = df[df['Difficulty'].between(values_list[0], values_list[1])]


    COCA_list_options  = st.radio(
      'Lexical coverage',
     ('BNC/COCA K1', 'BNC/COCA K1-2', 'BNC/COCA K1-3', 'BNC/COCA K1-4'))

    slider_val = st.slider("Lexical coverage %", 0,100)

    agree = st.checkbox('Show Dataframe')

   
 


    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted and agree:
        expander.dataframe(selected_videos)
        videoDisplayer(selected_videos['URL'])
    else:
        videoDisplayer(df['URL'][:50])
 

